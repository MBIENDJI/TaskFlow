from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Member,
    Team,
    Project,
    Task,
    Comment,
)

from .serializers import (
    MemberSerializer,
    TeamSerializer,
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer,
)

from .pagination import PaginationTaskFlow


# MEMBRE

class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()

    serializer_class = MemberSerializer

    pagination_class = PaginationTaskFlow


# EQUIPE
class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()

    serializer_class = TeamSerializer

    pagination_class = PaginationTaskFlow

    @action(detail=True, methods=["post"])
    def add_member(self, request, pk=None):
        """
        Ajoute un membre à une équipe.
        """

        equipe = self.get_object()

        member_id = request.data.get("member_id")

        if member_id is None:
            return Response(
                {"erreur": "member_id est obligatoire."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            membre = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return Response(
                {"erreur": "Membre introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        equipe.members.add(membre)

        return Response(
            {"message": "Le membre a été ajouté avec succès."},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["post"])
    def remove_member(self, request, pk=None):
        """
        Retire un membre d'une équipe.
        """

        equipe = self.get_object()

        member_id = request.data.get("member_id")

        if member_id is None:
            return Response(
                {"erreur": "member_id est obligatoire."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            membre = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return Response(
                {"erreur": "Membre introuvable."},
                status=status.HTTP_404_NOT_FOUND
            )

        equipe.members.remove(membre)

        return Response(
            {"message": "Le membre a été retiré avec succès."},
            status=status.HTTP_200_OK)


# PROJET

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()

    serializer_class = ProjectSerializer

    pagination_class = PaginationTaskFlow

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ["status", "team"]


# TACHE

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()

    serializer_class = TaskSerializer

    pagination_class = PaginationTaskFlow

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "status",
        "priority",
        "project",
        "assignee",
    ]



# COMMENTAIRE

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    pagination_class = PaginationTaskFlow

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "author",
        "task",
    ]
