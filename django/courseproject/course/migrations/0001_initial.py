# Generated by Django 4.2.4 on 2023-09-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, null=True)),
                ('fee', models.IntegerField(null=True)),
            ],
        ),
    ]
