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
        l =  ObtainAuthToken().post(request)
        print(l)
        print(type(l))
        print(request.data)
        if "non_field_errors" in l:
            print("error tha")
            return l
        else:
            da = l.data
            m = models.UserProfile.objects.values('id','email')
            for i in m:
                print(i)
                if i["email"] == dict(request.data)['username'][0]:
                    print("Andar Gush Gye")
                    da['id'] = i['id']
                    print(l)
                    break
            return Response(da)



class ProblemApi(generics.ListCreateAPIView):
    """
    Handles with all the IP
    """
    serializer_class = serializers.ProblemSerializer
    queryset = models.Problem.objects.all()

class ProblemApiDetail(generics.RetrieveUpdateDestroyAPIView):

    """Handles the significant Problem"""

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

class TemplateApi(generics.ListCreateAPIView):

    serializer_class = serializers.TemplateSerializer
    queryset = models.TemplateCode.objects.all()

class TemplateApiDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = serializers.TemplateSerializer
    queryset = models.TemplateCode.objects.all()



class LeaderBoardView(APIView):
    """To take the top 10 scores"""
    def get(self,request,format = None):
        """Return a list of top 10 leaderBoard"""
        leaderboard_data =list(models.UserProfile.objects.values('score','id','name').order_by('-score'))[:10]
        return Response(leaderboard_data)


class CompileIt(APIView):
    """Compile kar ke output dega"""

    serializer_class = serializers.CompileSerializer
    #queryset = models.Solution.objects.all()

    def get(self,request, blah = None):
        return Response({})

    def post(self, request):
        print(request.data)
        serializer = serializers.CompileSerializer(data = request.data)
        if serializer.is_valid():
            print(serializer.data)
            source_code = serializer.data.get('source_code')
            language_id = serializer.data.get('language_id')
            stdin = serializer.data.get('stdin')
            expected_output = serializer.data.get('expected_output')
            print(expected_output,source_code,language_id,stdin)
            import requests
            URL = "https://api.judge0.com/submissions?wait=true"
            #a = request.data

            #print(a)
            #a = dict(a)
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
            return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST)
