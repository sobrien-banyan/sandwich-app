from django.urls import path
# from sandwich_app.views import SandwichappView, IngredientsView
from sandwich_app.views import SandwichappView, IngredientsView

urlpatterns = [
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredient_type'),
]