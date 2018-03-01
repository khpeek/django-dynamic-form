from django.views.generic.edit import CreateView
from cars.models import Car


class CarCreate(CreateView):
	model = Car
	fields = '__all__'