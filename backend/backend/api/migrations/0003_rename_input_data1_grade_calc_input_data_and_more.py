# Generated by Django 4.2.20 on 2025-03-30 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_input_data_grade_calc_input_data1_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="grade_calc", old_name="input_data1", new_name="input_data",
        ),
        migrations.RenameField(
            model_name="grade_calc", old_name="input_file1", new_name="input_file",
        ),
        migrations.RemoveField(model_name="grade_calc", name="input_data2",),
        migrations.RemoveField(model_name="grade_calc", name="input_file2",),
    ]
