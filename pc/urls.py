from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addPc),
    path('edit', views.editPc),
    path('del/<int:id>', views.delPc),
    path('<int:id>', views.editPc),
    path('', views.index ),
]
