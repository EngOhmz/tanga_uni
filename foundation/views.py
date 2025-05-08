# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, News, GalleryImage, Leader
from django.contrib import messages  # for success or error alerts
from .forms import ContactForm, RegisterForm, DonationForm, MemberRegistrationForm
from django.contrib.auth import login, authenticate


def index(request):
    events = Event.objects.all()[:3]
    news = News.objects.all()[:3]
    return render(request, 'index.html', {'events': events, 'news': news})

def about(request):
    return render(request, 'about.html')


def news_list(request):
    articles = News.objects.all()
    return render(request, 'news.html', {'articles': articles})

def events_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})


def leadership_team(request):
    leaders = Leader.objects.all()
    return render(request, 'team.html', {'leaders': leaders})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # You can extract data like this:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Optional: Save to DB or send email (not shown here)
            # Example (if you have a model): Contact.objects.create(...)

            # Show success message
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact')  # Name in urls.py
        else:
            messages.error(request, "Oops! Something went wrong. Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




       
