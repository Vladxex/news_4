from django.urls import path
from .views import News, NewDetail, NewCreateView, NewDeleteView, NewUpdateView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем новостям у нас останется пустым, позже станет ясно почему
    path('', News.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewDetail.as_view(), name='new_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('add/', NewCreateView.as_view(), name='new_create'),  # Ссылка на create new
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),  # Ссылка на delete new
    path('<int:pk>/edit/', NewUpdateView.as_view(), name='new_update'),  # Ссылка на update new

]