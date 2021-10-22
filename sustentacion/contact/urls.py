
from django.urls import path
from package import views
from contact.views import Contact

urlpatterns = [
    path('contact/', Contact.as_view(), name="contact"),

]