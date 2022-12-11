from django.shortcuts import render

from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Replacer
from .serializer import ReplaceSerializer
import replace


class ReplaceView(APIView):

    @extend_schema(request=ReplaceSerializer, responses=ReplaceSerializer)

    def get(self, request, my_word):
        replacer = Replacer(my_word, replace.replace(my_word))

        serializer_for_request = ReplaceSerializer(instance=replacer)

        return Response(serializer_for_request.data)
