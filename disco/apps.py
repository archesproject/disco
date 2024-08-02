from django.apps import AppConfig

from arches.settings_utils import generate_frontend_configuration


class DiscoConfig(AppConfig):
    name = "disco"
    verbose_name = "Disco"
    is_arches_application = True

    def ready(self):
        generate_frontend_configuration()