import self as self
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from Petstagram.main_app.forms import ProfileForm, EditProfileForm
from Petstagram.main_app.models import PetPhoto, Profile, Pet
from Petstagram.main_app.views.others import get_profile


# class ProfileDetailsView(generic.DetailView):
#     model = Profile
#     template_name = 'profile_details.html'
#     context_object_name = 'profile'
#
#     def get_object(self, queryset=None):
#         obj = get_profile()
#         return obj
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profile_images = (PetPhoto.objects.filter(tagged_pets__account=request.user).distinct())
#         context['profile_images'] = profile_images
#         context['total_images'] = len(profile_images)
#         context['total_likes'] = sum(p_pic.likes for p_pic in profile_images)
#         context['pets'] = Pet.objects.filter(user_profile=profile.id)
#         return context


class CreateProfileView(LoginRequiredMixin, generic.CreateView):
    template_name = 'profile_create.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('home_page')

    def dispatch(self, request, *args, **kwargs):
        if Profile.objects.filter(account=self.request.user):
            return redirect('account_detail')
        return super(CreateProfileView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            form.instance.account = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ProfileEditView(generic.UpdateView):
    template_name = 'profile_edit.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('account_detail')


class ProfileDeleteView(generic.DeleteView):
    template_name = 'profile_delete.html'
    model = Profile
    success_url = reverse_lazy('home_page')

    def dispatch(self, request, *args, **kwargs):

        # TODO: To check is profile belong to current user
        # profile = Profile.objects.get(account=request.user)
        # if profile.account != self.request.user:
        #     return redirect('account_detail')
        return super(ProfileDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            form.instance.account = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['full_name'] = f'{self.object.first_name} {self.object.last_name}'
        context['picture'] = self.object.picture
        return self.render_to_response(context)
