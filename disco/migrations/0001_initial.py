# Generated by Django 3.2.19 on 2023-07-13 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("arches_templating", "0001_initial"),
    ]

    def add_document_templates(apps, schema_editor):
        ArchesTemplate = apps.get_model("arches_templating", "ArchesTemplate")

        ArchesTemplate.objects.update_or_create(
            templateid="72cc4dcf-9500-418f-a42e-7d980937a9db",
            name="Example Template",
            description="This is an example template",
            defaults={
                "template":"document_templates/example-template.docx",
                "preview":"document_templates/72cc4dcf-9500-418f-a42e-7d980937a9db_preview.pdf",
                "thumbnail":"document_templates/72cc4dcf-9500-418f-a42e-7d980937a9db_thumbnail.png",
                }
        )

    def remove_document_templates(apps, schema_editor):
        ArchesTemplate = apps.get_model("arches_templating", "ArchesTemplate")

        example_template = ArchesTemplate.objects.get(templateid="72cc4dcf-9500-418f-a42e-7d980937a9db")
        example_template.delete()

    operations = [
        migrations.RunPython(add_document_templates, remove_document_templates),
    ]
