from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Stream


@require_POST
def on_publish(request):
    stream_key = request.POST['name']

    stream = get_object_or_404(Stream, key=stream_key)

    stream.live_at = timezone.now()
    stream.save()

    return HttpResponse(status=204)  # 204 No Content


@require_POST
def on_publish_done(request):
    stream_key = request.POST['name']

    stream = get_object_or_404(Stream, key=stream_key)

    stream.update(live_at=None)

    return HttpResponse(status=200)  # 200 OK
