from django.http import HttpResponse, HttpRequest 
from django.shortcuts import render, redirect 
from .forms import * 
from .measurements import measure_dimensions
# Create your views here.
def success(request):
    return HttpResponse('successfully uploaded') 
def upload_image_to_be_measured_view(request):
    if request.method == 'POST':
        form = PhotoToBeMeasuredForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            photo_to_be_measured = PhotoToBeMeasured.objects.last()
            photo = "http://"+HttpRequest.get_host(request)+"/media/"+str(photo_to_be_measured.main_photo)
            width= photo_to_be_measured.left_most_width
            measure_dimensions(photo, width)
            return redirect('success')
    else:
        form = PhotoToBeMeasuredForm()
    return render(request, 'image_to_be_measured_form.html', {'form': form})
