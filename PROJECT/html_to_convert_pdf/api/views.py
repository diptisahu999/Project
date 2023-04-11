from django.shortcuts import render
from django.http import HttpResponse
from .pdf import html_to_pdf 
from django.views.generic import View
from api import models
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request,'home.html')

# def pdf(request):
#     global pdf
#     pdf=html2pdf(pdf)
#     return HttpResponse(pdf,content_type="application/pdf")

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         data = models.invoices.objects.get(id= 1434)
         open('templates/temp.html', "w").write(render_to_string('result.html',{'data': data} ))

        # Converting the HTML template into a PDF file
         pdf = html_to_pdf('temp.html')
         
         # rendering the template
         return HttpResponse(pdf, content_type='application/pdf')
         # getting the template
         pdf = html_to_pdf('result.html')
         
         # rendering the template
         return HttpResponse(pdf, content_type='application/pdf')
