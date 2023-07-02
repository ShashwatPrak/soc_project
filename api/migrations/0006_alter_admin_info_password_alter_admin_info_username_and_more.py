# Generated by Django 4.2.2 on 2023-06-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_courses_remove_admin_info_id_remove_student_info_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin_info",
            name="Password",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="admin_info",
            name="Username",
            field=models.CharField(
                default="", max_length=100, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="courses",
            name="courseCode",
            field=models.CharField(default="", max_length=5),
        ),
        migrations.AlterField(
            model_name="courses",
            name="courseId",
            field=models.CharField(
                default="", max_length=5, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="student_info",
            name="Password",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="student_info",
            name="Roll",
            field=models.CharField(
                default="", max_length=100, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="ta_info",
            name="Password",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="ta_info",
            name="Roll",
            field=models.CharField(
                default="", max_length=100, primary_key=True, serialize=False
            ),
        ),
    ]
