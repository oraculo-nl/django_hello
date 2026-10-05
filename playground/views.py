from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .forms import MemberForm
from .charts import simple_plot_png


def hello_form(request):
    message = None
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect("member-success", member.id)
    else:
        form = MemberForm()
    return render(request, "members/member_form.html", {"form": form})

def member_success(request):
    return render(request, "members/member_success.html")


from .models import Member

def member_list(request):
    members = Member.objects.order_by('-joined_date')
    return render(request, "members/member_list.html", {"members": members})

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect("member-success")
    else:
        form = MemberForm()
    return render(request, "members/member_form.html", {"form": form})

@cache_page (60 * 5)# 5 minuten
def simple_plot(request):
    return simple_plot_png(request)

def chart(request):
    return render(
        request,
        "playground/chart.html",
    )

from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Transactie
from .utils import bepaal_categorie
from datetime import datetime
from decimal import Decimal, InvalidOperation

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            bestand = request.FILES['bestand']
            inhoud = bestand.read().decode('utf-8')
            regels = inhoud.strip().splitlines()
            Transactie.objects.all().delete() # bestaande data wissen
            for regel in regels:
                velden = regel.split('\t')
                if len(velden) < 8:
                    continue # ongeldige regel overslaan
                try:
                    datum = datetime.strptime(velden[2], '%Y%m%d').date()
                    bedrag = Decimal(velden[6].replace(',', '.'))
                    omschrijving = velden[7].strip()
                    Transactie.objects.create(
                        rekeningnummer=velden[0],
                        transactiedatum=datum,
                        bedrag=bedrag,
                        omschrijving=omschrijving,
                        categorie=bepaal_categorie(omschrijving),
                        )
                except (ValueError, InvalidOperation):
                    continue
            return redirect('transacties')
    else:
            form = UploadForm()
    return render(request, 'playground/upload.html', {'form': form})


def transacties(request):
    alle = Transactie.objects.order_by('-transactiedatum')
    return render(request, 'playground/transacties.html', {'transacties': alle})



import io
import base64
import matplotlib
matplotlib.use('Agg')
# geen GUI nodig
import matplotlib.pyplot as plt
from django.db.models import Sum
def grafiek(request):
    # Alleen uitgaven (negatieve bedragen)
    data = (
        Transactie.objects
        .filter(bedrag__lt=0)
        .values('categorie')
        .annotate(totaal=Sum('bedrag'))
        .order_by('totaal')
    )

    categorieen = [d['categorie'] for d in data]
    bedragen = [abs(d['totaal']) for d in data]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(categorieen, bedragen, color='steelblue')
    ax.set_xlabel('Totaal uitgegeven (EUR)')
    ax.set_title('Uitgaven per categorie')
    plt.tight_layout()
    # Omzetten naar base64-string voor de template
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    afbeelding = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return render(request, 'playground/grafiek.html', {'afbeelding': afbeelding})