from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'form.html')

def submitForm(request):
 
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return render (request, 'result.html')

def goBack(request):
    if request.method=='POST':
        return redirect('/')