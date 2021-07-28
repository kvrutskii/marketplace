from django.contrib import admin
from django.urls import path
from .views import main, product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('<int:product_id>/', product_detail, name='product_detail')

]