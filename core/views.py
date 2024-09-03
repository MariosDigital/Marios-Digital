from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import os

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def contacto(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Construir el mensaje de correo electrónico
        email_subject = "New Contact Form Submission"
        email_body = render_to_string('core/email.html', {
            'fullname': fullname,
            'email': email,
            'phone': phone,
            'message': message,
        })

        # Dirección de correo del remitente y destinatario desde variables de entorno
        from_email = os.getenv('DEFAULT_FROM_EMAIL', 'no-reply@tu-dominio.com')
        recipient_list = [os.getenv('RECIPIENT_EMAIL', 'admin@tu-dominio.com')]

        email_message = EmailMessage(
            email_subject,
            email_body,
            from_email,
            recipient_list,
        )

        try:
            email_message.send()
            messages.success(request, "Tu mensaje se ha enviado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al enviar el mensaje: {str(e)}")

        return redirect('contacto')

def services(request):
    return render(request, "core/services.html")
