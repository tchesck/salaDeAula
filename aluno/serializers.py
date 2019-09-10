from rest_framework import serializers
from aluno.models import Aluno
from professor.models import Professor


class ProfessorDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class AlunoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255, required=True)
    idade = serializers.IntegerField()
    email = serializers.EmailField()
    prof_favorito = ProfessorDataSerializer()

    def create(self, validated_data):
        professor_data = validated_data.pop('prof_favorito')
        professor = Professor.objects.get(id=professor_data['id'])
        aluno = Aluno.objects.create(prof_favorito=professor, **validated_data)
        return aluno

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.email = validated_data.get('email')
        professor_data = validated_data('prof_favorito')
        professor = Professor.objects.get(id=professor_data['id'])
        instance.prof_favorito = professor
        instance.save()
        return instance
