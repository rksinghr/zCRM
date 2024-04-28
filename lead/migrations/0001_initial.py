# Generated by Django 4.2.6 on 2024-02-23 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('createdOn', models.DateField(auto_now_add=True)),
                ('lastContact', models.DateField()),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.contact')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.status')),
            ],
        ),
    ]
