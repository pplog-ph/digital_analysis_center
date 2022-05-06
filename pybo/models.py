from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True) # 게시글 Post에 이미지 추가
    sub_photo_1 = models.ImageField(blank=True, null=True)
    sub_photo_2 = models.ImageField(blank=True, null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')    # 추천인 추가
    thumbnail_img = models.ImageField(blank=True, null=True)
    content_summary = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Subscribe(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    google_email = models.EmailField(max_length=50, validators = [validate_email])
    wv_email = models.EmailField(max_length=50, validators = [validate_email])
    create_date = models.DateTimeField()
    subscribe_choices = (
        ('application', '구독신청(처리중)'),
        ('completed', '구독중'),
    )
    subscribe_state = models.CharField(max_length=50, choices=subscribe_choices, default=subscribe_choices[0][0])


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'google_email', 'wv_email',], name='name of constraint')
        ]

        #unique_together = ('question', 'google_email', 'wv_email',)  unique_together 보다 constraints기능을 사용하는 UniqueConstraint것이 좋습니다 .


    def __str__(self):
        return self.google_email


class RequestWork(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    category_choice = (
        ('ga_analysis', 'WV홈페이지(패밀리사이트) GA 관련 분석'),
        ('analysis_account', '분석 툴 계정 신청'),
        ('ga_setup', 'Google Analytics 설치 및 추가 행동 데이터 추적'),
        ('optimize', '페이지 UX 최적화(A/B Test)'),
        ('etc', '기타 디지털 분석'),
    )
    category_state = models.CharField(max_length=50, choices=category_choice, default=category_choice[0][0])
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    progress_choice = (
        ('request', '요청'),
        ('in_progress', '진행중'),
        ('not_in_progress', '진행안함'),
        ('ok', '처리완료'),
    )
    progress_state = models.CharField(max_length=50, choices=progress_choice, default=progress_choice[0][0])
    feedback = models.TextField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.subject

