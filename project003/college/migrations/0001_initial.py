# Generated by Django 3.2.3 on 2021-06-26 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ECE', 'Electroonics and communication'), ('MECH', 'Mechanical')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=150)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('ssc_marks', models.IntegerField()),
                ('inter_marks', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('father_name', models.CharField(max_length=150)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college.department')),
                ('student_app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='college.studentapplication')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('qualification', models.CharField(max_length=140)),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]