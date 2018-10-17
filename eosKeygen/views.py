from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from eosjs_python import Eos
import json
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def keyGenBtn(request):

    key_pair = Eos.generate_key_pair()
    return HttpResponse(json.dumps(key_pair), content_type='application/json')





