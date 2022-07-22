from django.contrib.messages import views
from django.shortcuts import render, redirect
from django.views import generic

from Petstagram.main_app.forms import PetForm, EditPetForm, DeletePetForm
from Petstagram.main_app.models import Pet
from django.urls import reverse_lazy


# def add_pet(request):
#     if request.method == 'POST':
#         profile = get_profile()
#         form = PetForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user_profile = profile
#             post.save()
#             return redirect('profile_details')
#
#     else:
#         form = PetForm()
#
#     context = {
#         'form': form,
# }
#     return render(request, 'pet_create.html', context )

class AddPetView(generic.CreateView):
    template_name = 'pet_create.html'
    form_class = PetForm
    success_url = reverse_lazy('profile_details')


class PetEditView(generic.UpdateView):
    template_name = 'pet_edit.html'
    model = Pet
    form_class = EditPetForm
    success_url = reverse_lazy('profile_details')


# def pet_edit(request, pk):
#     pet = Pet.objects.get(id=pk)
#     if request.method == 'POST':
#         form = EditPetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_details')
#     else:
#         form = EditPetForm(instance=pet)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'pet_edit.html', context)


# def pet_delete(request, pk):
#     pet = Pet.objects.get(id=pk)
#     form = DeletePetForm(instance=pet)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('home_page')
#     context = {
#         'form': form,
#     }
#     return render(request, 'pet_delete.html', context)

class PetDeleteView(generic.DeleteView):
    template_name = 'pet_delete.html'
    model = Pet
    form_class = DeletePetForm
    success_url = reverse_lazy('profile_details')


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
