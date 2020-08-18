from django.urls import path
from . import views
from .views import IndexView, InstanceView, AddPostView, EditPost, SearchView

urlpatterns = [
    # path('', views.index, name="index")
    path('', IndexView.as_view(), name="index"),
    path('instance/<int:pk>', views.detail, name="instance"),
    path('create_post/', AddPostView.as_view(), name="create_post"),
    path('instance/edit/<int:pk>', EditPost.as_view(), name="edit_post"),
    path('search/', SearchView.as_view(), name="search"),
    path('autocomplete/', views.autocomplete, name='autocomplete')
]
