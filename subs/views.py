from django.views.decorators.csrf import csrf_exempt
from .rhymeanalyser.analyser import Analyser
from django.http import HttpResponse, JsonResponse
from .forms import RhymeForm

@csrf_exempt
def analyse(request):
    form = RhymeForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['rhyme']
        analyser = Analyser(text)
        analyser.process();
        return JsonResponse(analyser.get_analysed_as_dict());
    else:
        return HttpResponse(status=500)

@csrf_exempt
def score(request):
    form = RhymeForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['rhyme']
        analyser = Analyser(text)
        analyser.process();
        return JsonResponse(analyser.get_score());
    else:
        return HttpResponse(status=500)
