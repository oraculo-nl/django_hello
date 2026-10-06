from datetime import datetime
from decimal import Decimal, InvalidOperation

from django.http import HttpResponse
from django.shortcuts import render, redirect

from budget.forms import UploadForm
from budget.models import Transactie
from budget.utils import bepaal_categorie


# Create your views here.
def transacties(request):
    # return  HttpResponse("Hello")
    alle = Transactie.objects.order_by('-transactiedatum')
    return render(request, "budget/transacties.html", {"transacties": alle})

#
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            bestand = request.FILES['bestand']
            inhoud = bestand.read().decode('utf-8')
            regels = inhoud.strip().splitlines()

            # bestaande data wissen
            Transactie.objects.all().delete()

            for regel in regels:
                velden = regel.split('\t')
                if len(velden) < 8:
                    continue
                try:
                    datum = datetime.strptime(velden[2], '%Y%m%d').date()
                    bedrag = Decimal(velden[6].replace(',', '.'))
                    omschrijving = velden[7].strip()
                    Transactie.objects.create(
                        rekeningnummer=velden[0],
                        transactiedatum=datum,
                        bedrag=bedrag,
                        omschrijving=omschrijving,
                        categorie=bepaal_categorie(omschrijving)
                    )
                except (ValueError, InvalidOperation):
                    continue
            return redirect('transacties')
    else:
        form = UploadForm()
    return render(request, 'budget/upload.html', {'form': form})