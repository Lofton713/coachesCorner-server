from rest_framework.viewsets import ViewSet
from coachescornerapi.models.attendee import Attendee
from rest_framework.response import Response
from rest_framework import serializers, status

from coachescornerapi.views.coach import CoachSerializer
from coachescornerapi.views.player import PlayerSerializer

class AttendeeView(ViewSet):
    """Attendee view"""
    
    def retrieve(self, request, pk):
        """handle GET requests for a single open_spot
        """

        try:
            attendee = Attendee.objects.get(pk=pk)
            serializer = AttendeeSerializer()
            return Response(serializer.data)
        
        except Attendee.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all attendees

        Returns:
            Response -- JSON serialized list of attendees
        """
        attendees = Attendee.objects.all()
        
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized attendee instance
        """
        attendee = Attendee.objects.create(
        game = request.data['game'],
        coach = request.data['coach'],
        player = request.data['player']
            )

        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        attendee = Attendee.objects.get(pk=pk)
        attendee.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        
class AttendeeSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    coach = CoachSerializer()
    class Meta:
        model = Attendee
        fields = ('game_id', 'coach', 'player')