from django import forms
from pybo.models import Question, Answer, Subscribe, RequestWork

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  #사용할 모델
        fields = ['subject', 'content', 'mainphoto', 'sub_photo_1', 'sub_photo_2', 'thumbnail_img', 'content_summary',]  #QuestionForm에서 사용할 Question 모델의 속성

        labels = {
            'subject': '제목',
            'content': '내용',
            'mainphoto': '미리보기이미지1',
            'sub_photo_1': '미리보기이미지2',
            'sub_photo_2': '미리보기이미지3',
            'thumbnail_img': '썸네일이미지',
            'content_summary': '리포트요약소개',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'department', 'google_email', 'wv_email']
        labels = {
            'name': '이름',
            'department': '부서',
            'google_email': '구글메일',
            'wv_email': '월드비전메일',
        }


class RequestWorkFrom(forms.ModelForm):
    class Meta:
        model = RequestWork
        fields = ['name', 'department', 'category_state', 'subject', 'content' ]
        labels = {
            'name': '이름',
            'department': '부서',
            'category_state': '분류',
            'subject': '제목',
            'content': '분석업무요청내용',
        }

