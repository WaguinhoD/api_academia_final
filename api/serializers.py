from rest_framework import serializers

from .models import Instrutor, Plano, Programa


class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor
        fields = ('nome', 'sobrenome', 'foto', 'descricao')


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ('id', 'image_plano', 'nome_plano', 'valor', 'beneficio1',
                  'beneficio1', 'beneficio2', 'beneficio3', 'beneficio4',
                  'beneficio5')


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ('is', 'image_programa', 'nome_programa', 'descricao')