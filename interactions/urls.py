from django.urls import path
from . import views

app_name = 'interactions'

urlpatterns = [
    path('like/<str:content_type>/<int:obj_id>/', views.ToggleLikeView.as_view(), name='toggle_like')
]