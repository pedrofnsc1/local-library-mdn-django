# Generated by Django 4.0.2 on 2022-03-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_make_returned', 'Set book as returned'),)},
        ),
    ]
