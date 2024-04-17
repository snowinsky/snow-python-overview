from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse(content="Hello world ! ", args = None)

def helloHtmlTemplate(req):
    templateParmMap = {}
    templateParmMap['userName'] = "sdwefqwr223434较高高温"
    templateParmMap['password'] = "asfdas!#%%&**&"
    return render(request=req, template_name='hello.html', context=templateParmMap)