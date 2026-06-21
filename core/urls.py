from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/",          include("apps.authentication.urls")),
    path("api/users/",         include("apps.users.urls")),
    path("api/ccm/",           include("apps.ccm.urls")),
    path("api/prayer-requests/", include("apps.prayerwinner.urls")),
    path("api/ministries/",    include("apps.ministries.urls")),
    path("api/evangelisation/",include("apps.evangelisation.urls")),
    path("api/events/",        include("apps.events.urls")),
    path("api/teachings/",     include("apps.teachings.urls")),
    path("api/donations/",     include("apps.donations.urls")),
    path("api/newsletter/",    include("apps.newsletter.urls")),
    path("api/contacts/",      include("apps.contacts.urls")),
    path("api/settings/",      include("apps.settings_app.urls")),
    path("api/cinepay/",       include("apps.cinepay.urls")),
    path("api/testimonials/",  include("apps.testimonials.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
