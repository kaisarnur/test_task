from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from webapp.models import Shop, Good, Category
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.forms import ShopForm


class IndexView(ListView):
    model = Shop
    context_object_name = "shops"
    template_name = "index.html"
    ordering = ["-created_at"]
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.get_filter_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        query = {}
        if self.filter:
            query["filter"] = self.filter
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.filter:
            print(self.filter)
            queryset = queryset.filter(category__category=self.filter)
        return queryset

    def get_filter_value(self):
        self.filter = self.request.GET.get("filter")


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = "create.html"

    def get_success_url(self):
        return reverse("shop_detail", kwargs={"shop_pk": self.object.pk})


class ShopDetailView(DetailView):
    model = Shop
    context_object_name = "shop"
    template_name = "detail.html"
    pk_url_kwarg = "shop_pk"


class ShopUpdateView(UpdateView):
    model = Shop
    template_name = "update.html"
    form_class = ShopForm
    context_object_name = "shop"

    def get_success_url(self):
        return reverse("shop_detail", kwargs={"shop_pk": self.object.pk})


class ShopDeleteView(DeleteView):
    model = Shop
    template_name = "delete.html"
    success_url = reverse_lazy("index")
    context_object_name = "shop"
