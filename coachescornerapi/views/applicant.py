from rest_framework.viewsets import ViewSet
from coachescornerapi.models.applicant import Applicant
from rest_framework.response import Response
from rest_framework import serializers, status
from coachescornerapi.models.player import Player
from coachescornerapi.models.open_spot import Open_spot
from coachescornerapi.views.open_spot import OpenSpotSerializer

from coachescornerapi.views.player import PlayerSerializer

class ApplicantView(ViewSet):
    """Applicant view

    """
    
    def retrieve(self, request, pk):
        """handle GET requests for a single open_spot
        """

        try:
            applicant = Applicant.objects.get(pk=pk)
            serializer = ApplicantSerializer()
            return Response(serializer.data)
        
        except Applicant.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all Applicants in the database

        Returns: 
            Response: JSON serialized list of Applicants
        """
        applicants = Applicant.objects.all()
        
        serializer = ApplicantSerializer(applicants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        """ POST operation for a new Open Spot

        Returns:
            Response: JSON serialized open_spot instance
        """
        player = Player.objects.get(user=request.auth.user)
        open_spot = Open_spot.objects.get(pk=request.data["college"])
        
        applicant = Applicant.objects.create(
            player=player,
            open_spot=open_spot
        )

        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ApplicantSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    open_spot = OpenSpotSerializer()
    class Meta:
        model = Applicant
        fields = ('open_spot', 'player')