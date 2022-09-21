from rest_framework.viewsets import ViewSet
from coachescornerapi.models.college import College
from coachescornerapi.models.player import Player
from coachescornerapi.models.favorites import Favorite
from rest_framework.response import Response
from rest_framework import serializers, status


from coachescornerapi.views.player import PlayerSerializer
from coachescornerapi.views.college import CollegeSerializer

class FavoriteView(ViewSet):
    """Open_spot view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single open_spot
        """

        try:
            favorite = Favorite.objects.get(pk=pk)
            serializer = FavoriteSerializer()
            return Response(serializer.data)
        
        except Favorite.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all open_spots in the database

        Returns: 
            Response: JSON serialized list of open_spots
        """
        favorites = Favorite.objects.all()
        
        user = request.query_params.get('user', None)
        if user is not None:
            favorites = Favorite.objects.filter(player=user)

        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        """ POST operation for a new Open Spot

        Returns:
            Response: JSON serialized open_spot instance
        """
        player = Player.objects.get(user=request.auth.user)
        college = College.objects.get(pk=request.data["college"])
        
        favorite = Favorite.objects.create(
            player=player,
            college=college
        )

        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
class FavoriteSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    college = CollegeSerializer()
    class Meta:
        model = Favorite
        fields = ('id','college', 'player')
        
        