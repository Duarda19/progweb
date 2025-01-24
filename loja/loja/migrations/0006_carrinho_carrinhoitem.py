# Generated by Django 4.2.7 on 2025-01-24 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0005_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('situacao', models.PositiveIntegerField(default=0)),
                ('confirmado_em', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrinhos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('carrinho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itens', to='loja.carrinho')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrinhos', to='loja.produto')),
            ],
        ),
    ]
