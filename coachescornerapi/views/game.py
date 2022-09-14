from rest_framework.viewsets import ViewSet
from coachescornerapi.models.game import Game
from rest_framework.response import Response
from rest_framework import serializers, status
from coachescornerapi.models.player import Player

from coachescornerapi.views.player import PlayerSerializer




class GameView(ViewSet):
    """Game view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single player
        """

        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer()
            return Response(serializer.data)
        
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all games in the database

        Returns: 
            Response: JSON serialized list of tags
        """
        games = Game.objects.all()
        
        user = request.query_params.get('user', None)
        if user is not None:
            games = Game.objects.filter(player=user)

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class GameSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    class Meta:
        model = Game
        fields = ('id', 'date', 'time', 'description', 'player', 'city', 'state', 'attendees')
        
    