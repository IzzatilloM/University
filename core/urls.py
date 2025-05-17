from django.contrib import admin
from django.urls import path

from univer.views import home_view, yunalish_view, ustozlar_view, fanlar_view, yunalish_confirm_delete_view, yunalish_delete_view, fanlar_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('yunalish/',yunalish_view),
    path('yunalish/<int:pk>/confirm-delete/', yunalish_confirm_delete_view),
    path('yunalish/<int:pk>/delete/', yunalish_delete_view),
    path('ustozlar/',ustozlar_view),
    path('fanlar/',fanlar_view),
    path('fanlar/<int:pk>/delete/', fanlar_delete_view),

]
