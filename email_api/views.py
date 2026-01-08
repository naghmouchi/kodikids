# email_app/views.py

import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index_page(request):
    """
    Renders the site index / landing page with navigation.
    """
    return render(request, 'email_api/index.html')

def start_page(request):
    """
    Renders the site index / landing page with navigation.
    """
    return render(request, 'email_api/commencer.html')

def email_form_page(request):
    """
    Renders the HTML page that contains the JS test form to call the send-email API.
    Accessible at /send/email/
    """
    return render(request, 'email_api/send_email.html')
# This decorator is crucial for handling POST requests without Django's CSRF token
@csrf_exempt
@require_POST
def send_email(request):
    """
    Handles a POST request to send an email.
    Expects recipient, subject, and message in the request body.
    """
    try:
        # Step 1: Parse the JSON payload
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Format JSON invalide.'}, status=400)
            
        recipient = data.get('recipient')
        subject = data.get('subject')
        message = data.get('message')
        
        # --- Strict Input Validation ---
        
        # 1. Check for presence of all fields
        if not all([recipient, subject, message]):
            return JsonResponse({'success': False, 'message': 'Champs requis manquants (recipient, subject, message).'}, status=400)
            
        # 2. VÉRIFICATION CRITIQUE DU TYPE: Assurez-vous que le destinataire est une chaîne de caractères non vide.
        if not isinstance(recipient, str) or not recipient.strip():
            logger.error(f"Recipient validation failed. Type: {type(recipient)}, Value: {recipient}")
            return JsonResponse({'success': False, 'message': 'Le destinataire doit être une chaîne de caractères non vide.'}, status=400)

        # Nettoyer l'espace blanc (trailing/leading)
        recipient = recipient.strip()
        
        # 3. Check format
        if '@' not in recipient:
             return JsonResponse({'success': False, 'message': 'Format d\'e-mail destinataire invalide (manque @).'}, status=400)
        
        # --- Send Email ---
        
        # Django's built-in mail function. The 'to' argument MUST be a list/tuple.
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL, # Expéditeur
            [recipient],                 # Liste de destinataires
            fail_silently=False,
        )

        logger.info(f"Successfully sent email to: {recipient}")
        return JsonResponse({'success': True, 'message': 'E-mail envoyé avec succès !'})

    except Exception as e:
        logger.error(f"ERREUR FATALE DU SERVEUR dans send_email_api: {e}", exc_info=True)
        # Le 500 erreur indique maintenant le type d'erreur pour faciliter le débogage
        return JsonResponse({'success': False, 'message': f'Échec de l\'envoi de l\'e-mail. Erreur interne du serveur : {type(e).__name__}'}, status=500)
    
def mbot_tutorial(request):
    return render(request, 'email_api/mbot_tutorial.html')

def arduino_tutorial(request):
    return render(request, 'email_api/arduino_tutoriel.html')

def raspberry_tutorial(request):
    return render(request, 'email_api/raspberry_tutoriel.html')

def microbit_tutorial(request):
    return render(request, 'email_api/microbit_tutoriel.html')

def iot_tutorial(request):
    return render(request, 'email_api/iot_tutoriel.html')

def ia_tutorial(request):
    return render(request, 'email_api/ia_tutoriel.html')

def python_tutorial(request):
    return render(request, 'email_api/python_tutoriel.html')

def javascript_tutorial(request):
    return render(request, 'email_api/javascript_tutoriel.html')

def scratch_tutorial(request):
    return render(request, 'email_api/scratch_tutoriel.html')

def quiz_hub(request):
    return render(request, 'email_api/quiz_hub.html')

def tutorials_hub(request):
    return render(request, 'email_api/tutorials_hub.html')

def coaching_page(request):
    return render(request, 'email_api/coaching.html')

def contact_page(request):
    return render(request, 'email_api/contact.html')

def courses_page(request):
    return render(request, 'email_api/courses.html')

def playandlearn_page(request):
    return render(request, 'email_api/playandlearn.html')

def game_hub(request):
    return render(request, 'email_api/game_hub.html')

def robotic_hub(request):
    return render(request, 'email_api/robotic_hub.html')

def math_code_niv1(request):
    return render(request, 'email_api/math_code_niv1.html')

def math_code_niv2(request):
    return render(request, 'email_api/math_code_niv2.html')

def math_code_niv3(request):
    return render(request, 'email_api/math_code_niv3.html')

def math_code_niv4(request):
    return render(request, 'email_api/math_code_niv4.html')

def deviner_lettre(request):
    return render(request, 'email_api/deviner_lettre.html')

def block_roblox(request):
    return render(request, 'email_api/block_roblox.html')

def python_quiz(request):
    return render(request, 'email_api/python_quiz.html')

def ia_quiz(request):
    return render(request, 'email_api/ia_quiz.html')

def javascript_quiz(request):
    return render(request, 'email_api/javascript_quiz.html')

def scratch_quiz(request):
    return render(request, 'email_api/scratch_quiz.html')

def arduino_quiz(request):
    return render(request, 'email_api/arduino_quiz.html')

def iot_quiz(request):
    return render(request, 'email_api/iot_quiz.html')

def raspberry_pi_quiz(request):
    return render(request, 'email_api/raspberry_pi_quiz.html')

def mbot_quiz(request):
    return render(request, 'email_api/mbot_quiz.html')

def web_basics_quiz(request):
    return render(request, 'email_api/web_basics_quiz.html')

def microbit_quiz(request):
    return render(request, 'email_api/microbit_quiz.html')

def roblox_tutorial(request):
    return render(request, 'email_api/roblox_tutoriel.html')

def roblox_quiz(request):
    return render(request, 'email_api/roblox_quiz.html')

def arduino_simulator(request):
    return render(request, 'email_api/arduino_sim_v1.html')

def soccer_block(request):
    return render(request, 'email_api/soccer_block.html')

def tetris_game(request):
    return render(request, 'email_api/tetris_game.html')

def arduino_simulator_v2(request):
    return render(request, 'email_api/arduino_sim_v2.html')

def arduino_simulator_v3(request):
    return render(request, 'email_api/arduino_sim_v3.html')

def arduino_simulator_v4(request):
    return render(request, 'email_api/arduino_sim_v4.html')

def arduino_simulator_v5(request):
    return render(request, 'email_api/arduino_sim_v5.html')

def microbit_simulator(request):
    return render(request, 'email_api/microbit_sim.html')

def raspberry_simulator(request):
    return render(request, 'email_api/raspberry_sim.html')

def mbot_simulator(request):
    return render(request, 'email_api/mbot_sim.html')

def iot_simulator(request):
    return render(request, 'email_api/iot_sim.html')

def ia_robot_simulator(request):
    return render(request, 'email_api/ia_robot_sim.html')

def robotic_arm_simulator(request):
    return render(request, 'email_api/robotic_arm_sim.html')

def blockly_robot_simulator(request):
    return render(request, 'email_api/blockly_robot_sim.html')
