# Generated by Django 3.1.14 on 2022-12-11 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['created_at'], 'verbose_name': 'Board', 'verbose_name_plural': 'Boards'},
        ),
        migrations.CreateModel(
            name='BoardSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('max_issues_limit', models.PositiveIntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_sections', to='boards.board')),
            ],
            options={
                'verbose_name': 'Board Section',
                'verbose_name_plural': 'Board Sections',
                'ordering': ['created_at'],
            },
        ),
    ]
