# from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, \
    DeleteView  # импортируем класс получения деталей объекта
from .models import New
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.shortcuts import render
from .filters import NewFilter
from .forms import NewForm


class News(ListView):
    paginate_by = 10  # поставим постраничный вывод в ten elements
    model = New
    template_name = 'new_list.html'
    context_object_name = 'news'
    ordering = ['-auto_time']

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


# создаём представление в котором будет детали конкретного отдельного товара
class NewDetail(DetailView):
    template_name = 'simpleapp/new_detail.html'
    queryset = New.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class NewCreateView(CreateView):
    template_name = 'simpleapp/new_create.html'
    form_class = NewForm


# дженерик для редактирования объекта
class NewUpdateView(UpdateView):
    template_name = 'simpleapp/new_create.html'
    form_class = NewForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


# дженерик для удаления товара
class NewDeleteView(DeleteView):
    template_name = 'simpleapp/new_delete.html'
    queryset = New.objects.all()
    success_url = '/news/'
