# Generated by Django 2.2.3 on 2019-08-09 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190809_0348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts3', to=settings.AUTH_USER_MODEL),
        ),
    ]
