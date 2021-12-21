from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from polls.models import Question, Choice
from rest_framework.decorators import action

from polls.serializers import (
    ChoiceSerializer,
    QuestionSerializer,
    QuestionVoteSerializer,
    QuestionDetailSerializer
)


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        obj = self.get_object()
        serializer = QuestionVoteSerializer(
            data=request.data,
            context={"question": obj})
        if serializer.is_valid():
            data = serializer.validated_data
            selected_choice = obj.choices.get(pk=data['choice_id'])
            selected_choice.votes += 1
            selected_choice.save(update_fields=['votes'])
            return Response({'votes': selected_choice.votes})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update']:
            return QuestionDetailSerializer
        return QuestionSerializer

class OptionViewSet(
        viewsets.GenericViewSet,
        mixins.DestroyModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
