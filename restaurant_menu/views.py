from django.shortcuts import render

# Create your views here.
# Class Based View

from django.views import generic
from .models import Items, MEAL_TYPE
from django.views.generic import TemplateView

class MenuList(generic.ListView):

    queryset = Items.objects.order_by("-date_create")
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):

    model = Items
    template_name = "menu_item_list.html"

class About(TemplateView):

    template_name = "about.html"