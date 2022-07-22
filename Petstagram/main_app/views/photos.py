from django.shortcuts import render, redirect

from Petstagram.main_app.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from Petstagram.main_app.models import PetPhoto
from Petstagram.main_app.views.others import get_profile


def add_photo(request):
    if request.method == 'POST':
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = PhotoCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'photo_create.html', context)


def photo_delete(request, pk):
    photo = PetPhoto.objects.get(id=pk)
    form = PhotoDeleteForm(instance=photo)
    if request.method == 'POST':
        photo.delete()
        return redirect('home_page')
    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photo_delete.html', context)


def photo_edit(request, pk):
    phototo = PetPhoto.objects.get(id=pk)
    if request.method == 'POST':
        form = PhotoEditForm(request.POST, instance=phototo)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = PhotoEditForm(instance=phototo)

    contex = {
        'phototo': phototo,
        'form': form,
    }
    return render(request, 'photo_edit.html', contex)


def photo_details(request, pk):
    phototo = PetPhoto.objects.get(id=pk)
    contex = {
        'phototo': phototo,
    }
    return render(request, 'photo_details.html', contex)


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo_details', pk)
