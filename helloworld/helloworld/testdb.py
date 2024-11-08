from django.http import HttpResponse
from TestModel.models import Test


def add(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    test = Test(name=name, age=age)
    test.save()
    return HttpResponse("<p>数据添加成功</p>")

def getAll(request):
    list = Test.objects.all()
    response = ''
    for var in list:
        response += var.name + " "
    return HttpResponse("<p>" + response + "</p>")

def update(request):
    id = request.GET.get('id')
    test = Test.objects.get(id = id)
    test.name = 'gggg'
    test.save()
    return HttpResponse("<p>修改成功</p>")

def delete(request):
    id = request.GET.get('id')
    test = Test.objects.get(id = id)
    test.name = 'gggg'
    test.delete()
    return HttpResponse("<p>删除成功</p>")