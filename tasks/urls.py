from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', index, name='home'),
    path('<int:user_id>/', your_tasks, name='your_tasks'),
    path('<int:user_id>/<int:pk_id>/', post, name='poster'),
    path('get_money/', get_money, name='get_money'),
    path('add_task/', add_task, name='add_task'),
    path('delete_task/', delete_task, name='delete_task'),
    path('delete_task/<int:pk_delete>/', delete_task_pk, name='delete_task_pk'),
    path('market/', market, name='market'),
    path('market/<int:market_pk>/', market_buy, name='market_buy'),
    path('market/add_market/', add_market, name='add_market'),
    path('market/delete_market/', market_delete, name='market_delete'),
    path('market/delete_market/<int:delete_pk_market>/', market_delete_pk, name='market_delete_pk'),

]
