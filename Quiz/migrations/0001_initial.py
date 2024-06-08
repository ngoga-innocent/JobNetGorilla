# Generated by Django 4.2.6 on 2024-06-08 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Payment', '0003_payment_type_subscription_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(default=None, null=True, upload_to='faculty')),
                ('description', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('number_of_questions', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=1, verbose_name='Duration of Quiz')),
                ('required_score_to_pass', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.faculties')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('correct', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Payment.otp')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quiz')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_response', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.answer')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quiz'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.question'),
        ),
    ]
