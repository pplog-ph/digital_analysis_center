from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db import IntegrityError

from ..forms import SubscribeForm
from ..models import Question, Subscribe


def subscribe_report(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscribe = form.save(commit=False)
            subscribe.question = question
            subscribe.create_date = timezone.now()
            try:
                subscribe.save()
                return redirect('pybo:report_update')
            except IntegrityError as e:
                error_message = '해당 리포트는 이미 구독 중입니다. 다른 리포트를 구독해주세요'
                #return redirect('pybo:detail', question_id=question.id)
                return render(request, 'pybo/subscribe_form.html', context={'form': form, 'e': error_message})
    else:
        form = SubscribeForm()
    context = {'form': form}
    return render(request, 'pybo/subscribe_form.html', context)