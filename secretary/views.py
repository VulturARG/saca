################################################################################
#                             Made by Luis Briones
################################################################################

from django.shortcuts import render
from .form import PartnerForm
from .models import Partner

# Create your views here.

def partner_list(request):
    contex = {'partner_list':Partner.objects.all()}
    return render(request,"partner/partner_list.html",contex)

def partner_form(request):
    form = PartnerForm()
    return render(request,"partner/partner_form.html",{'form':form})

def partner_delete(request):
    return

################################################################################
#                             Made by Luis Briones
################################################################################