from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project, Member, Role, ProjectCharter, WorkBreakdownStructure, Report, KanbanBoard, KanbanCard
from .serializers import (ProjectSerializer, MemberSerializer, RoleSerializer, ProjectCharterSerializer, 
    WorkBreakdownStructureSerializer, ReportSerializer, KanbanBoardSerializer, KanbanCardSerializer)


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


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class KanbanBoardViewSet(viewsets.ModelViewSet):
    queryset = KanbanBoard.objects.all()
    serializer_class = KanbanBoardSerializer


class KanbanCardViewSet(viewsets.ModelViewSet):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer

