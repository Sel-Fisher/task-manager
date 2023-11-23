# Generated by Django 4.2.7 on 2023-11-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0004_alter_task_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="complete_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("Urgent", "1"),
                    ("High", "2"),
                    ("Medium", "3"),
                    ("Low", "4"),
                    ("Optional", "Optional"),
                ],
                default="4",
                max_length=255,
            ),
        ),
    ]