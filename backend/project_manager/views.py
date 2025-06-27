from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project, Member, Role, ProjectCharter, WorkBreakdownStructure, StatusReport, KanbanBoard, KanbanCard
from .serializers import (ProjectSerializer, MemberSerializer, RoleSerializer, ProjectCharterSerializer, 
    WorkBreakdownStructureSerializer, StatusReportSerializer, KanbanBoardSerializer, KanbanCardSerializer)

from .utils import extract_pdf_text

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
def generate_description(request, project_id):
    # queries the database for the project
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({'error': f'There are no projects with id {project_id}.'}, status=400)
    
    # queries the database for that project's project charter
    try:
        charter = ProjectCharter.objects.get(project=project)
    except ProjectCharter.DoesNotExist:
        return Response({'error': 'There is no project charter for that project.'}, status=400)
    
    # extracts the text from the project charter file
    pdf_text = 'Project charter: '
    pdf_text += extract_pdf_text(charter.document)
            
    # promts ai for a dproject description
    api_key = os.getenv('GENAI_API_KEY')
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-05-20',
        contents=f'Generate a 2 paragraph long description for a project based on its project charter. {pdf_text}'
    )
    
    serializer = ProjectCharterSerializer(charter)
    return Response({'description': response.text}, status=200)
