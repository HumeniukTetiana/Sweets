from sweets.models import Person
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model  # 🟢 Не забудь імпорт
from django.contrib.auth import authenticate

User = get_user_model()  # Використовуй, якщо Person замінює User модель

@api_view(['POST'])
def register_user(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not all([username, email, password1, password2]):
        return Response({'error': 'Всі поля є обовʼязковими'}, status=400)

    if password1 != password2:
        return Response({'error': 'Паролі не збігаються'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Користувач з таким іменем вже існує'}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Користувач з таким email вже існує'}, status=400)

    # 👤 Створення користувача
    user = User.objects.create_user(username=username, email=email, password=password1)

    # 🔐 Створення токену
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'message': 'Користувача зареєстровано успішно',
        'token': token.key
    }, status=201)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Введіть імʼя користувача та пароль'}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is None:
        return Response({'error': 'Невірні дані для входу'}, status=400)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=200)
