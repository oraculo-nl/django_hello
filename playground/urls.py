# members/urls.py
from django.urls import path
from . import views
urlpatterns = [
path('', views.hello_form, name='hello-form'),
path('memberstest/nieuw/', views.member_create, name='member-create'),
path('memberstest/succes/', views.member_success, name='member-success'),
path('memberstest/', views.member_list, name='member-list'),
path('plot.png', views.simple_plot, name='plot_png'),
path('chart/', views.chart, name='chart'),
path('transacties/', views.transacties, name='transacties'),
path('upload/', views.upload, name='upload'),
path('grafiek/', views.grafiek, name='grafiek'),

]