# Generated by Django 2.2.2 on 2019-06-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='review',
            new_name='Feedback',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fname',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='lname',
            new_name='Last_Name',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Age',
            field=models.IntegerField(default='0'),
        ),
    ]