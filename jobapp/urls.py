from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path("login/", views.loginpage, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("post/", views.post, name="post"),
    path('detail/<int:pk>/', views.post_details, name='detail'),
    path("post/<int:pk>/edit/", views.edit_post, name="post_edit"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("create_post/", views.create_post, name="create_post"),
    path("create/", views.create_profile, name="create"),
    path('profile_detail/<int:pk>/', views.profile_detail, name='profile_detail'),
    path("profile/<int:pk>/edit/", views.profile_edit, name="profile_edit"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)