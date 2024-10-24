from django.urls import path, include
from django.contrib import admin  # Import 'admin' here
from . import views  # Import views from the current package (sudoku)

urlpatterns = [
    path('', views.home, name='home'),  # Define your home view
    path('solve/', views.solve_sudoku, name='solve_sudoku'),  # Add other views as needed
    # Add other paths as necessary
]