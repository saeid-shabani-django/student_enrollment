from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Stud
from students.forms import StudForm


def student(request):
    return render(
        request,
        "home.html",
    )


def registration(request):
    form = StudForm(request.POST or None)
    if form.is_valid():
        s_name = form.cleaned_data["s_name"]
        s_class = form.cleaned_data["s_class"]
        s_addr = form.cleaned_data["s_addr"]
        s_school = form.cleaned_data["s_school"]
        s_email = form.cleaned_data["s_email"]
        st = Stud(
            s_name=s_name,
            s_class=s_class,
            s_addr=s_addr,
            s_school=s_school,
            s_email=s_email,
        )
        st.save()
        return render(request,'ack.html')

    context = {"form": form, "title": "Student Registration"}
    return render(request, "registration.html", context)


def registered(request):
    all_students = Stud.objects.all()
    return render(request,'registered.html',{'students':all_students})


def search(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        all_students = Stud.objects.filter(s_name=name).all()
        if not all_students.exists():
            return HttpResponse('<h2>there is no student with this name</h2>')
        return render(request,'registered.html',{'students':all_students})
    
    return render(request,'search.html')


# by this function we remove a student from database
def dropout(request):
    if request.method == 'POST':
        s_name = request.POST.get('nameremove')
        s_class = request.POST.get('classremove')
        items = Stud.objects.filter(s_name=s_name,s_class=s_class).all()
        if not items.exists():
            return HttpResponse('<h2>there is no student with this properties</h2>')
        for item in items:
            print(item)
            item.delete()
        return render(request,'ack2.html')
    return render(request,'dropout.html')
    
    
