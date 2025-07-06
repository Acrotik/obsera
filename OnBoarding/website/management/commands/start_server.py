from django.core.management.base import BaseCommand
import subprocess
import os


class Command(BaseCommand):
    help = "Démarre Gunicorn pour la production (avec socket UNIX)."

    def handle(self, *args, **options):
        socket_path = "/var/www/OnBoarding/onboarding.sock"
        workers = "3"
        module = "onboarding.wsgi:application"

        gunicorn_cmd = [
            "gunicorn",
            "--workers", workers,
            "--bind", f"unix:{socket_path}",
            module
        ]

        self.stdout.write(self.style.SUCCESS(f"Lancement de Gunicorn sur {socket_path} avec {workers} workers..."))
        subprocess.call(gunicorn_cmd, env=os.environ.copy())
