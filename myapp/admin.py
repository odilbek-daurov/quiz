from django.contrib import admin

from .models import Topic, Answer, Questions, Result



@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    model = Topic
    fields = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
     

class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']
    

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fielsd = ['name', 'topic']
    list_displey = ['name', 'topic']
    inlines = [AnswerInline]


admin.site.register(Answer)

admin.site.register(Result)
