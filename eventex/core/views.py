# coding: utf-8
from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker

def homepage(request):
    return render(request, 'core/index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)
