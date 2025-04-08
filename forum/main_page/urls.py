from django.urls import path
from . import views

app_name='main_page'

urlpatterns = [
    path('subject/', views.SubjectsListView.as_view(), name='subjects_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:subject>/', views.subject_detail, name='subject_detail'),
    path('create-subject/', views.subject_create, name='subject_create'),
    path('search/', views.subject_search, name='subject_search'),
    path('profile/<int:user_id>/', views.my_view, name='profile'),
    path('delete_subject/<int:subject_id>/', views.delete_subject, name='delete_subject')
 ] 