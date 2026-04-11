from django.urls import path
from . import views

urlpatterns = [
    path('like/<str:content_type>/<int:obj_id>/', views.ToggleLikeView.as_view, name='toggle_like')
]