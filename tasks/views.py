from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # بازیابی تمام تسک‌ها
    serializer_class = TaskSerializer  # استفاده از سریالایزر برای تبدیل داده‌ها
