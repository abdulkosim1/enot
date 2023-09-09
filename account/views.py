from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordSerializer,ForgotPasswordCompleteSerializer, ProfileSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from account.permissions import IsUser, IsCompany
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated   
from rest_framework.generics import UpdateAPIView

class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class RegisterAPIView(APIView): # Пост запрос на регистрацию
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались. Вам отправлено письмо с активацией', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Успешно', status=200)
        except User.DoesNotExist:
            return Response('Link expired', status=400)

class ForgotPasswordAPIView(APIView): # Пост запрос на сброс пароля
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_reset_password_code()
        return Response('вам отправлено письмо для восстановления пароля')

class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен')

class EditProfileAPIView(generics.RetrieveUpdateAPIView): # Put & Patch на изменение данных профиля
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.queryset.get(id=self.request.user.id)

class GetProfile(generics.ListAPIView): # Просмотр профиля (себя)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# class GetExecutants(generics.ListAPIView): # Полуение всех работников, если я покупатель
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated, IsCompany]
#     queryset = User.objects.filter(is_executant=True)

# class GetBuyers(generics.ListAPIView): # Полуение всех клиентов, если я работник
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated, IsExecutant]
#     queryset = User.objects.filter(is_buyer=True)
