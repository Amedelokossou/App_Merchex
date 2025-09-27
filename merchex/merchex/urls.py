from django.contrib import admin
from django.urls import path
from listings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'), # mise à jour du chemin et de la vue
    path("bands/<int:id>/", views.band_detail, name="band-detail"), # ajouter ce motif sous notre autre motif de groupes

    path("contact-us/", views.contact, name="contact"), # contact

    
]
