# Generated by Django 4.0.3 on 2022-04-02 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_article_chategory_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='chategory_id',
            new_name='category_id',
        ),
    ]
