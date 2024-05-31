# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('render_graph/', views.render_graph, name='render_graph'),
    # Add other URLs as needed
]
