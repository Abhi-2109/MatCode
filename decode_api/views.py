from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from rest_framework import filters

from rest_framework.authtoken.serializers import  AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models.aggregates import Max

from . import serializers
from . import models
from . import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer

    queryset = models.UserProfile.objects.all()

    # Adding token Authentication
    authentication_classes = (TokenAuthentication,)

    # Adding permission classes

    permission_classes = (permissions.UpdateOnProfile,)

    # Adding filters

    filter_backends = (filters.SearchFilter,)

    # adding fields which should be filter

    search_fields =  ('name', 'email')

class LoginViewSet(viewsets.ViewSet):
    """check email and password and returns a auth token"""

    serializer_class = AuthTokenSerializer

    # Define a create request Post Request

    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)



class ProblemApi(generics.ListCreateAPIView):
    """
    Handles with all the IP
    """
    serializer_class = serializers.ProblemSerializer
    queryset = models.Problem.objects.all()

class ProblemApiDetail(generics.RetrieveUpdateDestroyAPIView):

    """Handles the significant IP"""

    serializer_class = serializers.ProblemSerializer
    queryset = models.Problem.objects.all()


class StatsApi(generics.ListCreateAPIView):

    serializer_class = serializers.StatSerializer
    queryset = models.Stats.objects.all()

class StatsApiDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = serializers.StatSerializer
    queryset = models.Stats.objects.all()

class SolutionApi(generics.ListCreateAPIView):

    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()

class SolutionApiDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()

class LeaderBoardView(APIView):
    """To take the top 10 scores"""
    def get(self,request,format = None):
        """Return a list of top 10 leaderBoard"""
        leaderboard_data =list(models.UserProfile.objects.values('score','id','name').order_by('-score'))[:10]
        return Response(leaderboard_data)
