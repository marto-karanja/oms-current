from rest_framework import serializers
from .models import Questions



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class QuestionTitleSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Questions
        fields = ['title']

    def get_title(self, obj):
        return obj.question_titles()
    


class QuestionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['link_no', 'title', 'content', 'category', 'project', 'spider', 'server', 'date_scraped', 'date_recorded', 'processed', 'short', 'link_no', 'no', 'content_length']

class TextSerializer(serializers.ModelSerializer):
    ...

