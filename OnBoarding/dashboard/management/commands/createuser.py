import getpass
from django.core.management.base import BaseCommand
from dashboard.models import CustomUser


class Command(BaseCommand):
    help = "Create a new user interactively with email and password"

    def handle(self, *args, **kwargs):
        self.stdout.write("Let's create a new user!")
        email = input("Email: ").strip()
        name = input("First name: ").strip()
        lastname = input("Last name: ").strip()

        while True:
            password = getpass.getpass("Password: ")
            password_confirm = getpass.getpass("Confirm Password: ")
            if password != password_confirm:
                self.stderr.write("Passwords do not match. Please try again.")
            else:
                break

        # Ask if superuser
        is_superuser_input = input("Is this user a superuser? (y/N): ").strip().lower()
        is_superuser = is_superuser_input == "y"

        if CustomUser.objects.filter(email=email).exists():
            self.stderr.write(f"User with email '{email}' already exists.")
            return

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            name=name,
            lastname=lastname,
            is_superuser=is_superuser,
            is_staff=is_superuser,  # usually superusers should have staff access
        )
        user.save()
        self.stdout.write(self.style.SUCCESS(f"User '{email}' created successfully."))
