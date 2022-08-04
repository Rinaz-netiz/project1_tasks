from django.shortcuts import render, redirect
from .forms import TaskDid, NewTask, BuyMarket, AddMarket, UserCreationForm, UserLoginForm
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except Exception:
                return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('your_tasks', request.user.pk)
    else:
        form = UserLoginForm()
    return render(request, 'tasks/login.html', {'form': form})


def how_money():
    moneys = 0
    for i in Task.objects.filter(done=True, account_task_id=id_object):
        moneys += i.money
    for buy in Market.objects.filter(buy=True, account_market_id=id_object):
        moneys -= buy.price
    return moneys


# base
def your_tasks(request, user_id):
    global id_object
    id_object = user_id

    tasks = Task.objects.filter(done=False, account_task_id=user_id).order_by('-date_add')
    return render(request, 'tasks/index.html', {'tasks': tasks, 'money': how_money})


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('register')
    else:
        return redirect('your_tasks', request.user.pk)
    #tasks = Task.objects.filter(done=False).order_by('-date_add')
    #return render(request, 'tasks/index.html', {'tasks': tasks, 'money': how_money})


def post(request, pk_id, user_id):
    if request.method == 'POST':
        tas = Task.objects.get(pk=pk_id)
        tas.done = True
        tas.save()
        return redirect('home')


def get_money(request):
    tasks = Task.objects.filter(done=True, account_task_id=id_object)
    market2 = Market.objects.filter(buy=True, account_market_id=id_object)
    if request.method == 'POST':
        if how_money() == 0:
            for i in tasks:
                i.delete()
            for m in market2:
                m.delete()
            return redirect('home')
    return render(request, 'tasks/get_money.html', {'tasks': tasks, 'money': how_money, 'market': market2})


def add_task(request):
    if request.method == 'POST':
        form = NewTask(request.POST)
        #print(form)
        if form.is_valid():
            try:
                user = User.objects.get(id=id_object)
                task2 = Task(
                    task=form.cleaned_data['task'],
                    date_add=form.cleaned_data['date_add'],
                    money=form.cleaned_data['money'],
                    account_task_id=user
                )
                task2.save()
            except Exception as ex:
                print(ex)
            else:
                return redirect('home')
    else:
        form = NewTask()

    return render(request, 'tasks/add_form.html', {'form': form, 'money': how_money})


def delete_task(request):
    tasks = Task.objects.filter(done=False, account_task_id=id_object).order_by('-date_add')
    return render(request, 'tasks/delete_task.html', {'tasks': tasks, 'money': how_money})


def delete_task_pk(request, pk_delete):
    if request.method == 'POST':
        form = TaskDid(request.POST)
        if form.is_valid():
            tas = Task.objects.get(pk=pk_delete)
            tas.delete()
            return redirect('home')


def market(request):
    market_task = Market.objects.filter(buy=False, account_market_id=id_object)
    return render(request, 'tasks/market.html', {'market': market_task, 'money': how_money})


def market_buy(request, market_pk):
    if request.method == 'POST':
        mar = Market.objects.get(pk=market_pk)
        if mar.price > how_money():
            return redirect('market')
        mar.buy = True
        mar.save()
        return redirect('home')


def add_market(request):
    if request.method == 'POST':
        form = AddMarket(request.POST)
        if form.is_valid():
            #print(form)
            user = User.objects.get(id=id_object)
            market_add = Market(
                text=form.cleaned_data['text'],
                price=form.cleaned_data['price'],
                account_market_id=user
            )
            market_add.save()
            return redirect('market')
    else:
        form = AddMarket()
    return render(request, 'tasks/add_market.html', {'form': form, 'money': how_money})


def market_delete(request):
    market_task = Market.objects.filter(buy=False, account_market_id=id_object)
    return render(request, 'tasks/delete_market.html', {'market': market_task, 'money': how_money})


def market_delete_pk(request, delete_pk_market):
    if request.method == 'POST':
        product_delete = Market.objects.get(pk=delete_pk_market)
        product_delete.delete()
        return redirect('market')
