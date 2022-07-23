from django.urls import path

from Petstagram.main_app.views import generic
from Petstagram.main_app.views.others import unauthorized
from Petstagram.main_app.views.photos import like_photo
from Petstagram.main_app.views import photos
from Petstagram.main_app.views.profiles import create_profile, profile_delete, profile_edit
from Petstagram.main_app.views import profiles, pets

urlpatterns = [
    path('', generic.HomePageView.as_view(), name='home_page'),
    path('dashboard/', generic.DashboardView.as_view(), name='dashboard'),

    path('profile/', profiles.ProfileDetailsView.as_view(), name='profile_details'),
    path('profile/create/', create_profile, name='create_profile'),
    path('profile/delete/', profile_delete, name='profile_delete'),
    path('profile/edit/', profile_edit, name='profile_edit'),

    path('photo/details/<str:pk>/', photos.PhotoDetailsView.as_view(), name='photo_details'),
    path('photo/like/<str:pk>/', like_photo, name='like_photo'),
    path('photo/edit/<str:pk>/', photos.PhotoEditView.as_view(), name='photo_edit'),
    path('photo/delete/<str:pk>/', photos.PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/add/', photos.AddPhotoView.as_view(), name='add_photo'),

    path('pet/add/', pets.AddPetView.as_view(), name='add_pet'),
    path('pet/delete/<str:pk>/', pets.PetDeleteView.as_view(), name='pet_delete'),
    path('pet/edit/<str:pk>/', pets.PetEditView.as_view(), name='pet_edit'),

    path('unauthorized/', unauthorized, name='unauthorized')
]