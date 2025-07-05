from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm  # Assuming the form is in forms.py


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']
            services = form.cleaned_data['services']

            # Prepare the subject and body for the email
            subject = f"New contact form submission from {username}"

            # Start constructing the email body
            body = (
                f"Name: {username}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Company: {company}\n\n"
                f"Message:\n{message}\n\n"
                f"Interested in services: {', '.join(services)}\n\n"
            )

            # Include details of the selected services (if any)
            for service in services:
                service_detail_field = f"details_{service}"
                service_detail = request.POST.get(service_detail_field)
                if service_detail:
                    body += f"Details for {service}: {service_detail}\n\n"

            try:
                # Send the email
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['info@obsera.ca'],
                    fail_silently=False,
                )
                # If email is sent successfully, redirect to success page
                messages.success(request, "Your message has been sent successfully!")
                return redirect('success')  # Redirect to success page
            except Exception as e:
                print(f"Error sending email: {e}")
                # If email fails, redirect to deny page
                messages.error(request, "Failed to send your message. Please try again later.")
                return redirect('deny')  # Redirect to deny page

        else:
            # If form is not valid, stay on the same page and show errors
            messages.error(request, "There were errors in the form. Please check your input.")
            return redirect('index')  # Stay on the index page and show errors
    else:
        # For GET requests, just render the form page
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html')  # Simple success page


def deny(request):
    return render(request, 'deny.html')  # Simple deny page
