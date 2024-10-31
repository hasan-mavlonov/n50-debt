from debts.views.users import user_detail, user_list_create, authenticated_view, authenticated_super_user, unauthenticated_view
from debts.views.debts import debt_detail, debt_list_create
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('users/', user_list_create, name='user_list_create'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('debts/', debt_list_create, name='debt_list_create'),
    path('debts/<int:pk>/', debt_detail, name='debt_detail'),
    path('authenticated/', authenticated_view, name='authenticated_view'),
    path('authenticated/admin/', authenticated_super_user, name='authenticated_superuser'),
    path('unauthenticated/', unauthenticated_view, name='unauthenticated_view'),
    path('token/', obtain_auth_token, name='obtain_auth_token'),
]
