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
from lxml import etree

def index(request):
    return render(request,"Index.html",{})






def json_upload(request):
    if request.method == 'POST':

      file= request.FILES['jsonFile']

      print(file)
      if file.content_type=='application/json' :
            print(file.content_type)
            oldname = file.name

            f = FileSystemStorage(location=BASE_DIR)
            name = "temp" + str(random.randint(1, 2000))
            print(name)
            n = f.save(name=name, content=file)
            print("n=" + str(n))
            path = f.path(name=n)
            if  is_json(path) == False:
                return render(request,'jsonUpload.html', {'error':"This file does not contain a well formated json!"})
            if isinstance(jsonschemavalidate(path),str) :
                return render(request, 'jsonUpload.html', {'error': "This file doesn't obey to the minimal structure of TEI!"+jsonschemavalidate(path)})

            output =createXml(path)
            print(output)
            if not(output[0]) :
                  return render(request, 'jsonUpload.html',
                                {'error': output[1]})
            else :

                return HttpResponse(content=output[1],content_type="text/xml")
      else :
          return render(request,'jsonUpload.html', {'error':"This file is not a json type!"})
    else:

        form = jsonForm()
    return render(request, 'jsonUpload.html', {})




def getJsonSample(request):
    response = HttpResponse(json.dumps(TEI_STRUCT),content_type="application/json")

    return  response;

def getJsonSchema(request):
    response = HttpResponse(json.dumps(JSON_SCHEMA),content_type="application/json")

    return  response;