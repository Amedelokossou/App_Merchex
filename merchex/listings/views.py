from django.shortcuts import render
from .models import Band
from listings.forms import ContactUsForm


def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})



def contact(request):
  form = ContactUsForm()  # ajout d’un nouveau formulaire ici
  return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit