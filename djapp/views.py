from django.shortcuts import render,HttpResponse
from datetime import datetime
from djapp.models import Contact,raw_text


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
    return render(request, 'contact.html')



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    modtext = str(djtext)
    op = " | "
    
    
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    
    if removepunc == "on":
        op += "1"
    else:
        op += "0"
    if fullcaps == "on":
        op += "1"
    else:
        op += "0"
    if newlineremover == "on":
        op += "1"
    else:
        op += "0"
    if extraspaceremover == "on":
        op += "1"
    else:
        op += "0"
    modtext += op  
    
    rawtext = raw_text(RawText=modtext,rdate = datetime.today())
    rawtext.save()
   



    global ops
    ops = ''
    if (removepunc == "on" or  fullcaps == "on" or newlineremover == "on" or extraspaceremover=="on"):
        #Check which checkbox is on
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            ops += '-Removed Punctuations.'
            charcount = len(analyzed)
            params = {'purpose':ops, 'analyzed_text': analyzed,'charcount':charcount}
            djtext = analyzed
            # return render(request, 'analyze.html', params)
        if fullcaps == "on":
            analyzed = djtext.upper()
            ops +='\n-Full caps.'
            charcount = len(analyzed)
            params = {'purpose':ops, 'analyzed_text':analyzed,'charcount':charcount}
            # return render(request,'analyze.html',params)
            djtext = analyzed

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
            ops += '\n-New lines removed.'
            charcount = len(analyzed)
            params = {'purpose':ops, 'analyzed_text': analyzed,'charcount':charcount}
            # Analyze the text
            # return render(request, 'analyze.html', params)
            djtext = analyzed

        if extraspaceremover=='on':
            analyzed = ''
            for index, char in enumerate(djtext):
                if not(djtext[index] == ' ' and djtext[index + 1] == ' '):
                    analyzed += char
            ops += '\n-Extra space removed.'
            charcount = len(analyzed)
            params = {'purpose': ops, 'analyzed_text': analyzed,'charcount':charcount}
            #

        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': '', 'analyzed_text': '','charcount':''}
        # return HttpResponse("Must select any options")
        return render(request, 'index.html', params)
