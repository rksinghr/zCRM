from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ProjectMaster, BOQ, Product
from .forms import ProjectForm, InvoiceItemForm
from django.contrib.auth.models import User
from .utils import render_to_pdf  # We'll create this utility function later
import json

# View to display all invoices
def project_list(request):
    projects = ProjectMaster.objects.all()
    return render(request, 'invoices/project_list.html', {'projects': projects})

# View to generate PDF for an invoice
def generate_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    pdf = render_to_pdf('invoices/invoice_pdf.html', {'invoice': invoice})
    return HttpResponse(pdf, content_type='application/pdf')

def create_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save()
            return redirect('project_list')
    else:
        project_form = ProjectForm()

    return render(request, 'invoices/create_project.html', {'project_form': project_form})

def create_BOQ(request, project_id):
    project = get_object_or_404(ProjectMaster, id=project_id)
    prod_list = Product.objects.all()  # Fetch list from Product Master
    for prod in prod_list:
        BOQ.objects.get_or_create(projectID=project, product=prod)
    # Fetch the linked tasks
    linked_tasks = BOQ.objects.filter(projectID=project).select_related('product')

    # Convert to dictionary: Group BOQs by product category (or another attribute)
    boq_dict = {}
    for task in linked_tasks:
        category_name = task.product.category  # Assuming Product has a ForeignKey to Category
        if category_name not in boq_dict:
            boq_dict[category_name] = []  # Initialize category list
        # Append BOQ entry
        boq_dict[category_name].append({
            'id': task.product.id,
            'activity': task.product.activity
            })
        
    if request.method == 'POST':
        project.name = request.POST.get("name")
        # project.description = request.POST.get("description") add later
        project.save()
        return redirect("invoices/create_BOQ", project_id=project.id)

    return render(request, "invoices/create_BOQ.html", {"project_id": project.id, "tasks": boq_dict})

@csrf_exempt
@require_POST
def save_boq(request):
    try:
        data = json.loads(request.body)
        boqdata = data.get('boqdata', [])
        project_id = data.get('project_id')
        

        for item in boqdata:
            project_id = item.get('project_id')
            product_id = item.get('product_id')
            price = item.get('price')
            quantity = item.get('quantity')

            if product_id and price is not None and quantity is not None:
                try:
                    boq = BOQ.objects.get(projectID=project_id, product=product_id)
                    boq.price_per_item = price
                    boq.quantity = quantity
                    boq.save()
                except boq.DoesNotExist:
                    return JsonResponse({'error': 'Product not found'}, status=404)

        return JsonResponse({'message': 'Prices and quantities saved successfully!'})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
