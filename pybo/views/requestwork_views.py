from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import RequestWorkFrom
from django.contrib import messages

def request_work(request):
    if request.method == 'POST':
        form = RequestWorkFrom(request.POST, request.FILES)
        if form.is_valid():
            requestwork = form.save(commit=False)
            requestwork.create_date = timezone.now()
            requestwork.end_date = timezone.now()
            requestwork.save()
            messages.info(request, '업무요청이 완료되었습니다. 내용 확인 후 사내 메일로 피드백 드릴께요:)')
            return redirect('pybo:report_update')

    else:
        form = RequestWorkFrom()
    context = {'form': form}
    return render(request, 'pybo/requestwork_form.html', context)