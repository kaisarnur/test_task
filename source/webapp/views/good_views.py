from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView

from webapp.models import Shop, Good
from webapp.forms import GoodForm


class GoodCreateView(FormView):
    template_name = "good/create.html"
    form_class = GoodForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["shop_pk"] = self.kwargs.get('shop_pk')
        return context

    def form_valid(self, form):
        shop = get_object_or_404(Shop, pk=self.kwargs.get('shop_pk'))
        self.good = form.save(commit=False)
        self.good.shop = shop
        self.good.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("good_detail", kwargs={"good_pk": self.good.pk})


class GoodView(TemplateView):
    template_name = "good/detail.html"

    def get_context_data(self, **kwargs):
        kwargs["good"] = get_object_or_404(Good, pk=kwargs["good_pk"])
        return super().get_context_data(**kwargs)


class GoodUpdateView(UpdateView):
    model = Good
    template_name = "good/update.html"
    form_class = GoodForm
    context_object_name = "good"

    def get_success_url(self):
        return reverse("index")


class GoodDeleteView(DeleteView):
    model = Good
    template_name = "good/delete.html"
    success_url = reverse_lazy("index")
    context_object_name = "good"
