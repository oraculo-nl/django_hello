from django.urls import path, include
from budget.views import transacties, upload, grafiek

urlpatterns = [
    path('', upload, name='upload'),
    path('transacties/', transacties, name='transacties'),
    path('grafiek/', grafiek, name='grafiek'),
    path("accounts/", include("django.contrib.auth.urls")),
]