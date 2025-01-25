from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("disco", "0001_initial"),
    ]

    forward_sql = """
        INSERT INTO public.plugins(
            pluginid, name, icon, component, componentname, config, slug, sortorder, helptemplate)
            VALUES ('a36dc14c-76d8-4926-a644-de0a139d7205', 
            '{"en": "Reference and Sample Collection Search"}', 
            'fa fa-archive', 
            'views/components/plugins/rascoll-viewer', 
            'rascoll-viewer', 
            '{"show": true, "description": {"en": null}, "i18n_properties": ["description"]}', 
            'rascoll-viewer', 
            1, 
            ''
        );
    """
    reverse_sql = """
        DELETE FROM public.plugins WHERE pluginid = 'a36dc14c-76d8-4926-a644-de0a139d7205';
    """

    operations = [
        migrations.RunSQL(forward_sql, reverse_sql),
    ]
