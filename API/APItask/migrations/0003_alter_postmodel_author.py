# Generated by Django 4.2.2 on 2023-06-18 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APItask', '0002_remove_postmodel_autor_postmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
