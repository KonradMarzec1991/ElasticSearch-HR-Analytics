# Generated by Django 3.0.6 on 2020-05-24 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es_core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='date_of_joining',
            new_name='DateOfJoining',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='position',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='interests',
            new_name='Interests',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='LastName',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='martial_status',
            new_name='MaritalStatus',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='salary',
            new_name='Salary',
        ),
    ]
