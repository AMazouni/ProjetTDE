from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.utils.encoding import smart_str
import json

from DjangoProject.settings import BASE_DIR
from main.jsonFormM import jsonForm
import random

from main.service import is_json, TEI_STRUCT, JSON_SCHEMA, jsonschemavalidate, createXml


def index(request):
    return render(request,"Index.html",{})






def json_upload(request):
    if request.method == 'POST':
      print("tst")
      file= request.FILES['jsonFile']
      print(type(file))
      print(file)
      if file.content_type=='application/json' :
            print(file.content_type)
            print(type(file))
            print()
            f = FileSystemStorage(location=BASE_DIR)
            name = "temp" + str(random.randint(1, 2000)) + ".txt"
            print(name)
            n = f.save(name=name, content=file)
            print("n=" + str(n))
            path = f.path(name=n)
            if  is_json(path) == False:
                return render(request,'jsonUpload.html', {'error':"This file does not contain a well formated json!"})
            if isinstance(jsonschemavalidate(path),str) :
                return render(request, 'jsonUpload.html', {'error': "This file doesn't obey to the minimal structure of TEI!"+jsonschemavalidate(path)})

            createXml(path)
            return HttpResponseRedirect('/')
      else :
          return render(request,'jsonUpload.html', {'error':"This file is not a json type!"})
    else:
        form = jsonForm()
    return render(request, 'jsonUpload.html', {})


def download(request):
    file_name = ""
    path_to_file = ""
    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response


def getJsonSample(request):
    response = HttpResponse(json.dumps(TEI_STRUCT),content_type="application/json")

    return  response;

def getJsonSchema(request):
    response = HttpResponse(json.dumps(JSON_SCHEMA),content_type="application/json")

    return  response;