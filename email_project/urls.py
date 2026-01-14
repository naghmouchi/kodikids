"""
URL configuration for email_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from email_api import views as email_api_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Map all URLs from the 'email_app' to the 'api/' path
    path('api/', include('email_api.urls')),
        # Index page
    path('', email_api_views.index_page, name='index'),

    # Contact redirected to the send-email template
    path('contact/', RedirectView.as_view(url='/api/test-send-email/', permanent=False), name='contact'),

    # Expose the test HTML page at /send/email/
    path('send/email/', email_api_views.email_form_page, name='send_email_page'),

]

# Gestionnaire pour la page 404 (Page non trouvée)
handler404 = email_api_views.custom_page_not_found