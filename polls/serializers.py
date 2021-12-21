from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        read_only_fields = ('votes', 'id')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'was_published_recently']


class QuestionDetailSerializer(WritableNestedModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = [
            'id', 'question_text', 'pub_date', 'was_published_recently',
            'choices']
        read_only_fields = ('was_published_recently', 'id')


class QuestionVoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()

    def validate(self, data):
        question = self.context.get('question')
        if question:
            try:
                question.choices.get(pk=data['choice_id'])
            except (KeyError, Choice.DoesNotExist):
                raise serializers.ValidationError({
                    'choice_id': 'Choice not found'
                })
        return data
