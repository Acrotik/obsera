from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Create a superuser with preset email and password'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = 'info@consultjpt.info'
        password = 'Logenda12$'
        try:
            if not User.objects.filter(email=email).exists():
                User.objects.create_superuser(username='admin', email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Superuser {email} created successfully!'))
            else:
                self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists.'))

            call_command('create_default_db_group')
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))
