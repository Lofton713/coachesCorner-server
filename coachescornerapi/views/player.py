from rest_framework.viewsets import ViewSet
from coachescornerapi.models.player import Player
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User
import uuid
import base64

class PlayerView(ViewSet):
    """Rare User view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single user
        """

        try:
            user = Player.objects.get(pk=pk)
            serializer = PlayerSerializer(user)
            return Response(serializer.data)
        except Player.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all RareUsers

        Returns:
            Response -- JSON serialized list of RareUsers
        """
        players = Player.objects.all().order_by("player__username")
        
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        
class PlayerSerializer(serializers.ModelSerializer):
    """JSON serializer for Players"""
    user = UserSerializer()
    class Meta:
        model = Player
        fields = ('id',  'user', 'bio', 'profile_pic', 'birthday', 'hometown', 'state', 'GPA',)