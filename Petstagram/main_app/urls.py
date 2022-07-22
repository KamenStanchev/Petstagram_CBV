from django.urls import path

from Petstagram.main_app.views.generic import home_page, dashboard
from Petstagram.main_app.views.others import unauthorized
from Petstagram.main_app.views.pets import add_pet, pet_delete, pet_edit
from Petstagram.main_app.views.photos import photo_details, like_photo, photo_edit, add_photo, photo_delete
from Petstagram.main_app.views.profiles import profile_details, create_profile, profile_delete, profile_edit

urlpatterns = [
    path('', home_page, name='home_page'),
    path('dashboard/', dashboard, name='dashboard'),

    path('profile/', profile_details, name='profile_details'),
    path('profile/create/', create_profile, name='create_profile'),
    path('profile/delete/', profile_delete, name='profile_delete'),
    path('profile/edit/', profile_edit, name='profile_edit'),

    path('photo/details/<str:pk>/', photo_details, name='photo_details'),
    path('photo/like/<str:pk>/', like_photo, name='like_photo'),
    path('photo/edit/<str:pk>/', photo_edit, name='photo_edit'),
    path('photo/delete/<str:pk>/', photo_delete, name='photo_delete'),
    path('photo/add/', add_photo, name='add_photo'),

    path('pet/add/', add_pet, name='add_pet'),
    path('pet/delete/<str:pk>/', pet_delete, name='pet_delete'),
    path('pet/edit/<str:pk>/', pet_edit, name='pet_edit'),

    path('unauthorized/', unauthorized, name='unauthorized')
]