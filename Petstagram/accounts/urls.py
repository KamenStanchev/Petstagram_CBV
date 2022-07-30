from django.urls import path

from Petstagram.accounts.views import create_accout, login_page, account_details, edit_profile, edit_password, logout_page

urlpatterns = [
    path('create-profile/', create_accout, name='create_account'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('profile/<int:pk>/', account_details, name='account_detail'),
    path('edit-profile/<int:pk>/', edit_profile, name='edit_account'),
    path('edit-password/<int:pk>/', edit_password, name='edit_password'),

]
