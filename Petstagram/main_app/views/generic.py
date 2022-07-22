from django.shortcuts import render

from Petstagram.main_app.models import PetPhoto


def home_page(request):
    context = {
        'hide_additional_nav_item': True,
    }
    return render(request, 'home_page.html', context)


def dashboard(request):
    # profile = get_profile()
    # pets = profile.pet_set.all()
    pet_photos = PetPhoto.objects.all()
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)