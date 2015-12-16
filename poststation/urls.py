import views
from django.conf.urls import url

urlpatterns = [
    url('^list[/]$',views.list,name="list"),
]