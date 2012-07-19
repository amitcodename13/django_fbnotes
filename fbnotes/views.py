# Create your views here.
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from fbnotes.models import Note, UserProfile
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

def home(request):
    document_id = ""
    note_title = ""
    note_contents = ""
    
    if request.user.is_authenticated():
        result = request.user.get_profile()
        if result:
            document_id = result.document_id
        else:
            document_id = 1
        
        result = Note.objects.filter(username=request.user, document_id=document_id)
        if result:
            note_contents = result[0].contents
            note_title = result[0].title

    return render_to_response('index.html', {"note_contents":note_contents, "note_title":note_title, "note_selected":document_id,}, RequestContext(request))
    
def save(request):
    if not request.user.is_authenticated():
        return HttpResponse("Login first")
        
    username = request.user
    document_id = request.GET.get('document_id')
    title = request.GET.get('title')
    contents = request.GET.get('contents')
    
    try:
        v = int(document_id)
        if v < 0 or v > 10:
            raise ValueError
    except:
        return HttpResponse("Some error occured")
    
    try:
        result = Note.objects.filter(username=username, document_id=document_id)
        if result:
            result[0].title = title
            result[0].contents = contents
            result[0].save()
        else:
            newnote = Note(username=username, document_id=document_id, title=title, contents=contents)
            newnote.save()
        return HttpResponse("Save successful")
    except:
        return HttpResponse("Some error occured")
       
def note(request):
    if not request.user.is_authenticated():
        return HttpResponse("Login first")
    
    username = request.user
    document_id = request.GET.get('document_id')
    
    if not document_id:
        return HttpResponse("Incomplete request")
    
    try:
        result = request.user.get_profile()
        result.document_id = document_id
    except:
        result= UserProfile(user = request.user, document_id = document_id)
    result.save()
    assert result
    
    try:
        result = Note.objects.filter(username=username, document_id=document_id)
        if(result):
            return HttpResponse(simplejson.dumps({"title":result[0].title, "contents":result[0].contents}))
        else:
            return HttpResponse(simplejson.dumps({"title":"", "contents":""}))
    except:
        return HttpResponse("Some error occurred")
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")