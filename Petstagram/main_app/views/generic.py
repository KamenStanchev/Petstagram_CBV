from django.views import generic

from Petstagram.main_app.models import PetPhoto


# def home_page(request):
#     context = {
#         'hide_additional_nav_item': True,
#     }
#     return render(request, 'home_page.html', context)

class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hide_additional_nav_item'] = True
        return context


# def dashboard(request):
#     # profile = get_profile()
#     # pets = profile.pet_set.all()
#     pet_photos = PetPhoto.objects.all()
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'dashboard.html', context)


class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    model = PetPhoto
    context_object_name = 'pet_photos'


