# Generated by Django 3.1.7 on 2022-03-01 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0002_subcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image/Product')),
                ('price', models.CharField(max_length=10)),
                ('detail', models.CharField(max_length=600)),
                ('pcate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='med.subcategories')),
            ],
        ),
    ]
