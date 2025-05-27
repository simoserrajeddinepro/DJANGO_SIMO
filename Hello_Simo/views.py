from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count




# Create your views here.

def hello_view(request):
        return render(request, 'Hello_Simo/home.html', {'name': 'Mohammed'})
def personalized_hello(request, name):
    return render(request, 'Hello_Simo/home.html', {'name': name})


@login_required
@login_required
def student_list(request):
    search_query = request.GET.get('q', '')
    all_students = Student.objects.filter(user=request.user)

    if search_query:
        all_students = all_students.filter(name__icontains=search_query)

    paginator = Paginator(all_students, 5)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'Hello_Simo/student_list.html', {
        'students': students,
        'search_query': search_query
    })

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'Hello_Simo/add_student.html', {'form': form})

@login_required
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'Hello_Simo/edit_student.html', {'form': form, 'student': student})

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'Hello_Simo/delete_confirm.html', {'student': student})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'Hello_Simo/register.html', {'form': form})

@login_required
def dashboard(request):
    students = Student.objects.filter(user=request.user)

    total = students.count()
    enrolled = students.filter(enrolled=True).count()
    not_enrolled = students.filter(enrolled=False).count()

    return render(request, 'Hello_Simo/dashboard.html', {
        'total': total,
        'enrolled': enrolled,
        'not_enrolled': not_enrolled
    })
