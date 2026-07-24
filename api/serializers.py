from rest_framework import serializers

from .models import Member, Team, Project, Task, Comment


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, data):
        """
        Vérifie que le membre assigné appartient bien
        à l'équipe du projet.
        """

        membre = data.get("assignee")
        projet = data.get("project")

        # Aucune vérification si aucun membre n'est assigné
        if membre is None:
            return data

        # Vérification de la règle métier
        if membre not in projet.team.members.all():
            raise serializers.ValidationError(
                "Le membre affecté doit appartenir à l'équipe du projet."
            )

        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"