from django.urls import path
from . import views

urlpatterns = [
    # Full path will be: /api/send-email/
    path('send-email/', views.send_email, name='send_email'),
    path('start/', views.start_page, name='start'),
    path('test-send-email/', views.email_form_page, name='test_email_page'),
    path('play/mbot/', views.mbot_tutorial, name='mbot_tutorial'),
    path('play/arduino/', views.arduino_tutorial, name='arduino_tutorial'),
    path('play/raspberry/', views.raspberry_tutorial, name='raspberry_tutorial'),
    path('play/microbit/', views.microbit_tutorial, name='microbit_tutorial'),
    path('play/iot/', views.iot_tutorial, name='iot_tutorial'),
    path('play/ia/', views.ia_tutorial, name='ia_tutorial'),
    path('play/python/', views.python_tutorial, name='python_tutorial'),
    path('play/javascript/', views.javascript_tutorial, name='javascript_tutorial'),
    path('play/scratch/', views.scratch_tutorial, name='scratch_tutorial'),
    path('play/tutorials/', views.tutorials_hub, name='tutorials_hub'),
    path('play/quiz/', views.quiz_hub, name='quiz_hub'),
    path('play/games/', views.game_hub, name='game_hub'),
    path('play/robotics/', views.robotic_hub, name='robotic_hub'),
    path('coaching/', views.coaching_page, name='coaching_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('courses/', views.courses_page, name='courses_page'),
    path('play/playandlearn/', views.playandlearn_page, name='playandlearn_page'),
]
