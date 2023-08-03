from rest_framework import viewsets

from .serializers import PassSerializer
from .models import Pass


class Passviewset(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
