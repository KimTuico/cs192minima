# Generated by Django 4.0.3 on 2022-04-23 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gspt_test', '0005_alter_specialization_spec_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adviser_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='gspt_test.person'),
        ),
    ]
