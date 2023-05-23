from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Portfolio
from .serializers import Portfolio_detailsSerializer
from user.authenticate import CustomAuthentication

class PortfolioView(APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = Portfolio_detailsSerializer(portfolios, many=True)
        return Response(serializer.data)
    


class PortfolioDetailView(APIView):
    authentication_classes = [CustomAuthentication]
    
    def put(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                portfolio = Portfolio.objects.get(id=id)
            except Portfolio.DoesNotExist:
                return Response({"detail": f"Portfolio {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = Portfolio_detailsSerializer(portfolio,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Unable to amend portfolio due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def delete(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                portfolio = Portfolio.objects.get(id=id)
                portfolio.delete()
            except Portfolio.DoesNotExist:
                return Response({"detail": f"Portfolio {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"detail": "Portfolio deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"Unable to delete portfolio due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self, request, id):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            try:
                portfolio = Portfolio.objects.get(id=id)
            except Portfolio.DoesNotExist:
                return Response({"detail": f"Portfolio {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = Portfolio_detailsSerializer(portfolio)
            return Response(serializer.data)
        
        else:
            return Response({"detail": "Unable to retrieve portfolio due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)

        
    def post(self, request):
        if request.user and request.user.is_authenticated:  # check if user is authenticated
            serializer = Portfolio_detailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Unable to create portfolio due to denied access"}, status=status.HTTP_401_UNAUTHORIZED)    