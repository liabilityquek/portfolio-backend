from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from functools import wraps
import jwt
from django.http import JsonResponse

# @ensure_csrf_cookie
# def get_csrf(request):
#     token = get_token(request)
#     return JsonResponse({'token': token})

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }
        
# class LoginView(APIView):
#     def post(self, request):
#         # print("LoginView method called")
#         data = request.data
#         response = Response()        
#         email = data.get('email', None)
#         password = data.get('password', None)
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             if user.is_active:
#                 data = get_tokens_for_user(user)
#                 response.set_cookie(
#                     key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
#                     value = data["access"],
#                     expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
#                     secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
#                     httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
#                     samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
#                 )
#                 csrf.get_token(request)
#                 response.data = {"Success" : "Login successfully","data":data}
#                 return response
#             else:
#                 return Response({"Invalid Credentials!"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"Invalid Credentials!"}, status=status.HTTP_404_NOT_FOUND)

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     # success_url = reverse_lazy('users-home')        
    
@api_view(['POST'])
def Auth0UserView(request):
    user_data = request.data
    email = user_data.get('email', None)
    
    if not email:
        return Response({"Invalid Data!"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserData.objects.get(email=email)
    except UserData.DoesNotExist:
        user = UserData.objects.create_user(
            name=user_data.get('name', ''),
            email=email,
        )

    # Serialize and return user data
    serializer = UserSerializer(user)
    return Response(serializer.data)