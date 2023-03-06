from rest_framework import serializers 
from main_oms.models import Orders
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Orders
        fields = ('title', 
        'email',
        'paper_length',
        'topic',
        'audience',
        'written_in',
        'email',
        'deadline',
        'paid')
