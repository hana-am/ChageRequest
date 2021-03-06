from django.shortcuts import render
from django.http import HttpResponse
from app.models import Requst
from django.template import RequestContext, loader 

from app.forms import ContactForm # for the form def (contact us )
from django.http import HttpResponseRedirect # need for contact us 
from django.core.mail import send_mail # need for contact us 

#===============================================
#here is the request form 
from forms import RequstForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    latest_request_list = Requst.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {
        'latest_request_list': latest_request_list,
    })
    return HttpResponse(template.render(context))

def results(request, request_id):
    response = "You're looking at the results of request %s."
    return HttpResponse(response % request_id)

def search_form(request):
    #template = loader.get_template('app/search_form.html')
    #context = RequestContext(request, {
        
    #})
    #return HttpResponse(template.render(context))
    return render(request, 'app/search_form.html') # this is anather way to point at a template , the comment above is the first way 

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        r = Requst.objects.filter(title__icontains=q)
        return render(request, 'app/search_results.html',
            {'req': r, 'query': q})
    else:
        #return HttpResponse('Please submit a search term.')
        return render(request, 'app/search_form.html', {'error': True})
#===============================================================================
#create request funcation 
def create(request):
    if request.POST:
    #if request.method == 'POST':
        form = RequstForm(request.POST)
        if form.is_valid():
            print form.errors
            form.save()
                         
            return HttpResponseRedirect('/app/thanks')
    #else:
      #  form = RequstForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('app/create_article.html',args)

def thanks(request):
    return render_to_response('app/success.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'app/contact_form.html', {'form': form})



