from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Collecte les fichiers statiques (comme collectstatic --noinput)."

    def handle(self, *args, **options):
        self.stdout.write("📦 Collecte des fichiers statiques...")
        try:
            call_command("collectstatic", "--noinput", verbosity=1)
            self.stdout.write(self.style.SUCCESS("✅ Fichiers statiques collectés avec succès."))
        except Exception as e:
            raise CommandError(f"❌ Erreur lors de la collecte des fichiers statiques : {e}")
