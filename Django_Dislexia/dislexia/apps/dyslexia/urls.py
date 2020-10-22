from django.urls import path
from apps.dyslexia import views
urlpatterns=[
    path('especialista/', views.GetEspecialistas),
    path('especialista/<int:key>/', views.Especialistas),
    path('save_e/', views.SaveEspecialistas),
    path('niño/', views.GetNiños),
    path('niño/<int:key>/', views.Niños),
    path('save_n/', views.SaveNiños),
    path('diagnostico/', views.GetDiagnosticos),
    path('diagnostico/<int:key>/', views.Diagnosticos),
    path('save_d/', views.SaveDiagnosticos)
    
]   