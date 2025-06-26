from rest_framework import serializers
from .models import Project, Member, Role, ProjectCharter, WorkBreakdownStructure, Report, KanbanBoard, KanbanCard


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ProjectCharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCharter
        fields = '__all__'


class WorkBreakdownStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkBreakdownStructure
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class KanbanBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanBoard
        fields = '__all__'


class KanbanCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanCard
        fields = '__all__'