from django.urls import path
from .controllers import seller


urlpatterns = [
    path('', seller.SellerView.as_view())
]