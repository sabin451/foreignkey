from django.shortcuts import render,redirect
from course.models import course,student

# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    return render(request,'add_course.html')
def add_student(request):
    return render(request,'add_student.html')
def add_course(request):
    if request.method == 'POST':
        cname=request.POST['course_name']
        fees=request.POST['fee']
        cdetails=course(course_name=cname,fee=fees)
        cdetails.save()
        return redirect('/')
def add_student(request):
    Courses=course.objects.all()
    return render(request,'add_student.html',{'courses':Courses})
def add_studentdb(request):
    if request.method == 'POST':
        name=request.POST['sname']
        address=request.POST['address']
        age=request.POST['age']
        date=request.POST['date']
        sel=request.POST['sel']
        courses=course.objects.get(id=sel)
        Student=student(sname=name,address=address,age=age,date=date,course=courses)
        Student.save()
        return redirect('/')
def show_details(request):
    students=student.objects.all()
    return render(request,'show_details.html',{'students':students})

def edit(request,pk):
    students=student.objects.get(id=pk)
    courses=course.objects.all()
    return render(request,'edit.html',{'courses':courses,'stud':students})
        
def editdb(request,pk):
    if request.method == "POST":
        stud=student.objects.get(id=pk)
        stud.sname=request.POST['sname']
        stud.address=request.POST['address']
        stud.age=request.POST['age']
        stud.date=request.POST['date']
        sel=request.POST['sel']
        courses=course.objects.get(id=sel)
        stud.course=courses
        stud.save()
        return redirect('show_details')
    return render(request,'edit.html')
def delete(request,pk):
    s = student.objects.get(id=pk)
    s.delete()
    return redirect('show_details')
