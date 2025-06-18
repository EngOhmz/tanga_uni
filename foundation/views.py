# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, News, GalleryImage, Leader
from django.contrib import messages  # for success or error alerts
from .forms import ContactForm,  DonationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm
from .models import ContactMessage
from .forms import MemberForm
from django.contrib.auth import logout
# from django.contrib.auth import logout


def custom_logout_view(request):
    logout(request)  # This logs out the user and clears the session
    return redirect('/')  # Redirect to home page after logout

def home(request):
    events = Event.objects.all()[:3]
    news = News.objects.all()[:3]
    return render(request, 'index.html', {'events': events, 'news': news})

def about(request):
    return render(request, 'about.html')


def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})

def events_view(request):
    events = Event.objects.all().order_by('-date')  # Optional: show latest first
    return render(request, 'events.html', {'events': events})


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})


def leadership_team(request):
    leaders = Leader.objects.all()
    return render(request, 'leadership.html', {'leaders': leaders})





def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Welcome to Tanga University Foundation.')
            return redirect('register')
    else:
        form = MemberForm()

    return render(request, 'register.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Welcome to Tanga University Foundation.')
            return redirect('register')  # or 'dashboard' or any other page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MemberForm()
    return render(request, 'register.html', {'form': form})


def login_portal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect based on permission
            if user.is_staff:
                return redirect('/admin/')  # Send staff/admins to admin panel
            else:
                return redirect('admin_dashboard')  # Replace with your actual dashboard view name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login_portal.html')

# def logout_user(request):
#     logout(request)
#     return redirect('login_portal')


def admin_dashboard(request):
    # Ensure only authenticated users can access the dashboard
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to access the dashboard.")
        return redirect('login_portal')
    
    # Get dashboard data
    total_events = Event.objects.count()
    total_news = News.objects.count()
    total_images = GalleryImage.objects.count()
    total_leaders = Leader.objects.count()
    
    # Get recent items
    recent_events = Event.objects.all()[:5]
    recent_news = News.objects.all()[:5]
    
    context = {
        'user': request.user,
        'total_events': total_events,
        'total_news': total_news,
        'total_images': total_images,
        'total_leaders': total_leaders,
        'recent_events': recent_events,
        'recent_news': recent_news,
    }
    
    return render(request, 'admin_dashboard.html', context)


def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your generous donation!")
            return redirect('donate')
        else:
            messages.error(request, "Please correct the errors in the donation form.")
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message to DB
            ContactMessage.objects.create(
                name=f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']}",
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact')  # redirect to avoid form resubmission
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})