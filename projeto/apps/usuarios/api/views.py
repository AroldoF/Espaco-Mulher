from django.contrib.auth.models import User
from apps.usuarios.api.serializers import UserSerializer
from rest_framework import viewsets, generics, filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    ordering_fields = ['id','username',]
    search_fields = ['username',]