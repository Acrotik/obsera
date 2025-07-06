from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "Affiche le status des services Gunicorn et Nginx."

    def handle(self, *args, **options):
        services = ["gunicorn", "nginx"]

        for service in services:
            self.stdout.write(f"🔍 Vérification du status de {service}...")
            try:
                output = subprocess.check_output(["sudo", "systemctl", "is-active", service])
                status = output.decode().strip()
                if status == "active":
                    self.stdout.write(self.style.SUCCESS(f"✅ {service} est actif."))
                else:
                    self.stdout.write(self.style.WARNING(f"⛔ {service} est inactif ({status})."))
            except subprocess.CalledProcessError:
                self.stdout.write(self.style.ERROR(f"❌ Impossible de vérifier le service {service} (non trouvé ou erreur)."))
