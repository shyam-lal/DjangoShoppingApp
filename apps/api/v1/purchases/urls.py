from django.urls import path
from api.v1.purchases import views

app_name = 'purchases'

urlpatterns = [
   # path('<slug>',views.cart_api_view,name = "create-cart-api"),
    path('purchase/<slug>/',views.cart_purchase_api,name='cart-purchase-api'),
]