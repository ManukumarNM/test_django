# Generated by Django 3.0.3 on 2020-05-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('monitoring', '0008_remove_graph_fields')]

    operations = [
        migrations.AlterField(
            model_name='threshold',
            name='value',
            field=models.FloatField(help_text='threshold value'),
        )
    ]
