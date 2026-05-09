# src/models.py
from patterns import NotificationManager

# Nsiyw nsawbo instance we7da dyal NotificationManager (b7al Singleton hta hya)
notif_manager = NotificationManager()

class Utilisateur:
    """
    Classe katmttel un utilisateur f l'application (Admin wla Membre).
    Katjewb l'exigence dyal Gestion des utilisateurs.
    """
    def __init__(self, id_user, nom, email, role="Membre"):
        self.id = id_user
        self.nom = nom
        self.email = email
        self.role = role # "Administrateur" wla "Membre"

    def recevoir_notification(self, message):
        """Méthode exigée par le pattern Observer pour recevoir les alertes."""
        print(f"🔔 [Notification pour {self.nom}] : {message}")

    def __str__(self):
        return f"{self.nom} ({self.role})"


class Tache:
    """
    Classe katmttel une tâche f l'application.
    Katjewb l'exigence dyal Gestion des tâches.
    """
    def __init__(self, id_tache, titre, description, statut="À faire"):
        self.id = id_tache
        self.titre = titre
        self.description = description
        self.statut = statut # "À faire", "En cours", "Terminée"
        self.responsable = None

    def assigner_a(self, utilisateur):
        """
        Attribuer une tâche à un membre et déclencher une notification (Observer).
        """
        self.responsable = utilisateur
        notif_manager.ajouter_observateur(utilisateur)
        message = f"La tâche '{self.titre}' vous a été assignée."
        notif_manager.notifier_tous(message)

    def changer_statut(self, nouveau_statut):
        """Changer le statut d'une tâche."""
        statuts_valides = ["À faire", "En cours", "Terminée"]
        if nouveau_statut in statuts_valides:
            self.statut = nouveau_statut
            print(f"Statut de la tâche '{self.titre}' changé en : {self.statut}")
        else:
            print("Statut invalide.")


class Projet:
    """
    Classe katmttel un projet li fih des membres w des tâches.
    Katjewb l'exigence dyal Gestion des projets.
    """
    def __init__(self, id_projet, nom, description):
        self.id = id_projet
        self.nom = nom
        self.description = description
        self.membres = []
        self.taches = []

    def ajouter_membre(self, utilisateur):
        """Ajouter un membre dans un projet."""
        if utilisateur not in self.membres:
            self.membres.append(utilisateur)
            print(f"{utilisateur.nom} a été ajouté au projet '{self.nom}'.")

    def ajouter_tache(self, tache):
        """Ajouter une tâche au projet."""
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée au projet '{self.nom}'.")