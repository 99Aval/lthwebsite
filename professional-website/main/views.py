from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def ups(request):
    return render(request, 'ups.html')

def contact(request):
    return render(request, 'contact.html')

def footer_contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            subject='Website Contact Form',
            message=f"From: {email}\n\nMessage:\n{message}",
            from_email=None,
            recipient_list=['avalarch61@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent!")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')