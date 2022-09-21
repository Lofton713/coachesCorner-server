from rest_framework.viewsets import ViewSet
from coachescornerapi.models.player import Player
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User


class PlayerView(ViewSet):
    """Player view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single player
        """

        try:
            user = Player.objects.get(pk=pk)
            serializer = PlayerSerializer(user)
            return Response(serializer.data)
        except Player.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all players

        Returns:
            Response -- JSON serialized list of players
        """
        players = Player.objects.all()
        
        user = request.query_params.get('user', None)
        if user is not None:
            players = Player.objects.filter(player=user)
        
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """handle put"""
        
        player = Player.objects.get(pk=pk)
        user = User.objects.get(player=player)
        
        player.bio = request.data["bio"]
        player.birthday = request.data["birthday"]
        player.GPA = request.data["GPA"]
        player.hometown = request.data["hometown"]
        player.state = request.data["state"]
        player.position = request.data["position"]
        player.grade = request.data["grade"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.email = request.data["email"]
        player.save()
        user.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        
class PlayerSerializer(serializers.ModelSerializer):
    """JSON serializer for Players"""
    user = UserSerializer()
    class Meta:
        model = Player
        fields = ('id',  'user', 'bio', 'profile_pic', 'birthday', 'hometown', 'state', 'GPA', 'grade', 'position')