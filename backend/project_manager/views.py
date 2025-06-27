from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project, Member, Role, ProjectCharter, WorkBreakdownStructure, StatusReport, KanbanBoard, KanbanCard
from .serializers import (ProjectSerializer, MemberSerializer, RoleSerializer, ProjectCharterSerializer, 
    WorkBreakdownStructureSerializer, StatusReportSerializer, KanbanBoardSerializer, KanbanCardSerializer)

from .services import extract_pdf_text, extract_json_from_string

import os
from google import genai


@api_view(['GET'])
def test(request):
    return Response({'0-0': '0-0'})


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ProjectCharterViewSet(viewsets.ModelViewSet):
    queryset = ProjectCharter.objects.all()
    serializer_class = ProjectCharterSerializer


class WorkBreakdownStructureViewSet(viewsets.ModelViewSet):
    queryset = WorkBreakdownStructure.objects.all()
    serializer_class = WorkBreakdownStructureSerializer


class StatusReportViewSet(viewsets.ModelViewSet):
    queryset = StatusReport.objects.all()
    serializer_class = StatusReportSerializer


class KanbanBoardViewSet(viewsets.ModelViewSet):
    queryset = KanbanBoard.objects.all()
    serializer_class = KanbanBoardSerializer


class KanbanCardViewSet(viewsets.ModelViewSet):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer


@api_view(['GET'])
def generate_report(request, project_id):
    """
    Compares data from the 5 most recent reports to generate a short description of the project's current status
    """
    # queries the database for the project
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({'error': f'There is no project with id {project_id}.'}, status=400)

    # queries the database for that project's status reports (queries by reverse chronological order and limits the query to only 5 objects)
    status_reports = StatusReport.objects.filter(project=project).order_by('-created_at')[:5]
    if not status_reports:
        return Response({'error': 'This project has no status reports'}, status=400)
    
    # extracts the text from the reports
    reports_text = 'Status reports: '
    for report in status_reports:
        reports_text += extract_pdf_text(report.document)
        
    # promts ai for a summary of the current status of the project
    api_key = os.getenv('GENAI_API_KEY')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-05-20',
        contents=f'Generate a 3 paragraph long summary of the current status of the project based on the last week\'s status reports. {reports_text}'
    )
    current_status = response.text
    
    project.current_status = current_status
    project.save()
    
    return Response({'current_status': current_status}, status=200)


@api_view(['GET'])
def generate_kanban_board(request, project_id):
    """
    Generates tasks for a kanban board based on the project's work breakdown structure
    """
    # queries the database for the project
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({'error': f'There is no project with id {project_id}.'}, status=400)
    
    # queries the database for a kanban board related to that project
    try:
        board = KanbanBoard.objects.get(project=project)
    except KanbanBoard.DoesNotExist:
        # creates a board for that project in case it doesn't exist
        board = KanbanBoard.objects.create(project=project)
    
    # queries the database for a work breakdown structure related to that project
    try:
        wbs = WorkBreakdownStructure.objects.get(project=project)
    except WorkBreakdownStructure.DoesNotExist:
        return Response({'error': 'That project does not have a work breakdown structure yet.'}, status=400)
    
    # extracts text from the wbs document
    wbs_text = 'work breakdown structure: '
    wbs_text += extract_pdf_text(wbs.document)
    
    # promts ai for tasks based on the components described in the wbs
    api_key = os.getenv('GENAI_API_KEY')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-05-20',
        contents='Generate tasks based on this project\'s work breakdown structure and put them in a json list in the following format: [{"task": "<task>"}]' + wbs_text
    )
    tasks = extract_json_from_string(response.text)
    
    # creates kanbanCard model instances for all of the generated tasks
    for task in tasks:
        task['status'] = 'to do'
        task['board'] = board
        KanbanCard.objects.create(**task)
        # serializes the board so that the tasks can be rendered later
        task['board'] = KanbanBoardSerializer(board).data

    return Response({'tasks': tasks}, status=200)