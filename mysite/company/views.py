from django.shortcuts import render
from django.core.paginator import Paginator
from company.forms import Companyform
from company.models import Company

#todo:index
def home(request):
    return render(request, 'home.html')

#todo:view for render form     
def create_form(request):
    
    form_company = Companyform()
    context = {'form': form_company}
    return render(request, 'form.html', context)

#todo:view for render list form
def list_form(request):
    
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 2) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj,'count_elements':company_list.count()})
  

