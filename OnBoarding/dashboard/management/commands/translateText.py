from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Extracts and compiles message files for translations'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.NOTICE('Running makemessages for French...'))
            subprocess.run(['python', 'manage.py', 'makemessages', '-l', 'fr'], check=True)

            self.stdout.write(self.style.NOTICE('Running makemessages for English...'))
            subprocess.run(['python', 'manage.py', 'makemessages', '-l', 'en'], check=True)

            self.stdout.write(self.style.NOTICE('Compiling messages...'))
            subprocess.run(['python', 'manage.py', 'compilemessages'], check=True)

            self.stdout.write(self.style.SUCCESS('Translation files processed successfully.'))

        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))
