from django.urls import path
from . import views

urlpatterns = [
    # Full path will be: /api/send-email/
    path('send-email/', views.send_email, name='send_email'),
    path('test-send-email/', views.email_form_page, name='test_email_page'),
]