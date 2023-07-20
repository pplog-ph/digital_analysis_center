from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Question, Subscribe

def index(request):
    page = request.GET.get('page', '1')   # 페이지
    #question_list = Question.objects.order_by('-create_date')
    question_list = Question.objects.order_by('create_date')
    paginator = Paginator(question_list, 20)  # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    page = request.GET.get('page', '1')    #페이지
    subscribe_list = Subscribe.objects.order_by('-name')
    paginator = Paginator(subscribe_list, 20)  # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question': question, 'subscribe_list': page_obj}
    return render(request, 'pybo/question_detail.html', context)


