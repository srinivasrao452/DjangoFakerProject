
from django.shortcuts import render,redirect
from employeeapp.models import Employee

#pip install faker

from faker import Faker
fakerObject = Faker()

def Employee_Create_View(request):
    for i in range(50):
        first_name = fakerObject.first_name()
        last_name = fakerObject.last_name()
        email = fakerObject.email()
        # city = fakerObject.city()
        city = fakerObject.random_element(
            elements=('Hyderabad','Pune','Mumbai','Delhi'))

        salary = fakerObject.random_element(elements=(10000,20000,30000,40000))
        role = fakerObject.random_element(
            elements=('PM','SR','JR','TM'))

        Employee.objects.create(
            first_name=first_name, last_name=last_name,email=email,
            city=city, salary=salary, role=role
        )
    return redirect('display_employee')


def Employee_Display_View(request):
    employee_list = Employee.objects.all()
    employee_count = Employee.objects.count()
    salary_30k_employees = Employee.objects.filter(salary=30000).count()
    # salary_30k_employees = Employee.objects.filter(salary__lt=30000).count()
    # salary_30k_employees = Employee.objects.filter(salary__lte=30000).count()
    # salary_30k_employees = Employee.objects.filter(salary__gt=30000).count()
    # salary_30k_employees = Employee.objects.filter(salary__gte=30000).count()
    # salary_30k_employees = Employee.objects.filter(salary__in=[20000,40000]).count()
    # salary_30k_employees = Employee.objects.exclude(salary__in=[20000,40000]).count()
    # salary_30k_employees = Employee.objects.filter(salary__range=[20000,40000]).count()

    context = {
        "employee_list" : employee_list,
        "employee_count" : employee_count,
        "salary_30k_employees":salary_30k_employees
    }
    return render(request, 'employee_display.html',context)


def templates_tags_view(request):
    context = {
        "name" : "Virat",
        "salary" : 10000,
        "numbers" : [1111122222,2222233333],
        "address" : {"city" : "delhi", "state" : "delhi", "country" : "india"}
    }
    return render(request,'tags.html',context)


from django.core.paginator import Paginator
from django.core import paginator
def read_employee_list(request):
    employee_list = Employee.objects.all() # 50

    p = Paginator(employee_list, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except paginator.PageNotAnInteger:
        page_obj = p.page(1)
    except paginator.EmptyPage:
        page_obj = p.page(1)

    context = {
        "page_obj" : page_obj
    }
    return render(request, 'read_employee.html', context)



