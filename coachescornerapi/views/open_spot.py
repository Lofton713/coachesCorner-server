from rest_framework.viewsets import ViewSet
from coachescornerapi.models.coach import Coach
from coachescornerapi.models.college import College
from coachescornerapi.models.open_spot import Open_spot
from rest_framework.response import Response
from rest_framework import serializers, status

from coachescornerapi.views.coach import CoachSerializer
from coachescornerapi.views.college import CollegeSerializer

class OpenSpotView(ViewSet):
    """Open_spot view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single open_spot
        """

        try:
            open_spot = Open_spot.objects.get(pk=pk)
            serializer = OpenSpotSerializer()
            return Response(serializer.data)
        
        except Open_spot.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all open_spots in the database

        Returns: 
            Response: JSON serialized list of open_spots
        """
        open_spots = Open_spot.objects.all()
        
        user = request.query_params.get('user', None)
        if user is not None:
            open_spots = Open_spot.objects.filter(posted_by=user)

        serializer = OpenSpotSerializer(open_spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """ POST operation for a new Open Spot

        Returns:
            Response: JSON serialized open_spot instance
        """
        user = Coach.objects.get(user=request.auth.user)
        college = College.objects.get(pk=request.data["college"])
        
        open_spot = Open_spot.objects.create(
            position=request.data["position"],
            description=request.data["description"],
            posted_by=user,
            college=college
        )

        serializer = OpenSpotSerializer(open_spot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
        open_spot = Open_spot.objects.get(pk=pk)
        open_spot.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    
    
        
class OpenSpotSerializer(serializers.ModelSerializer):
    posted_by = CoachSerializer()
    college = CollegeSerializer()
    class Meta:
        model = Open_spot
        fields = ('id', 'college', 'position', 'description', 'posted_by', 'applicants')
        depth = 3
        