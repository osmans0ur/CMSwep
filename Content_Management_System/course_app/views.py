from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

from .models import Course, Topic, CustomUser
from .forms import SignUpForm, SignInForm, UserUpdateForm
import requests
from django.utils.decorators import method_decorator
from django.views import View
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'registration/sign_in.html', {'form': form})  # Update the path here
def sign_out(request):
    logout(request)
    return redirect('home')
@login_required
def settings(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})
@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('settings')
    else:
        password_change_form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {
        'password_change_form': password_change_form,
    })
def custom_password_reset(request):
    return PasswordResetView.as_view(
        request,
        template_name='forgot_password.html',
        email_template_name='forgot_password_email.html',
        subject_template_name='forgot_password_subject.txt',
        post_reset_redirect='/course_app/sign_in/',
    )    
def courses_page(request):
    courses = Course.objects.all()
    return render(request, 'course_app/courses_page.html', {'courses': courses})

def topics_page(request, course_id):
    course = Course.objects.get(pk=course_id)
    topics = Topic.objects.filter(course=course)
    return render(request, 'course_app/topics_page.html', {'course': course, 'topics': topics})

def youtube_results_page(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    youtube_api_key = 'AIzaSyCl1AgLuehYUSn3L_gfiGgx5cXwdvODhs4'
    youtube_query = topic.youtube_topic_query

    # Make a request to the YouTube API using the provided query and API key
    # Ensure you have error handling for the API request in your code
    response = requests.get(f'https://www.googleapis.com/youtube/v3/search?q={youtube_query}&key={youtube_api_key}')
    data = response.json()
    videos = data.get('items', [])

    return render(request, 'course_app/youtube_results_page.html', {'topic': topic, 'videos': videos})
