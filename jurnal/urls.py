from django.urls import path
from .views import home_page, create_jurnal, update_jurnal, delete_jurnal

urlpatterns = [
  path('home/', home_page, name='home'),
  path('create/', create_jurnal, name='create'),
  path('update/<int:id>', update_jurnal, name='update'),
  path('delete/<int:id>', delete_jurnal, name='delete')
]
