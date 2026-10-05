from django.urls import path
from budget.views import transacties

urlpatterns = [
    path('transacties/', transacties, name='transacties')
]