from django.urls import path

from .views import SignUpView , ProfilesView , UserView , UserOwnView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('explore/', ProfilesView.as_view(), name='explore'),
    path('profile/<int:id>', UserView.as_view(), name='profile'),
    path('ownprofile/<int:id>', UserOwnView.as_view(), name='ownprofile'),
]
