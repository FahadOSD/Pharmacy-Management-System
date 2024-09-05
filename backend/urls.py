from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from accounts import views as accounts_views
from user_role import views as user_role_views
from drug import views as drug_views
from stock import views as stock_views
from cart import views as cart_views
from orders import views as orders_views

router = DefaultRouter()
router.register(r'accounts', accounts_views.AccountsViewSet, basename='accounts')
router.register(r'user_role', user_role_views.UserRoleViewSet, basename='user_role')
router.register(r'drug', drug_views.DrugViewSet, basename='drug')
router.register(r'stock', stock_views.StockViewSet, basename='stock')
router.register(r'cart', cart_views.CartViewSet, basename='cart')
router.register(r'cart_item', cart_views.CartItemView, basename='cart_item')
router.register(r'orders', orders_views.OrderViewSet, basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]