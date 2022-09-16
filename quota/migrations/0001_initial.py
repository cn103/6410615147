# Generated by Django 4.1.1 on 2022-09-16 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Registant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('student_id', models.CharField(max_length=10)),
                ('quotas', models.ManyToManyField(blank=True, related_name='registant', to='quota.quota')),
            ],
        ),
        migrations.AddField(
            model_name='quota',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quota.subject'),
        ),
    ]