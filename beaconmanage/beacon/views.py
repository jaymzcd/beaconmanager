from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from .models import Beacon


class BeaconAddView(CreateView):
    model = Beacon

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(BeaconAddView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            beacon = Beacon.objects.get(uuid=request.POST['uuid'], major=request.POST['major'], minor=request.POST['minor'])
            # Upate time
            beacon.save()
            return redirect(beacon.get_absolute_url())
        except Beacon.DoesNotExist:
            return super(BeaconAddView, self).post(request, *args, **kwargs)
