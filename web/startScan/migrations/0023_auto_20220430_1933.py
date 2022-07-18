# Generated by Django 3.2.4 on 2022-04-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0022_subscan_engine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waf',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='subdomain',
            name='waf',
            field=models.ManyToManyField(blank=True, related_name='waf', to='startScan.Waf'),
        ),
    ]