from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from aluno.models import Aluno
from aluno.serializers import AlunoSerializer
from rest_framework.response import Response
from rest_framework.status import status


class AlunoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome','=idade']
    queryset = Aluno.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer

class AlunoList(views.APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)