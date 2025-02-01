from django.urls import path
from .views import inventory_list
from . import views
urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    # path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    # path('item/new/', views.item_new, name='item_new'),
    # path('item/<int:item_id>/edit/', views.item_edit, name='item_edit'),
    # path('item/<int:item_id>/delete/', views.item_delete, name='item_delete'),
    # path('item/<int:item_id>/checkout/', views.item_checkout, name='item_checkout'),
    # path('item/<int:item_id>/checkin/', views.item_checkin, name='item_checkin'),
    # path('item/<int:item_id>/history/', views.item_history, name='item_history'),
    # path('item/<int:item_id>/history/<int:history_id>/', views.history_detail, name='history_detail'),
    # path('item/<int:item_id>/history/<int:history_id>/edit/', views.history_edit, name='history_edit'),
    # path('item/<int:item_id>/history/<int:history_id>/delete/', views.history_delete, name='history_delete'),
]
