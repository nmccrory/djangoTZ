from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
	now = datetime.datetime.now()
	data = {'time': now}
	return render(request, 'timey/index.html', data)