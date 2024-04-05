from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FileName
from .sheet_create import create_sheet
from .drive import download
from .writing_data import writing


# Create your views here.

class FileWritingView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        f = FileName.objects.all()
        for i in f:
            i.delete()
        print("MJJJJJJJJJJJJJJJJJ")
        download()
        create_sheet()
        file_name = []
        key = []
        word = []
        for name in f:
            file_name.append(name.name)
            key.append(name.key)
            word.append(name.word)
        print(file_name, key, word)
        writing(file_name, key, word)
        return Response({"message": "kkk"})

