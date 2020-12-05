# Generated by Django 3.1.3 on 2020-12-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('collectible_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('artist', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ComicBook',
            fields=[
                ('collectible_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('illustrator', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('collectible_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SportCard',
            fields=[
                ('collectible_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('sport', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComicGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('comicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comicbook')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('phonenumber', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('userid', 'username')},
            },
        ),
        migrations.CreateModel(
            name='AlbumGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
            ],
        ),
    ]
