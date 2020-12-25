from django.contrib import admin
from .models import Question,Choice
# Register your models here.

admin.site.site_header= 'Poll Voting Admin'
admin.site.site_title= 'Poll Admin Area'
admin.site.index_title='welcome to the poll admin'

class ChoiceInLine(admin.TabularInline):
    model=Choice
    choiceFields=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[('Question', {'fields': ['question_text']}),
                ('date-published',{'fields':['pub_date']}),]
    inlines=[ChoiceInLine]
    

admin.site.register(Question,QuestionAdmin)