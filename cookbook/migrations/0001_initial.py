# Generated by Django 2.2.7 on 2019-11-19 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('icon', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('instructions', models.TextField(blank=True)),
                ('file_uid', models.CharField(default='', max_length=256)),
                ('file_path', models.CharField(default='', max_length=512)),
                ('link', models.CharField(default='', max_length=512)),
                ('time', models.IntegerField(default=0)),
                ('internal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('keywords', models.ManyToManyField(blank=True, to='cookbook.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('method', models.CharField(choices=[('DB', 'Dropbox'), ('NEXTCLOUD', 'Nextcloud')], default='DB', max_length=128)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('token', models.CharField(blank=True, max_length=512, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(default='', max_length=512)),
                ('active', models.BooleanField(default=True)),
                ('last_checked', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cookbook.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='SyncLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=32)),
                ('msg', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sync', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Sync')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('ingredient', models.CharField(max_length=128)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('file_uid', models.CharField(default='', max_length=256)),
                ('file_path', models.CharField(default='', max_length=512)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cookbook.Storage')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cookbook.Storage'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe')),
            ],
        ),
    ]
