

# # Create your views here.
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Message

# def chatbot_view(request):
#     messages = Message.objects.all().order_by('timestamp')
#     return render(request, 'chatbot/chat.html', {'messages': messages})

# def get_bot_response(user_message):
#     # Replace this with real NLP or chatbot logic
#     return f"You said: {user_message}"

# def chat_api(request):
#     if request.method == 'POST':
#         user_text = request.POST.get('message')

#         # Save user message
#         user_msg = Message.objects.create(sender='user', text=user_text)

#         # Get bot response
#         bot_text = get_bot_response(user_text)
#         bot_msg = Message.objects.create(sender='bot', text=bot_text)

#         return JsonResponse({'message': bot_text})

from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

# Basic Q&A dictionary
QA = {
    "what is your name": "I am a Django Chatbot.",
    "how are you": "I'm just code, but thanks for asking!",
    "what is django": "Django is a high-level Python web framework.",
    "hello": "Hi there! How can I help you?",
}

def chatbot_view(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chatbot/chat.html', {'messages': messages})

def get_bot_response(user_message):
    message = user_message.strip().lower()
    return QA.get(message, "Sorry, I don't understand that yet.")

def chat_api(request):
    if request.method == 'POST':
        user_text = request.POST.get('message')
        Message.objects.create(sender='user', text=user_text)

        bot_text = get_bot_response(user_text)
        Message.objects.create(sender='bot', text=bot_text)

        return JsonResponse({'message': bot_text})
