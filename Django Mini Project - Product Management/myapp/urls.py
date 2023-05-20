from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('product_manager',views.product_manager,name='product_manager'),
    path('search',views.search,name='search'),
]