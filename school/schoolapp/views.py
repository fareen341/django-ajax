from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib import messages


def AddStudent(request):
    student_data = Student.objects.all()
    response = {}
    try:
        if request.method=="POST":            
            name=request.POST['name']
            desc=request.POST['desc']
            age=request.POST['age']
            Student(student_name=name, desc=desc, age=age).save()
            response["status"] = True
            response['msg'] = "data added successfully"
            return JsonResponse(json.dumps(response), safe=False)
        else:
            fm = StudentForm()
            return render(request,"index.html", {"form":fm, "data":student_data})
    except Exception as e:
        print(e)
        response["status"] = False
        response['msg'] = "data cannot be submitted"
        return JsonResponse(json.dumps(response), safe=False)


def updateStudent(request):
    response={}
    try:
        if request.method=="POST":
            student_id = request.POST.get('id')
            print("product id in edit fun=====>",student_id)
            name=request.POST['name']
            desc=request.POST['desc']
            age=request.POST['age']
            print("values",name, desc, age)
            Student.objects.filter(id=student_id).update(student_name=name, desc=desc, age=age)
            response["status"] = True
            response['msg'] = "data update successfully"
            return JsonResponse(json.dumps(response), safe=False)
        else:
            fm = StudentForm()
            return render(request,"index.html", {"form":fm})
    except Exception as e:
        print(e)
        response["status"] = False
        response['msg'] = "data cannot be submitted"
        return JsonResponse(json.dumps(response), safe=False)



def ProductView(request):
    response={}
    msg=""
    if request.method=="POST":
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            msg=messages.success(request, 'Your message has been inserted.')
            # response["status"] = True
            # response['msg'] = "added"
            fm=StudentForm()
            # return JsonResponse(json.dumps(response), safe=False)
            # return JsonResponse(response)
            
    else:
        fm=StudentForm()
    j=Student.objects.all()
    return render(request, 'add_student.html',{'form':fm,'job':j, "msg":msg})

# def editData(request):
#     response = {}
#     if request.method == "POST":
#         id=request.POST.get('id')
#         prod =Student.objects.get(pk=id)
#         print("prod",prod)
#         prod_data = {"id":prod.id, "name":prod.student_name, "desc":prod.desc, "age":prod.age}
#         print(prod_data)
#         # response['status'] = 'true'
#         # response['msg'] = 'Record Updated'
#         return JsonResponse(json.dumps(prod_data), safe=False)