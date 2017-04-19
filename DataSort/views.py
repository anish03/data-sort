from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import numpy as np

def index(request):
    template = loader.get_template('DataSort/index.html')
    return HttpResponse(template.render(request))

def plot(request,n):
    current_url = request.get_full_path()
    n = current_url.split('/')
    array = np.random.randint(0,25,int(n[-2]))

    def insertion_sort(arr):
        frames = []

        for j in range(1,len(arr)):
            key = arr[j]
            i = j - 1
            while(arr[i] > key and i >= 0):
                arr[i+1] = arr[i]
                i = i - 1
            arr[i+1] = key
            frames.append(arr[0:])

        return frames

    context = {
        'x': len(array)+1,
        'y': array.tolist(),
        'frames': insertion_sort(array.tolist())
    }

    template = loader.get_template('DataSort/index.html')
    return HttpResponse(template.render(context,request))

def result(request):

    array = np.random.randint(0,50,10)

    def insertion_sort(arr):
        frames = []

        for j in range(1,len(arr)):
            key = arr[j]
            i = j - 1
            while(arr[i] > key and i >= 0):
                arr[i+1] = arr[i]
                i = i - 1
            arr[i+1] = key
            frames.append(arr[0:])

        return frames

    context = {
        'x': len(array)+1,
        'y': array.tolist(),
        'frames': insertion_sort(array.tolist())
    }

    template = loader.get_template('DataSort/index.html')
    return HttpResponse(template.render(context,request))

