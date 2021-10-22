from package.views import PackageListView,PackageDetailView, PackageCreate, PackageUpdate, PackageDelete
from django.urls import path
from package import views




urlpatterns = [
    path('', PackageListView.as_view(), name="package"),
    path('<int:pk>/', PackageDetailView.as_view(), name='pack'),
    path('create/', PackageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PackageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PackageDelete.as_view(), name='delete'),

]