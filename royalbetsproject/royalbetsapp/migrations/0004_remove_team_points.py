# Generated by Django 4.0.6 on 2022-09-13 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('royalbetsapp', '0003_alter_team_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='points',
        ),
    ]
