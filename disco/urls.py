from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path, path


urlpatterns = [
    re_path(r"^", include("arches.urls")),
    re_path(r"^", include("arches_for_science.urls")),
    path("reports/", include("arches_templating.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)