from django.urls import path
from . import views

urlpatterns = [
    path("add_expense/", views.add_expense, name="add"),
    path("expense_detail/edit_expense/<int:id>", views.edit_expense, name="edit"),
    path("delete_expense/<int:id>", views.delete_expense, name="delete"),
    path("expenses/", views.expenses, name="expenses"),
    path("expenses/logout", views.Logout, name="logout"),
    path("expense_detail/<int:id>", views.expenseDetail, name="details"),
    path("total_spend/", views.totalSpend, name="total"),
    path("get_categories/", views.get_categories, name="get_ctg"),
    path("filter_by_category/", views.filter_by_category, name="filter")
]

