from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.utils.encoding import smart_str
import json
from main.jsonFormM import jsonForm
import random

from main.service import is_json, TEI_STRUCT


def index(request):
    return render(request,"Index.html",{})




def json_upload(request):
    if request.method == 'POST':
      print("tst")
      file= request.FILES['jsonFile']
      if file.content_type=='application/json' :
            print(file.content_type)
            f = FileSystemStorage()
            name ="temp"+str(random.randint(1,2000))+".txt"
            n =f.save(name,file)
            if(is_json(name)):
                print("true")
            else :
                return render(request,'jsonUpload.html', {'error':file.name})
            return HttpResponseRedirect('/')
      else :
          return render(request,'jsonUpload.html', {'error':file.name})
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