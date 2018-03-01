import logging
import sys

from django.views import generic
from .models import CheckIn, CheckInType

from django.http import HttpResponse


def get_stdout_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = get_stdout_logger(__name__, level=logging.DEBUG)


class CheckInCreate(generic.CreateView):
    model = CheckIn
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            self.checkin_type = CheckInType.objects.get(pk=request.POST['id'])
        return super().post(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        if hasattr(self, 'checkin_type'):
            initial.update(title=self.checkin_type.title)
        logger.debug(f"Getting initial: {initial}")
        return initial

    def form_valid(self, *args, **kwargs):
        logger.debug("The form is valid!")
        return super().form_valid(*args, **kwargs)

    def form_invalid(self, form):
        logger.debug("The form is invalid!")
        if hasattr(self, 'checkin_type'):
            form['title'].initial = self.checkin_type.title
            logger.debug(f"The form's inital title is now {form['title'].initial}")
        return super().form_invalid(form)


class CheckInUpdate(generic.UpdateView):
    model = CheckIn
    fields = '__all__'


class CheckInList(generic.ListView):
    model = CheckIn


class CheckInDetail(generic.DetailView):
    model = CheckIn


def get_checkin_type(request):
    # logger.debug("The get_checkin_type endpoint received a request!")
    logger.debug(f"The endpoint got a request! Here is request.POST: {request.POST}")
    # import ipdb; ipdb.set_trace()
    return HttpResponse("It worked!")
