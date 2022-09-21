import re
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from coachescornerapi.models import Player, Coach
from coachescornerapi.views.coach import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a player or coach

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)
    # If authentication was successful, respond with their token
    try: 
        user = Player.objects.get(user=authenticated_user)
        
    except Exception: 
        user = Coach.objects.get(user=authenticated_user)
    if authenticated_user is not None:
        
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'user_id': user.id,
            'is_staff': authenticated_user.is_staff,
            'is_active': authenticated_user.is_active
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_coach(request):
    '''Handles the creation of a new player or coach for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_coach = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email']
    )

    # Now save the extra info in the coaches table
    coach = Coach.objects.create(
        bio=request.data['bio'],
        profile_pic=request.data['profile_pic'],
        user=new_coach
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=coach.user)
    # Return the token to the client
    data = { 'token': token.key, 'is_staff': True, 'user_id': coach.id }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_Player(request):
    '''Handles the creation of a new player for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_player = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email']
    )

    # Now save the extra info in the coaches table
    player = Player.objects.create(
        birthday=request.data['birthday'],
        bio=request.data['bio'],
        GPA=request.data['GPA'],
        hometown=request.data['hometown'],
        state=request.data['state'],
        profile_pic=request.data['profile_pic'],
        user=new_player
    )

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=player.user)
    # Return the token to the client
    data = { 'token': token.key, 'user_id': player.id}
    return Response(data)