from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    days_left = serializers.SerializerMethodField()  # فیلد محاسباتی برای روزهای باقی‌مانده

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'created_at', 'updated_at', 'days_left']
        read_only_fields = ['created_at', 'updated_at']  # این فیلدها فقط خواندنی هستند

    def get_days_left(self, obj):
        # محاسبه تعداد روزهای باقی‌مانده
        remaining_days = (obj.due_date - datetime.now()).days
        return remaining_days

    def validate_due_date(self, value):
        # اعتبارسنجی برای تاریخ due_date
        if value < datetime.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
