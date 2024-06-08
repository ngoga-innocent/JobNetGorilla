# Generated by Django 4.2.6 on 2024-06-08 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=255)),
                ('valid', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('one', 'One')], default='one', max_length=14)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_validated_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subscription_type', models.CharField(choices=[('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('one', 'One')], max_length=255)),
                ('subscription_valid', models.BooleanField(default=False)),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ref', models.CharField(max_length=255)),
                ('valid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
