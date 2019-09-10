from rest_framework import serializers
from aluno.serializers import AlunoSerializer
from professor.models import Professor


class ProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255, required=True)
    idade = serializers.IntegerField()
    aluno = AlunosSerializer(many=True, read_oly=True, required=False)

    def create(self, validated_data):
        professor = Professor.objects.create(**validated_data)
        return professor

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.save()
        return instance