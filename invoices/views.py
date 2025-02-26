from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from .utils import render_to_pdf  # We'll create this utility function later

# View to display all invoices
def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})

# View to generate PDF for an invoice
def generate_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    pdf = render_to_pdf('invoices/invoice_pdf.html', {'invoice': invoice})
    return HttpResponse(pdf, content_type='application/pdf')

def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        item_form = InvoiceItemForm(request.POST)
        if invoice_form.is_valid() and item_form.is_valid():
            # Create the invoice object but don't save it yet
            invoice = invoice_form.save(commit=False)
            invoice.save()  # Save the invoice to get its ID
            
            # Now create the invoice items
            product = item_form.cleaned_data['product']
            quantity = item_form.cleaned_data['quantity']
            price_per_item = item_form.cleaned_data['price_per_item']
            InvoiceItem.objects.create(invoice=invoice, product=product, quantity=quantity, price_per_item=price_per_item)
            
            # Calculate total amount for the invoice
            total_amount = sum(item.total_price() for item in invoice.items.all())
            invoice.total_amount = total_amount
            invoice.save()
            
            return redirect('invoice_list')
    else:
        invoice_form = InvoiceForm()
        item_form = InvoiceItemForm()

    return render(request, 'invoices/create_invoice.html', {'invoice_form': invoice_form, 'item_form': item_form})