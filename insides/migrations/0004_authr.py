# Generated by Django 4.0.2 on 2022-04-04 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insides', '0003_authors_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insides.books')),
            ],
        ),
    ]
