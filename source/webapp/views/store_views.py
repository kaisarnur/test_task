from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from webapp.models import Shop, Good
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from webapp.forms import ShopForm


class IndexView(ListView):
    model = Shop
    context_object_name = "shops"
    template_name = "shop/index.html"
    ordering = ["-created_at"]
    paginate_by = 5


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = "shop/create.html"

    def get_success_url(self):
        return reverse("shop_detail", kwargs={"shop_pk": self.object.pk})


class ShopDetailView(ListView):
    model = Good
    context_object_name = "goods"
    template_name = "shop/detail.html"
    ordering = ["-created_at"]
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["shop"] = self.shop
        return context

    def get_queryset(self):
        self.shop = get_object_or_404(Shop, pk=self.kwargs["shop_pk"])
        queryset = super().get_queryset().filter(shop=self.shop)
        return queryset


class ShopUpdateView(UpdateView):
    model = Shop
    template_name = "shop/update.html"
    form_class = ShopForm
    context_object_name = "shop"

    def get_success_url(self):
        return reverse("shop_detail", kwargs={"shop_pk": self.object.pk})


class ShopDeleteView(DeleteView):
    model = Shop
    template_name = "shop/delete.html"
    success_url = reverse_lazy("index")
    context_object_name = "shop"
