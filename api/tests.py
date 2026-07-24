from datetime import date

from django.test import TestCase

from .models import (
    Member,
    Team,
    Project,
    StatutProjet,
    StatutTache,
    PrioriteTache,
)
from .serializers import TaskSerializer


# ==========================================================
# TESTS MEMBRE
# ==========================================================

class TestMember(TestCase):

    def test_creation_membre(self):
        """
        Vérifie qu'un membre est créé correctement.
        """

        membre = Member.objects.create(
            name="Sebastien",
            email="sebastienmbiendji@gmail.com"
        )

        self.assertEqual(membre.name, "Sebastien")
        self.assertEqual(
            membre.email,
            "sebastienmbiendji@gmail.com"
        )


# ==========================================================
# TESTS EQUIPE
# ==========================================================

class TestTeam(TestCase):

    def test_creation_equipe(self):
        """
        Vérifie qu'une équipe est créée correctement.
        """

        equipe = Team.objects.create(
            name="Développement"
        )

        self.assertEqual(
            equipe.name,
            "Développement"
        )


# ==========================================================
# TESTS RELATION MEMBRE / EQUIPE
# ==========================================================

class TestRelationEquipe(TestCase):

    def test_ajout_membre_equipe(self):
        """
        Vérifie qu'un membre peut être ajouté à une équipe.
        """

        membre = Member.objects.create(
            name="Sebastien",
            email="sebastienmbiendji@gmail.com"
        )

        equipe = Team.objects.create(
            name="Développement"
        )

        equipe.members.add(membre)

        self.assertIn(
            membre,
            equipe.members.all()
        )


# ==========================================================
# TEST VALIDATION METIER
# ==========================================================

class TestValidationTask(TestCase):

    def test_membre_hors_equipe(self):
        """
        Vérifie qu'un membre ne peut pas être affecté
        à une tâche s'il n'appartient pas à l'équipe.
        """

        # Création d'une équipe
        equipe = Team.objects.create(
            name="Développement"
        )

        # Création d'un projet
        projet = Project.objects.create(
            title="API REST",
            description="Projet Django",
            status=StatutProjet.ACTIF,
            team=equipe
        )

        # Création d'un membre
        membre = Member.objects.create(
            name="Alexandre",
            email="alexandre@gmail.com"
        )

        # Le membre n'est PAS ajouté à l'équipe

        serializer = TaskSerializer(
            data={
                "title": "Créer les modèles",
                "description": "Description de la tâche",
                "status": StatutTache.A_FAIRE,
                "priority": PrioriteTache.ELEVEE,
                "due_date": date.today(),
                "project": projet.id,
                "assignee": membre.id,
            }
        )

        self.assertFalse(serializer.is_valid())

        self.assertIn(
            "Le membre affecté doit appartenir à l'équipe du projet.",
            str(serializer.errors)
        )