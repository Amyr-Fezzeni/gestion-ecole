from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('microblading/<name>/<day>/<month>/<year>', views.microblading),
    path('brow/<name>/<day>/<month>/<year>', views.brow),
    path('extension_cils/<name>/<day>/<month>/<year>', views.extension_cils),
    path('keratine/<name>/<day>/<month>/<year>', views.keratine),
    path('microneedling/<name>/<day>/<month>/<year>', views.microneedling),
    path('massage/<name>/<day>/<month>/<year>', views.massage),
    path('coiffure_dames/<name>/<day>/<month>/<year>', views.coiffure_dames),
    path('coiffure_homme/<name>/<day>/<month>/<year>', views.coiffure_homme),
    path('esthetique/<name>/<day>/<month>/<year>', views.esthetique),
    path('onglerie/<name>/<day>/<month>/<year>/<day2>/<month2>/<year2>', views.onglerie),
    path('maquilliage/<name>/<day>/<month>/<year>/<day2>/<month2>/<year2>', views.maquilliage),
]
