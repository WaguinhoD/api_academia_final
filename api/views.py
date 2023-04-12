from api.models import Instrutor, Plano, Programa
from api.serializers import (InstrutorSerializer, PlanoSerializer,
                             ProgramaSerializer)
from rest_framework import viewsets


# Lista de instrutores Criar exibição de API
class instrutorViewSet(viewsets.ModelViewSet):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer
    lookup_field = 'slug_name'


class planosViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer
    lookup_field = 'id'


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    lookup_field = 'id'
