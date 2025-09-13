import django_filters
from expense.models import Expense

class ExpenseFilter(django_filters.FilterSet):
    # category = django_filters.ChoiceFilter()
    class Meta:
        model = Expense
        fields = ['category']