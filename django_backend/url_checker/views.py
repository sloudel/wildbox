from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Url
from .serializers import UrlSerializer


class ListCreateUrlAPIView(ListCreateAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroyUrlAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    permission_classes = [IsAuthenticated]
