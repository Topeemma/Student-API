from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Student
from . serializers import StudentSerializer
# Create your views here.

def index(request):
    return HttpResponse(''' This is a student API
                    Go to /api to view the list of students
                    
                    ''')
@api_view(['GET'])
def listStudent(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request, pk):
    student = student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response('Studentdeleted successfully')