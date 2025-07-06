from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Génère et compile les fichiers de traduction (.po et .mo) pour en et fr."

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.NOTICE("🔍 Génération des fichiers .po..."))
            call_command("makemessages", "-l", "en")
            call_command("makemessages", "-l", "fr")

            self.stdout.write(self.style.SUCCESS("✅ Fichiers .po générés."))

            self.stdout.write(self.style.NOTICE("🛠 Compilation des fichiers .mo..."))
            call_command("compilemessages")

            self.stdout.write(self.style.SUCCESS("✅ Compilation terminée avec succès."))

        except Exception as e:
            raise CommandError(f"❌ Erreur durant le processus de traduction : {e}")
