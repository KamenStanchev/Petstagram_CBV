from django.shortcuts import render, redirect
from django.views import generic

from Petstagram.main_app.forms import ProfileForm, EditProfileForm
from Petstagram.main_app.models import PetPhoto, Profile, Pet
from Petstagram.main_app.views.others import get_profile


# def profile_details(request):
#     profile = get_profile()
#
#     profile_images = (PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
#     total_images = len(profile_images)
#     total_likes = sum(p_pic.likes for p_pic in profile_images)
#     context = {
#         'profile': profile,
#         'total_images': total_images,
#         'total_likes': total_likes,
#         'pets': Pet.objects.filter(user_profile=profile.id),
#     }
#     return render(request, 'profile_details.html', context)

class ProfileDetailsView(generic.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        obj = get_profile()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        profile_images = (PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
        context['profile_images'] = profile_images
        context['total_images'] = len(profile_images)
        context['total_likes'] = sum(p_pic.likes for p_pic in profile_images)
        context['pets'] = Pet.objects.filter(user_profile=profile.id)
        return context


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile_edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        return redirect('home_page')
    context = {
        'full_name': f'{profile.first_name} {profile.last_name}',
        'picture': profile.picture,
    }
    return render(request, 'profile_delete.html', context)
