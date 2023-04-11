# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa



# def html2pdf(templates_source,contect_dict={}):
#     templates=get_template(templates_source)
#     html=templates.render(contect_dict)
#     result=BytesIO
#     pdf=pisa.pisaDocument(BytesIO(html.encode("cpl252")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),contect_type="application/pdf")
#     return None

# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None