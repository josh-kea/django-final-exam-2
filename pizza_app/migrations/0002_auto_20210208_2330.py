# Generated by Django 3.1.3 on 2021-02-08 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza_app.pizza')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizzas',
        ),
        migrations.AddField(
            model_name='order',
            name='line_items_total_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='OrderPizza',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='line_item_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pizza_app.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='final_line_items',
            field=models.ManyToManyField(blank=True, to='pizza_app.LineItem'),
        ),
    ]
