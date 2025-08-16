from django.urls import path, re_path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),                     # Home page
    path('signup/', views.signup, name="signup"),          # Signup page
    path('signup/validate/', views.signup_validate, name="signup_validate"),  # AJAX signup
    path('login/', views.c_login, name="login"),           # Login page
    path('login/validate/', views.login_validate, name="login_validate"),    # AJAX login
    path('logout/', views.c_logout, name="logout"),       # Logout
    path('search/', views.search, name="search"),         # Search page
    re_path(r'^country/(?P<country_name>[\w|\W]+)$', views.get_country_details, name="country_page"),
]
