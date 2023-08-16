from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name= "entry"),
    path("search/",views.search, name= "search"),
    path("new/",views.new_page, name= "new_page"),
    path("edit_content/",views.edit_content, name= "edit_content"),
    path("save_edit/",views.save_edit, name= "save_edit"),
    path("rand/",views.rand, name= "rand")
]
