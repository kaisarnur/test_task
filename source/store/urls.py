from django.contrib import admin
from django.urls import path
from webapp import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("shop/create/", views.ShopCreateView.as_view(), name="shop_create"),
    path("shop/<int:shop_pk>/", views.ShopDetailView.as_view(), name="shop_detail"),
    path("shop/<int:pk>/edit/", views.ShopUpdateView.as_view(), name="shop_update"),
    path("shop/<int:pk>/delete/", views.ShopDeleteView.as_view(), name="shop_delete"),

]
