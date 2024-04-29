from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题内容', {"fields": ["question_text"]}),
        ("发布时间", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
