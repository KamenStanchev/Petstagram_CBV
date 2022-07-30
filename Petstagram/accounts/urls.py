from django.urls import path

from Petstagram.accounts.views import create_account, login_page, account_details, edit_account, edit_password, logout_page

urlpatterns = [
    path('create-profile/', create_account, name='create_account'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('account-details/', account_details, name='account_detail'),
    path('edit-account/', edit_account, name='edit_account'),
    path('edit-password/', edit_password, name='edit_password'),

]
