from django.shortcuts import render, redirect
from .forms import ExpenseForm, SignupForm
from .models import Expense
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request): # home page
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(User_ID=request.user)
        return render(request, "expenses.html", {"expenses":expenses})
    else:
        return render(request, "home.html")


def expenses(request): # expense list
    exps = Expense.objects.filter(User_ID=request.user)
    return render(request, "expenses.html", {"expenses":exps})


def expenseDetail(request, id): # expense details
    exp = Expense.objects.get(id=id)
    return render(request, "expense_detail.html", {"expense":exp})


def add_expense(request): # add an expense
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.User_ID = request.user
            form.save()
            return redirect("expenses")
    else: 
        user_expenses = Expense.objects.filter(User_ID=request.user)
        if user_expenses.exists():
            recent_exp = Expense.objects.filter(User_ID=request.user).order_by("-created_at").first()
        else:
            recent_exp = Expense.objects.filter(User_ID=request.user).order_by("-created_at").first()
        form = ExpenseForm()
        return render(request, "add_expense.html", {"form":form, "recent_exp":recent_exp})


def edit_expense(request, id): # edit expense
    exp = Expense.objects.get(id=id)
    if request.method == "GET":
        form = ExpenseForm(instance=exp)
        return render(request, "edit_expense.html", {"form":form, "expense":exp})
    else:
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect("expenses")
        else:
            form = ExpenseForm(request.POST, instance=exp)
            return render(request, "edit_expense.html", {"form":form, "created_at":exp.created_at, "updated_at":exp.updated_at})

def delete_expense(request, id): # delete expense
    exp = Expense.objects.get(id=id)
    if request.method == "POST":
        exp.delete()
        return redirect("expenses")
    else:
        return render(request, "delete_expense.html", {"expense":exp})
    

def get_categories(request):
    if request.method == "GET":
        categories = list(Expense.objects.filter(User_ID=request.user).values_list("category", flat=True).distinct()) # for unique non-dict and non-tuple single values
        return JsonResponse({"categories":categories})
    else:
        return JsonResponse({"categories":""})


def filter_by_category(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
            category = request.POST.get("category", "")

            if category: # if category found
                filtered_expenses = Expense.objects.filter(User_ID=request.user, category=category)
                filtered_json_expenses = [{"id":expense.id, "amount":str(expense.amount), "category":expense.category, "description":expense.description} for expense in filtered_expenses]
                return JsonResponse({"expenses":filtered_json_expenses})

            else: # if not found
                all_expenses = Expense.objects.filter(User_ID=request.user)
                all_json_expenses = [{"id":expense.id, "amount":str(expense.amount), "category":expense.category, "description":expense.description} for expense in all_expenses]
                return JsonResponse({"expenses":all_json_expenses})
            

def totalSpend(request): # total spendings
    total = sum(list(Expense.objects.filter(User_ID=request.user).values_list("amount", flat=True)))
    categories_total = list(Expense.objects.filter(User_ID=request.user).values("category").annotate(total=Sum("amount")))
    return render(request, "total_spend.html", {"total":total, "categories_total":categories_total})


def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("expenses")
        else:
            err_msg = "Invalid email or password. Please try again."
            return render(request, "login.html", {"error":err_msg})
    else:
        return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect("home")

def Signup(request):
    if request.method == "GET":
        form = SignupForm()
        return render(request, "signup.html", {"form":form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "signup.html", {"form":form})