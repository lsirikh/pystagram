from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm
from django.shortcuts import get_object_or_404


# Create your views here.

def hello(request):
    return HttpResponse('안녕하세요!')

def detail(request, pk):

    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄께요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}"/></P>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))

def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)



    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)

