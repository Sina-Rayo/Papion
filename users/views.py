from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .serializers import SignupSerializer, LoginSerializer

from recepie.models import Account

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            ac = serializer.validated_data['username']
            account = Account(username=ac , been_liked=0)
            account.save()
            serializer.save()

            return Response({'message': 'User created successfully!'}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful!'}, status=200)
            return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
