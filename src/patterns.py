# src/patterns.py

class DatabaseConnection:
    """
    Pattern Singleton : Kaydmen anana 3dna instance we7da dyal base de données f l'application kamla.
    Kansst3mlouh bach manb9awch n7ellou plusieurs connexions w nt9lou systeme.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("[Singleton] Création de la connexion à la base de données...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance


class NotificationManager:
    """
    Pattern Observer : Had la classe katsiyer les notifications.
    Mnin katw9e3 chi 7aja (b7al assignation dyal tâche), katsift notification lga3 les observateurs (Membres).
    """
    def __init__(self):
        self._observateurs = []

    def ajouter_observateur(self, observateur):
        """Ajoute un utilisateur à la liste des observateurs."""
        if observateur not in self._observateurs:
            self._observateurs.append(observateur)

    def notifier_tous(self, message):
        """Envoie un message à tous les observateurs enregistrés."""
        for obs in self._observateurs:
            obs.recevoir_notification(message)


class TacheFactory:
    """
    Pattern Factory : Kaytkelf b la création dyal les objets 'Tache'.
    Kayshel 3lina l'instanciation w kaydmen ano n طبقo le principe KISS w SOLID.
    """
    @staticmethod
    def creer_tache(id_tache, titre, description):
        """
        Créer une nouvelle tâche m3a statut par défaut 'À faire'.
        (Kan importiw Tache mn models hna bach manty7ouch f l'import circulaire).
        """
        from models import Tache
        return Tache(id_tache, titre, description, "À faire")