# Generated by Django 4.2.2 on 2023-07-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_remove_student_info_course_remove_ta_info_course_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student_info",
            name="Name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="ta_info",
            name="Name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
