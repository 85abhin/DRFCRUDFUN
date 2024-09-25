from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Studentserializer
from .models import Student


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            stu = Student.objects.get(id = pk)
            s = Studentserializer(stu)
            return Response(s.data)
        
        stu = Student.objects.all()
        s= Studentserializer(stu,many=True)
        print(s)
        return Response(s.data)
    
        
    if request.method == 'POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created..'},status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT':
            stu = Student.objects.get(id = pk)
            serializer = Studentserializer(stu,request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({'msg':'Complete Data Updated'})
            return Response(serializer.data,status =status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
         stu = Student.objects.get(id = pk)
         serializer = Studentserializer(stu,data = request.data, partial =True)
         if serializer.is_valid():
              serializer.save()
              return Response({'msg':'data is updated'},status=status.HTTP_201_CREATED)
         return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        if pk:
            stu = Student.objects.get(id = pk)
            stu.delete()
            return Response({'msg':'data is deleted..'})
        return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)



        


    