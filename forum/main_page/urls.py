from django.urls import path
from . import views

app_name='main_page'

urlpatterns = [
    path('', views.SubjectsListView.as_view(), name='subjects_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:subject>/', views.subject_detail, name='subject_detail'),
    path('create-subject/', views.subject_create, name='subject_create'),
 ] 