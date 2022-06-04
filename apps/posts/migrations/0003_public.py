# Generated by Django 4.0.4 on 2022-06-02 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_image', models.ImageField(blank=True, null=True, upload_to='public_image/')),
                ('public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='public_image', to='posts.post')),
            ],
            options={
                'verbose_name': ' Фото новостей ',
                'verbose_name_plural': 'Фотки новостей ',
            },
        ),
    ]
