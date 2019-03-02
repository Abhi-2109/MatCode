from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """
    A serialier for our User profiles Object
    """
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        #extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new user
        """
        user = models.UserProfile(
            email = validated_data["email"],
            name = validated_data["name"]
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class ProblemSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = models.Problem
        fields = '__all__'
        
class SolutionSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = models.Solution
        fields = '__all__'
        
class StatSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = models.Stats
        fields = '__all__'

class CompileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Compile
        fields = '__all__'

