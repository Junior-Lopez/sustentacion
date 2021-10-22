from blog.views import *
from django.urls import path
from blog import views


urlpatterns = [
    path('blog/', BlogList.as_view(), name="blog"),
    path('<int:pk>/', BlogDetail.as_view(), name='category'),
]