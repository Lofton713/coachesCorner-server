from rest_framework.viewsets import ViewSet
from coachescornerapi.models.college import College
from rest_framework.response import Response
from rest_framework import serializers, status

from coachescornerapi.views.player import PlayerSerializer




class CollegeView(ViewSet):
    """College view"""

    def retrieve(self, request, pk):
        """handle GET requests for a single college
        """

        try:
            college = College.objects.get(pk=pk)
            serializer = CollegeSerializer()
            return Response(serializer.data)
        
        except College.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """The GET for all colleges in the database

        Returns: 
            Response: JSON serialized list of colleges
        """
        colleges = College.objects.all()

        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class CollegeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = College
        fields = ('id', 'name', 'city', 'state', 'min_GPA')
        
    