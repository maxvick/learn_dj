from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone

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
			
        form = ModCForm()

        return render(request, 'selbox/templates/sb.html', {'form': form})

def update_rv(request):
    rh_key = request.GET.get('run_hist', None)
    data = {
        'rv_dat': RunValues.objects.filter(run_history__iexact=rh_key)
    }
    return JsonResponse(data)

class RunHistoryListView(ListView):
    model = RunHistory
    
    template_name = 'selbox/templates/runhistory_list.html'

