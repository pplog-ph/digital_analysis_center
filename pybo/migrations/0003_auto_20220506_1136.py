# Generated by Django 3.1.3 on 2022-05-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20220429_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestwork',
            name='category_state',
            field=models.CharField(choices=[('ga_analysis', 'WV홈페이지(패밀리사이트) GA 관련 분석'), ('analysis_account', '분석 툴 계정 신청'), ('ga_setup', 'Google Analytics 설치 및 추가 행동 데이터 추적'), ('optimize', '페이지 UX 최적화(A/B Test)'), ('etc', '기타 디지털 분석')], default='ga_analysis', max_length=50),
        ),
    ]
