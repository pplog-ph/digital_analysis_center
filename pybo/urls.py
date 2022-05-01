from django.urls import path
from .views import base_views, question_views, answer_views, subscribe_views, update_views, requestwork_views

app_name = 'pybo'


urlpatterns = [
    # base_views.py
    path('report/list_table/',
         base_views.index, name='index'),   #list 페이지:table
    path('report/list_visual/',
         update_views.report_update, name='report_update'),   #list 페이지:visual
    path('report/<int:question_id>/',
         base_views.detail, name='detail'),     #report detail 페이지

    # question_views.py
    path('report/create/',
         question_views.question_create, name='question_create'),   #report 생성 페이지
    path('report/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),   #report 수정 페이지
    path('report/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),   #report 삭제 페이지
    path('report/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),   #report 추천 페이지


    # answer_views.py
    path('answer/create/<int:question_id>/',      #
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),


    # subscribe_views.py
    path('report/subscribe/<int:question_id>/',
         subscribe_views.subscribe_report, name='question_subscribe'),    #report 구독 신청 페이지

    # requestwork_views.py
    path('request/create/',
         requestwork_views.request_work, name='requestwork_create'),        #업무 요청 페이지


]

