from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter # generate urls by default(register)

router=DefaultRouter()
router.register('api/products',views.ProductViewsetView,basename='products')
router.register('api/users',views.UserViewsetView,basename='users')
# router.register('cart',views.CartView,basename='cart')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('carts/<int:id>/',views.CartView.as_view()),
    # path('products/<int:id>/', views.ProductDetailsView.as_view()),
] + router.urls
