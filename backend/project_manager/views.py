from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import KanbanCard
from .serializers import KanbanCardSerializer


@api_view(['GET'])
def test(request):
    return Response({'0-0': '0-0'})


class KanbanCardViewSet(viewsets.ModelViewSet):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer

    def destroy(self, request, *args, **kwargs):
        card = self.get_object()
        board = card.board

        self.perform_destroy(card)

        if board.card_count > 0:
            board.card_count -= 1
            board.save()

        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()

