from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import Signupform,UploadImageForm,EmployeeForm
from .models import UploadedImage,Emp_details
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')
@login_required
def images(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = UploadImageForm()
        images = UploadedImage.objects.all()
        return render(request,'image.html',{'form':form,'images':images})
@login_required
def iframe(request):
    return render(request,'iframe.html')
@login_required
def multiple(request):
    return render(request,'multipletabs.html')
@login_required
def cssprop(request):
    return render(request,'cssproperties.html')
@login_required
def autocomplete(request):
    return render(request,'Autocomplete.html')
@login_required
def tooltip(request):
    return render(request,'tooltip.html')
@login_required
def links(request):
    return render(request,'links.html')
@login_required
def popups(request):
    return render(request,'popup.html')

@login_required
def slider(request):
    return render(request,'slider.html')
@login_required
def collapse(request):
    return render(request,'collapsable.html')

@login_required
def menu_items(request):
    return render(request,'menu.html')




def signup(request):
    if request.method =='POST':
        form = Signupform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Webpage:login')
    else:
        form = Signupform()

    return render(request,'registration/signup.html',{"form":form})

@login_required
def create_employe(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            print(clean)
            form.save()
            messages.success(request, 'Employee details saved successfully!')
            return redirect('Webpage:create_emp')
    else:
        form = EmployeeForm()
     
    return render(request, 'createemp.html',{'form':form})
@login_required
def show_details(request):
    candidates_list = Emp_details.objects.all()
    paginator = Paginator(candidates_list, 10)  
    page_number = request.GET.get('page')
    candidates_data = paginator.get_page(page_number)
    total_page = candidates_data.paginator.num_pages

    return render(request,'showdetails.html',{'candidate':candidates_data,'lastpage':total_page,'total_page':[n+1 for n in range(total_page)]})
@login_required
def delete_data(request,id):
    if request.method == 'POST':
        pi = Emp_details.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/details/')
@login_required
def update_date(request,id):
    if request.method == 'POST':
        pi = Emp_details.objects.get(pk=id)
        fm = EmployeeForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('Webpage:show_detail')
    else:
        pi = Emp_details.objects.get(pk=id)
        fm = EmployeeForm(instance=pi)

    return render(request,'update.html',{'form':fm})
@login_required
def search_employees(request):
    search_firstname = request.GET.get('search_firstname', '').strip()
    search_mobile = request.GET.get('search_mobile', '').strip()
    candidates = Emp_details.objects.all()


    if search_firstname or search_mobile:
        if search_firstname:
            candidates = candidates.filter(firstname__icontains=search_firstname)

        if search_mobile:
            candidates = candidates.filter(mobile__icontains=search_mobile)

    else:
        candidates = Emp_details.objects.none()

    return render(request, 'search_results.html', {'candidates': candidates})
