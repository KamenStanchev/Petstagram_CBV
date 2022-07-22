from django.shortcuts import render, redirect

from Petstagram.main_app.forms import PetForm, EditPetForm, DeletePetForm
from Petstagram.main_app.models import Pet
from Petstagram.main_app.views.others import get_profile


def add_pet(request):
    if request.method == 'POST':
        profile = get_profile()
        form = PetForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = profile
            post.save()
            return redirect('profile_details')

    else:
        form = PetForm()

    context = {
        'form': form,
}

    return render(request, 'pet_create.html', context )


def pet_edit(request, pk):
    pet = Pet.objects.get(id=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditPetForm(instance=pet)

    context = {
        'form': form,
    }
    return render(request, 'pet_edit.html', context)


def pet_delete(request, pk):
    pet = Pet.objects.get(id=pk)
    form = DeletePetForm(instance=pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('home_page')
    context = {
        'form': form,
    }
    return render(request, 'pet_delete.html', context)

#
# def profile_delete(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         profile.delete()
#         return redirect('home_page')
#     context={
#         'full_name': f'{profile.first_name} {profile.last_name}',
#         'picture': profile.picture,
#     }
#     return render(request, 'profile_delete.html', context)
