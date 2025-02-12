# Generated by Django 2.2.14 on 2024-04-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('12', '12 MONTH'), ('01', '1 MONTH'), ('03', '3 MONTH'), ('06', '6 MONTH')], default='12', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('p', 'primary'), ('s', 'secondary'), ('d', 'danger')], default='p', max_length=1),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='package',
            field=models.ManyToManyField(to='core.Package'),
        ),
    ]
