from rest_framework import serializers
from .models import Team, User, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = ['id', 'name']
    def get_id(self, obj):
        return str(obj.id)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']
    def get_id(self, obj):
        return str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'distance']
    def get_id(self, obj):
        return str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']
    def get_id(self, obj):
        return str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points']
    def get_id(self, obj):
        return str(obj.id)
