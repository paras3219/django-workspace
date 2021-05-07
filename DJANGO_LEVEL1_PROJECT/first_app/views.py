from django.shortcuts import render
from django.http import HttpResponse
# from first_app.models import Topic,AccessRecord,Webpage,User
from first_app.forms import Newuser

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def user(request):
    # webpages_list = User.objects.order_by('first_name')
    # f_dict = {'user':webpages_list}
    # return render(request, 'first_app/user.html', context=f_dict)
    
    form = Newuser()

    if request.method == 'POST':
        form = Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID!")

    return render(request, 'first_app/user.html', {'form':form})


def help(request):
    my_help = {'help':"HELP ME!"}
    return render(request, 'first_app/help.html', context=my_help)
