# Generated by Django 2.2.5 on 2019-09-30 07:10

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
            name='ArtCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('period', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CvCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('Your_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('time_chosen', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', models.ImageField(upload_to='')),
                ('bio', models.TextField(max_length=500)),
                ('hobbies', models.TextField()),
                ('contact', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='webmedia/%Y/%m/%d/')),
                ('size', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('datemade', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('categorie', models.ManyToManyField(to='portfolio.ArtCategory')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Profile')),
            ],
        ),
    ]
