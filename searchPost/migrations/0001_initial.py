# Generated by Django 3.1.13 on 2021-12-04 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pushat', models.DateField(auto_created=True, auto_now_add=True)),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='post')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='post')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='post')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='post')),
                ('numberOfSaved', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='searchPost.categoryes')),
                ('kannel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.kennel')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='searchPost.post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='searchPost.sizes'),
        ),
    ]
