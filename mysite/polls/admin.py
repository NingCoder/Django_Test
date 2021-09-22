# from django.contrib import admin
# from .models import Question,Choice
# # Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     #增加表项目
#     # fields = ['pub_date', 'question_text']
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question,QuestionAdmin)
# # admin.site.register(Question)
# admin.site.register(Choice)
from django.contrib import admin
from .models import Choice, Question

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice#choice的三个选项
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)