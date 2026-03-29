from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import SkillCategory, Project, Education, ContactMessage

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # 1. Save the message to your database (so you never lose it)
            ContactMessage.objects.create(name=name, email=email, message=message)
            
            # 2. Try to send the email notification to your Gmail
            subject = f"New Portfolio Message from {name}"
            email_body = f"You received a new message from your portfolio website.\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            try:
                send_mail(
                    subject,
                    email_body,
                    settings.EMAIL_HOST_USER,  # Sends FROM your authenticated Gmail
                    ['pratham2149@gmail.com'], # Sends TO your Gmail inbox
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                # If the email fails (e.g., wrong App Password), it will show the error on the site
                print(f"EMAIL ERROR: {e}") # This will print in your VS Code terminal
                messages.error(request, "Message saved to database, but email failed to send. Check terminal for error.")
            
            return redirect('home')

    # Fetch dynamic data from the database
    categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all().order_by('-id')
    education = Education.objects.all()

    context = {
        'categories': categories,
        'projects': projects,
        'education': education,
    }
    return render(request, 'portfolio/index.html', context)