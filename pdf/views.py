from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic import ListView

from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Customer


class CustomerList(ListView):
    template_name = 'pdf/customer.html'
    model = Customer
    queryset = Customer.objects.all()


def customer_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)

    template_path = 'pdf/pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if we want to download the pdf :
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if we want to display the pdf :
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request):
    template_path = 'pdf/pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if we want to download the pdf :
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if we want to display the pdf :
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
