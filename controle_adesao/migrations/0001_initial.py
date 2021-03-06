# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('nome', models.CharField(max_length=500)),
                ('status_adesao', models.CharField(max_length=30)),
                ('documento_solicitacao', models.TextField(blank=True, null=True)),
                ('capacitacao', models.CharField(blank=True, max_length=20, null=True)),
                ('modalidade', models.CharField(blank=True, max_length=20, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('id_ator', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Ator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Publicacaoinformacaogeoespacial',
            fields=[
                ('tem_metadados', models.CharField(blank=True, max_length=20, null=True)),
                ('tem_geoservicos', models.CharField(blank=True, max_length=20, null=True)),
                ('tem_download', models.CharField(blank=True, max_length=20, null=True)),
                ('tem_vinde', models.CharField(blank=True, max_length=20, null=True)),
                ('id_publicacao_informacao_geoespacial', models.AutoField(primary_key=True, serialize=False)),
                ('ator', models.ForeignKey(db_column='id_ator', on_delete=django.db.models.deletion.CASCADE, to='controle_adesao.Ator')),
            ],
            options={
                'db_table': 'PublicacaoInformacaoGeoespacial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id_representante', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('e_mail', models.CharField(blank=True, max_length=70, null=True)),
                ('funcao_cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('area_setor', models.CharField(blank=True, max_length=150, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=25, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=25, null=True)),
                ('celular_telefone3', models.CharField(blank=True, max_length=25, null=True)),
                ('ator', models.ForeignKey(db_column='id_ator', on_delete=django.db.models.deletion.CASCADE, related_name='representantes', to='controle_adesao.Ator')),
            ],
            options={
                'db_table': 'Representante',
                'managed': True,
            },
        ),
    ]
