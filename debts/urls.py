from debts.views.users import user_detail, user_list_create
from debts.views.debts import debt_detail, debt_list_create
from django.urls import path, include

urlpatterns = [
    path('users/', user_list_create, name='user_list_create'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('debts/', debt_list_create, name='debt_list_create'),
    path('debts/<int:pk>/', debt_detail, name='debt_detail'),
]
