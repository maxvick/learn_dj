from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import SBForm, ModCForm
from .models import RunHistory, RunValues

def get_rh(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
	# create a form instance and populate it with data from the request:
        #qs = RunHistory.objects.all()
        #ch_list = []
		
        #for i in range(len(qs)):
        #    ch_list.append((qs[i].run_name, qs[i].id))

        form = ModCForm(request.POST)


        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(form.cleaned_data['run_hist'])
        else:
            return HttpResponse('form data was not valid')

    # if a GET (or any other method) we'll create a blank form
    else:
        qs = RunHistory.objects.all()
        ch_list = []
		
        for i in range(len(qs)):
            ch_list.append((qs[i].run_name, qs[i].id))
			
        #form.fields['run_hist'].choices = ch_list
        #form = SBForm(ch_list)
        form = ModCForm()

        return render(request, 'selbox/templates/sb.html', {'form': form})
