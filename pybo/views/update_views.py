from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Count

from ..models import Question

def report_update(request):
    page = request.GET.get('page', '1')   # 페이지
    question_list = Question.objects.annotate(subscribe_count=Count('subscribe')).order_by('-subscribe_count')
    paginator = Paginator(question_list, 20)  # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/report_update.html', context)

