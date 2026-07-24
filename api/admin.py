from django.contrib import admin

from .models import (
    Member,
    Team,
    Project,
    Task,
    Comment,
)


@admin.register(Member)
class AdministrationMembre(admin.ModelAdmin):
    """
    Configuration de l'affichage des membres.
    """

    list_display = ("id", "name", "email")

    search_fields = ("name", "email")


@admin.register(Team)
class AdministrationEquipe(admin.ModelAdmin):
    """
    Configuration de l'affichage des équipes.
    """

    list_display = (
        "id",
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

    filter_horizontal = (
        "members",
    )


@admin.register(Project)
class AdministrationProjet(admin.ModelAdmin):
    """
    Configuration de l'affichage des projets.
    """

    list_display = (
        "id",
        "title",
        "team",
        "status",
    )

    list_filter = (
        "status",
        "team",
    )

    search_fields = (
        "title",
    )


@admin.register(Task)
class AdministrationTache(admin.ModelAdmin):
    """
    Configuration de l'affichage des tâches.
    """

    list_display = (
        "id",
        "title",
        "project",
        "assignee",
        "status",
        "priority",
        "due_date",
    )

    list_filter = (
        "status",
        "priority",
    )

    search_fields = (
        "title",
    )


@admin.register(Comment)
class AdministrationCommentaire(admin.ModelAdmin):
    """
    Configuration de l'affichage des commentaires.
    """

    list_display = (
        "id",
        "author",
        "task",
        "created_at",
    )

    search_fields = (
        "content",
    )


from django.contrib import admin

# Register your models here.
