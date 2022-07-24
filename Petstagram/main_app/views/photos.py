from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from Petstagram.main_app.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from Petstagram.main_app.models import PetPhoto


class AddPhotoView(generic.CreateView):
    template_name = 'photo_create.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('dashboard')


class PhotoDeleteView(generic.DeleteView):
    template_name = 'photo_delete.html'
    model = PetPhoto
    form_class = PhotoDeleteForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['form'] = PhotoDeleteForm(instance=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.form_valid(form)

    context_object_name = 'photo'

    success_url = reverse_lazy('dashboard')


class PhotoEditView(generic.UpdateView):
    template_name = 'photo_edit.html'
    model = PetPhoto
    form_class = PhotoEditForm
    context_object_name = 'phototo'
    success_url = reverse_lazy('dashboard')


class PhotoDetailsView(generic.DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto
    context_object_name = 'phototo'


def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo_details', pk)
