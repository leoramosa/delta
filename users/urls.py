""" Users Urls. """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='feed/',
        view=views.Feed.as_view(),
        name='feed'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),

    # Detail Profile private
    path(
        route='account/<str:username>/',
        view=views.UserDetailInterView.as_view(),
        name='detailinter',
    ),
]
