from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    return HttpResponseRedirect("home")


def login(request):
    return HttpResponseRedirect("/login/")


@login_required(login_url='/login/')
def home(request):
        template = loader.get_template('web/index.html')
        return HttpResponse(template.render({'activate': 'home'}, request))


@login_required(login_url='/login/')
def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)



        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/web/register')


    else:
        messages.MessageFailure(request, 'Failed Tray Again')
        f = UserCreationForm()

    template = loader.get_template('web/add_worker.html')
    return HttpResponse(template.render({'form': f}, request))



@login_required(login_url='/login/')
def reguser(request):
    msg = ""
    template = loader.get_template('web/add_user.html')
    return HttpResponse(template.render({'message': msg}, request))



@login_required(login_url='/login/')
def reg(request):
    username = request.POST.get('username')
    password = request.POST.get('pass')
    user = User.objects.create_user(username=username,
                                     password=password)
    user.is_staff = True
    user.save()
    return HttpResponseRedirect('/web/success')

@login_required(login_url='/login/')
def success(request):
   message = "Admin Added Successfully"
   template = loader.get_template(('web/success.html'))
   return HttpResponse(template.render({'msg':message},request))