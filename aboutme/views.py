from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import Profile_detailsSerializer
from user.authenticate import CustomAuthentication

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        serializer = Profile_detailsSerializer(profile, many=True)
        return Response(serializer.data)
    


class ProfileDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    
    def put(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                profile = Profile.objects.get(id=id)
            except profile.DoesNotExist:
                return Response({"detail": f"profile {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = Profile_detailsSerializer(profile,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Unable to amend Profile due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                profile = Profile.objects.get(id=id)
                profile.delete()
            except Profile.DoesNotExist:
                return Response({"detail": f"Profile {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"detail": "Profile deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"Unable to delete Profile due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                profile = Profile.objects.get(id=id)
            except Profile.DoesNotExist:
                return Response({"detail": f"Profile {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = Profile_detailsSerializer(profile)
            return Response(serializer.data)
        
        else:
            return Response({"detail": "Unable to retrieve Profile due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)

        
    def post(self, request):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            serializer = Profile_detailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Unable to create Profile due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)    