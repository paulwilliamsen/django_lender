# Generated by Django 2.1.7 on 2019-03-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('author', models.CharField(max_length=4096)),
                ('year', models.CharField(max_length=4096)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_borrowed', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('checked_out', 'Checked Out')], default='available', max_length=48)),
            ],
        ),
        migrations.DeleteModel(
            name='First',
        ),
    ]