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
]
