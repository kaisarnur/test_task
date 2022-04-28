from django.contrib import admin
from django.urls import path
from webapp.views import store_views, good_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", store_views.IndexView.as_view(), name="index"),
    path("shop/create/", store_views.ShopCreateView.as_view(), name="shop_create"),
    path("shop/<int:shop_pk>/", store_views.ShopDetailView.as_view(), name="shop_detail"),
    path("shop/<int:pk>/edit/", store_views.ShopUpdateView.as_view(), name="shop_update"),
    path("shop/<int:pk>/delete/", store_views.ShopDeleteView.as_view(), name="shop_delete"),
    path("good/new/<int:shop_pk>/", good_views.GoodCreateView.as_view(), name="good_form"),
    path("good/<int:good_pk>/", good_views.GoodView.as_view(), name="good_detail"),
    path("good/<int:pk>/edit/", good_views.GoodUpdateView.as_view(), name="good_update"),
    path("good/<int:pk>/delete/", good_views.GoodDeleteView.as_view(), name="good_delete")
]
