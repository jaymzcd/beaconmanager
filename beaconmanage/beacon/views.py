from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from .models import Beacon


class BeaconCreateView(CreateView):
    model = Beacon

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(BeaconCreateView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print self.request.POST
        return super(BeaconCreateView, self).post(request, *args, **kwargs)
