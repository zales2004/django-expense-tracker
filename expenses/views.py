from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense


# ----------------------------
# Home View (Landing Page)
# ----------------------------
@login_required
def home(request):
    return render(request, 'home.html')


# ----------------------------
# Register View
# ----------------------------
def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request, user)
        return redirect('dashboard')

    return render(request, 'register.html')


# ----------------------------
# Dashboard View
# (Add + List + Filter + Total)
# ----------------------------
@login_required
def dashboard(request):

    # Add Expense
    if request.method == 'POST':
        Expense.objects.create(
            user=request.user,
            title=request.POST['title'],
            amount=request.POST['amount'],
            category=request.POST['category'],
            date=request.POST['date']
        )

    # Filtering
    selected_category = request.GET.get('category')
    expenses = Expense.objects.filter(user=request.user)

    if selected_category and selected_category != 'All':
        expenses = expenses.filter(category=selected_category)

    # Total Expense
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0

    # Categories for dropdown
    categories = ['All', 'Food', 'Travel', 'Rent', 'Shopping', 'Bills', 'Other']

    return render(
        request,
        'dashboard.html',
        {
            'expenses': expenses,
            'total_expense': total_expense,
            'categories': categories,
            'selected_category': selected_category
        }
    )


# ----------------------------
# Delete Expense View
# ----------------------------
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )
    expense.delete()
    return redirect('dashboard')


# ----------------------------
# Update Expense View
# ----------------------------
@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        return redirect('dashboard')

    return render(request, 'update_expense.html', {'expense': expense})
