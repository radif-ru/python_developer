from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from .forms import GoodsForm
from .models import Goods


class GoodsModelListView(ListView):
    template_name = 'goods_list.html'
    # Группировка запросов для OneToOne
    queryset = Goods.objects.select_related('supplier').all()
    # Группировка запросов для ManyToMany
    # queryset = Goods.objects.prefetch_related('supplier').all()


class GoodsModelFormView(FormView, CreateView):
    template_name = 'good_create.html'
    form_class = GoodsForm
    success_url = reverse_lazy('goods')
