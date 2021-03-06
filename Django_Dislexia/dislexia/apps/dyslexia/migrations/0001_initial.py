# Generated by Django 3.1.1 on 2020-09-28 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id_especialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Niño',
            fields=[
                ('id_niño', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyslexia.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.AutoField(primary_key=True, serialize=False)),
                ('resultado', models.CharField(max_length=8)),
                ('descripcion', models.CharField(max_length=50)),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dyslexia.especialista')),
            ],
        ),
    ]
