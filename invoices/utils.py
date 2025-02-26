from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    template = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    pisa_status = pisa.CreatePDF(template, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
