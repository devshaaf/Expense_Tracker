from django.urls import path
from . import views

urlpatterns = [
    path("expenses/", views.Expenses),
    path("expense/<int:pk>/", views.ExpenseDetail),
    path("expenses/summary/", views.TotalSpend)
]
