from django.urls import path
from product.views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('get_product/', ProductListAPIView.as_view()),
    path('create_product/', ProductCreateAPIView.as_view()),
    path('change/<int:id>/', ProductRetriveUpdateDestroyAPIView.as_view()),


    path('recom/', SystemOfRecomendation.as_view()),

]