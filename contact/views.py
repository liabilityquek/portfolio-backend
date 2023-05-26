from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SocialMediaLinks
from .serializers import SocialMediaLinksSerializer
from user.authenticate import CustomAuthentication
        
class SocialMediaLinksView(APIView):
    def get(self, request):
        social_links = SocialMediaLinks.objects.all()
        serializer = SocialMediaLinksSerializer(social_links, many=True)
        return Response(serializer.data)
    


class SocialMediaLinksDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    
    def put(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                social_links = SocialMediaLinks.objects.get(id=id)
            except social_links.DoesNotExist:
                return Response({"detail": f"social_links {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = SocialMediaLinksSerializer(social_links,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Unable to amend social_links due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                social_links = SocialMediaLinks.objects.get(id=id)
                social_links.delete()
            except SocialMediaLinks.DoesNotExist:
                return Response({"detail": f"social_links {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"detail": "social_links deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"Unable to delete social_links due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                social_links = SocialMediaLinks.objects.get(id=id)
            except SocialMediaLinks.DoesNotExist:
                return Response({"detail": f"social_links {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = SocialMediaLinksSerializer(social_links)
            return Response(serializer.data)
        
        else:
            return Response({"detail": "Unable to retrieve social_links due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)

        
    def post(self, request):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            serializer = SocialMediaLinksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Unable to create social_links due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)            