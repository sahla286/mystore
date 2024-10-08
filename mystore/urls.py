from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter # generate urls by default(register)

router=DefaultRouter()
router.register('api/products',views.ProductViewsetView,basename='products')
router.register('api/users',views.UserViewsetView,basename='users')
router.register('cart',views.CartView,basename='cart')
# router.register('review',views.ReviewView,basename='review')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products/<int:id>/', views.ProductDetailsView.as_view()),
    path('review/<int:id>/', views.ReviewView.as_view()),

] + router.urls
