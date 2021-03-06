# Generated by Django 2.2.6 on 2019-10-29 21:05

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
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='hood_photo/hood.jpg', upload_to='hood_photo')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='profile_photo/defaultprofile.jpg', upload_to='profile_photo')),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('contacts', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Hood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Hood')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='facilities/sample.jpg', upload_to='facilities')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Hood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='biz_pic/bizpic.jpg', upload_to='biz_pic/')),
                ('details', models.TextField(max_length=500)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Hood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
