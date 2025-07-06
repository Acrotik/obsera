from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    help = "Démarre le service Nginx via systemd."

    def handle(self, *args, **options):
        try:
            self.stdout.write("🚀 Démarrage de Nginx...")
            subprocess.check_call(["sudo", "systemctl", "start", "nginx"])
            self.stdout.write(self.style.SUCCESS("✅ Nginx démarré avec succès."))
        except subprocess.CalledProcessError as e:
            raise CommandError(f"❌ Échec du démarrage de Nginx : {e}")
