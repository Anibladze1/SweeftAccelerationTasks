from django.urls import path
from .views import CreateShortURLAPIView, RetrieveFullURLAPIView, ListAllURLsAPIView, ShortURLDetailAPIView

urlpatterns = [
    path('create/', CreateShortURLAPIView.as_view(), name='create_short_url'),
    path('list/', ListAllURLsAPIView.as_view(), name='list_all_urls'),
    path('list/<str:short_url>/', ShortURLDetailAPIView.as_view(), name='short_url_detail'),
    path('<str:short_url>/', RetrieveFullURLAPIView.as_view(), name='get_full_url'),
]
