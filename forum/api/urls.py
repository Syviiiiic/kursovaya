from django.urls import path
from . import views

app_name='api'

urlpatterns = [
    path('subjectlist/', views.SubjectViewSet.as_view()),
 ] 