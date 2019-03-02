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

class CompileIt(APIView):
    """Compile kar ke output dega"""

    def get(self,request,format = None):

        return Response({})

    def post(self, request):

        serializer = serializers.CompileSerializer(data = request.data)
        if serializer.is_valid():
            source_code = serializer.data.get('source_code')
            language_id = serializer.data.get('language_id')
            stdin = serializer.data.get('stdin')
            expected_output = serializer.data.get('excepted_output')

            import requests
            URL = "https://api.judge0.com/submissions?wait=true"
            a = request.data

            print(a)
            a = dict(a)
            d = {
                "source_code" : source_code,
                "language_id" : language_id,
                "stdin" : stdin,
                "expected_output" : expected_output,
                "number_of_runs": "1",
                "cpu_time_limit": "2",
                "cpu_extra_time": "0.5",
                "wall_time_limit": "5",
                "memory_limit": "128000",
                "stack_limit": "64000",
                "max_processes_and_or_threads": "30",
                "enable_per_process_and_thread_time_limit": False,
                "enable_per_process_and_thread_memory_limit": True,
                "max_file_size": "1024"
            }
            r = requests.post(url=URL, data = d)
            print(r.json())
            return Response(r.json())
        else:
            return Response({})
