# mysite/urls.py
from django.contrib import admin
from django.urls import path
from charts.views import simple_plot_png, chart

urlpatterns = [
    path('plot.png', simple_plot_png , name='plot_png '),
    path('chart/', chart , name='chart ')
]