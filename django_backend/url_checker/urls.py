from django.urls import path
from .views import ListCreateUrlAPIView, RetrieveUpdateDestroyUrlAPIView

urlpatterns = [
    path('', ListCreateUrlAPIView.as_view(), name='get_post_url'),
    path('<int:pk>', RetrieveUpdateDestroyUrlAPIView.as_view(), name='get_delete_update_url'),
]
