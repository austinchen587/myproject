from django.urls import path
from .views import candidate_list, add_candidate, update_candidate, delete_candidate, hr_analysis_view

app_name = 'hr'  # 为应用指定 app_name

urlpatterns = [
    path('hr/candidates/', candidate_list, name='candidate_list'),
    path('hr/candidates/add/', add_candidate, name='add_candidate'),
    path('candidates/update/<int:id>/', update_candidate, name='update_candidate'),
    path('candidates/delete/<int:id>/', delete_candidate, name='delete_candidate'),
    path('hr/analysis/', hr_analysis_view, name='hr_analysis'),

]