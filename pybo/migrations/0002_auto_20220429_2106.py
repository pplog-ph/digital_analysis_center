# Generated by Django 3.1.3 on 2022-04-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestwork',
            name='category_state',
            field=models.CharField(choices=[('ga_analysis', 'WV홈페이지(패밀리사이트) GA 관련 분석'), ('ga_setup', 'Google Analytics 설치 및 추가 행동 데이터 추적'), ('optimize', '페이지 UX 최적화(A/B Test)'), ('etc', '기타 디지털 분석')], default='ga_analysis', max_length=50),
        ),
    ]
