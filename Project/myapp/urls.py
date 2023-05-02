from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('seller-index',views.seller_index,name='seller-index'),
    path('signout/',views.signout,name='signout'),
    path('change-password/',views.change_password,name='change-password'),
    #path('seller-change-password/',views.seller_change_password,name='seller-change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password',views.new_password,name='new-password'),
    path('profile',views.profile,name='profile'),
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>',views.seller_product_details,name='seller-product-details'),
    path('seller-edit-product/<int:pk>',views.seller_edit_product,name='seller-edit-product'),
    path('seller-delete-product/<int:pk>',views.seller_delete_product,name='seller-delete-product'),
    path('product-details/<int:pk>',views.product_details,name='product-details'),
    path('add-to-wishlist/<int:pk>',views.add_to_wishlist,name='add-to-wishlist'),
]
