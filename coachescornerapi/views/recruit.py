from rest_framework.viewsets import ViewSet
from coachescornerapi.models.player import Player
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User

from coachescornerapi.models.recruit import Recruit


class RecruitView(ViewSet):
    """Recruit view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single recruit
        """

        try:
            recruits =Recruit.objects.get(pk=pk)
            serializer = RecruitSerializer(recruits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Recruit.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all Recruits in the database

        Returns: 
            Response: JSON serialized list of tags
        """
        recruits = Recruit.objects.all()

        serializer = RecruitSerializer(recruits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
        

        
class RecruitSerializer(serializers.ModelSerializer):
    """JSON serializer for Recruits"""
    
    class Meta:
        model = Recruit
        fields = ('id',  'coach_id', 'player_id')
        depth = 2