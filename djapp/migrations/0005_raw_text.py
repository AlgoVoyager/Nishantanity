# Generated by Django 3.2.7 on 2022-02-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0004_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='raw_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RawText', models.TextField(max_length=1000)),
                ('rdate', models.DateTimeField()),
            ],
        ),
    ]