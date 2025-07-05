import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Runs the Django development server with a custom IP and port.'

    def handle(self, *args, **options):
        ip_address = '74.208.248.151'
        port = '80'

        try:
            self.stdout.write(self.style.NOTICE(f'Starting server on {ip_address}:{port}...'))

            # Run the Django server with the specified IP and port
            subprocess.run(['python', 'manage.py', 'runserver', f'{ip_address}:{port}'], check=True)

            self.stdout.write(self.style.SUCCESS(f'Server started successfully on {ip_address}:{port}.'))

        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f'An error occurred while starting the server: {e}'))
