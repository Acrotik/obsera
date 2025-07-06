from django.core.management.base import BaseCommand, CommandError
import subprocess

class Command(BaseCommand):
    help = "Redémarre les services systemd Gunicorn et Nginx."

    def handle(self, *args, **options):
        services = ["gunicorn", "nginx"]

        for service in services:
            try:
                self.stdout.write(f"🔄 Redémarrage de {service}...")
                subprocess.check_call(["sudo", "systemctl", "restart", service])
                self.stdout.write(self.style.SUCCESS(f"✅ {service} redémarré avec succès."))
            except subprocess.CalledProcessError as e:
                raise CommandError(f"❌ Échec du redémarrage de {service}: {e}")
