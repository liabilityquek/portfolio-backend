from django.urls import path
from .views import PortfolioView, PortfolioDetailView

urlpatterns = [
    path('portfolios/', PortfolioView.as_view(), name='portfolios'),
    path('portfolios/<int:id>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('portfolios/create/', PortfolioDetailView.as_view(), name='portfolio_detail'),
]
