from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from .forms import GoodsForm
from .models import Goods


class GoodsModelListView(ListView):
    template_name = 'goods_app/index.html'
    queryset = Goods.objects.all()


class GoodsModelFormView(FormView, CreateView):
    template_name = 'goods_app/create_good.html'
    form_class = GoodsForm
    success_url = reverse_lazy('goods')
