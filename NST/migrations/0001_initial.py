# Generated by Django 3.0.7 on 2020-11-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(default='img1.jpg', upload_to='content/uploads', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.ImageField(default='img2.jpg', upload_to='style/uploads', verbose_name='')),
            ],
        ),
    ]
