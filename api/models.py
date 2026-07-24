from django.db import models

# ==========================================================
# ENUMERATIONS
# ==========================================================

class StatutProjet(models.TextChoices):
    ACTIF = "ACTIVE", "Actif"
    ARCHIVE = "ARCHIVED", "Archivé"


class StatutTache(models.TextChoices):
    A_FAIRE = "TODO", "À faire"
    EN_COURS = "IN_PROGRESS", "En cours"
    TERMINEE = "COMPLETED", "Terminée"


class PrioriteTache(models.TextChoices):
    FAIBLE = "LOW", "Faible"
    MOYENNE = "MEDIUM", "Moyenne"
    ELEVEE = "HIGH", "Élevée"


# ==========================================================
# MEMBRE
# ==========================================================

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# ==========================================================
# EQUIPE
# ==========================================================

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    members = models.ManyToManyField(
        Member,
        related_name="teams",
        blank=True
    )

    def __str__(self):
        return self.name


# ==========================================================
# PROJET
# ==========================================================

class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatutProjet.choices,
        default=StatutProjet.ACTIF
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    def __str__(self):
        return self.title


# ==========================================================
# TACHE
# ==========================================================

class Task(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatutTache.choices,
        default=StatutTache.A_FAIRE
    )

    priority = models.CharField(
        max_length=20,
        choices=PrioriteTache.choices,
        default=PrioriteTache.MOYENNE
    )

    due_date = models.DateField()

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    assignee = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks"
    )

    def __str__(self):
        return self.title


# ==========================================================
# COMMENTAIRE
# ==========================================================

class Comment(models.Model):

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def __str__(self):
        return f"Commentaire de {self.author.name}"