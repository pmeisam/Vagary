# Generated by Django 2.1.5 on 2019-03-21 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_suitcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='suitcase',
            name='trip',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.Trip'),
            preserve_default=False,
        ),
    ]