import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic import list_detail
from django.core.paginator import Paginator, InvalidPage
from django.contrib.auth.models import User

from mdc3.board.views import view_thread

from models import Event, Market
from forms import NewEventForm


@login_required
def view_event(request, ev_id):
    event = get_object_or_404(Event,pk=ev_id)
    return view_thread(request,event.thread.id)

@login_required
def list_events(request, upcoming=True, local=True):
    queryset = Event.objects.all()
    if upcoming:
        queryset = queryset.filter(time__gte=datetime.datetime.now)
        
    usr_mrk = request.user.get_profile().market
    if usr_mrk:
        if usr_mrk.id == 1:
            local = False
        if local:
            queryset = queryset.filter(Q(
                Q(market=usr_mrk) | Q(market__id=1)))
    queryset = queryset.order_by('time')

    return list_detail.object_list(
        request,
        queryset = queryset,
        paginate_by = 50,
        extra_context={
            'upcoming' : upcoming,
            'local' : local,
            }
        )
    

    
    
@login_required
def new_event(request):
    if request.method =='POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/')
    else:
        form = NewEventForm()
    return render_to_response('events/new_event.html',
        {
            'form': form,
        },
        context_instance = RequestContext(request))
