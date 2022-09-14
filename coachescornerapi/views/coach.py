from rest_framework.viewsets import ViewSet
from coachescornerapi.models.coach import Coach
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User

from coachescornerapi.views.college import CollegeSerializer


class CoachView(ViewSet):
    """Coach view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single coach
        """

        try:
            user = Coach.objects.get(pk=pk)
            serializer = CoachSerializer(user)
            return Response(serializer.data)
        except Coach.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all coaches

        Returns:
            Response -- JSON serialized list of coaches
        """
        coaches = Coach.objects.all()
        
        serializer = CoachSerializer(coaches, many=True)
        return Response(serializer.data)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        
class CoachSerializer(serializers.ModelSerializer):
    """JSON serializer for Players"""
    user = UserSerializer()
    college = CollegeSerializer()
    class Meta:
        model = Coach
        fields = ('id',  'user', 'bio', 'profile_pic', 'recruits', 'college')