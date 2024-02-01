from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

from .views import sign_up, sign_in, sign_out, home, settings, change_password, custom_password_reset


urlpatterns = [
    path('courses/', views.courses_page, name='courses_page'),
    path('topics/<int:course_id>/', views.topics_page, name='topics_page'),
    path('youtube_results/<int:topic_id>/', views.youtube_results_page, name='youtube_results_page'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication views,
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='logout'),
    path('settings/', settings, name='settings'),
    path('change_password/', change_password, name='change_password'),
    path('forgot_password/', custom_password_reset, name='forgot_password'),


    path('home/', home, name='home'),

]
