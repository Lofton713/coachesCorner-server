from rest_framework.viewsets import ViewSet
from coachescornerapi.models.game import Game
from rest_framework.response import Response
from rest_framework import serializers, status
from coachescornerapi.models.player import Player

from coachescornerapi.views.coach import CoachSerializer

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
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)

        game = Game.objects.create(
            city=request.data["city"],
            state=request.data["state"],
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            player=player
            
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        
        game = Game.objects.get(pk=pk)
        game.description
        game.date
        game.time
        
        player = Player.objects.get(user=request.auth.user)
        game.player = player
        game.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
class GameSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    attendees = CoachSerializer(many=True)
    class Meta:
        model = Game
        fields = ('id', 'date', 'time', 'description', 'player', 'city', 'state', 'attendees')
        
    