from django.contrib import admin

# Question 모델을 관리자에서 보기 위해
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = (
        'subject',
        'create_date',
        'author',
    )
    list_filter = (
        'subject',
    )
admin.site.register(Question, QuestionAdmin)

# Answer 모델을 관리자에서 보기 위해
from .models import Answer
admin.site.register(Answer)


# Subscribe 모델을 관리자에서 보기 위해
from .models import Subscribe
class SubscribeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'name',
        'question',
        'department',
        'google_email',
        'wv_email',
        'create_date',
        'subscribe_state',
    )
    list_filter = (
        'subscribe_state',
        'question',
        'name',
        'google_email',
    )
admin.site.register(Subscribe, SubscribeAdmin)


# RequestWork 모델을 관리자에서 보기 위해
from .models import RequestWork
class RequestWorkAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        'subject',
        'name',
        'department',
        'category_state',
        'content',
        'create_date',
        'progress_state',
        'end_date',
    )
    list_filter = (
        'name',
        'department',
        'category_state',
        'progress_state',
    )
admin.site.register(RequestWork, RequestWorkAdmin)
