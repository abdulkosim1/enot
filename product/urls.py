from django.urls import path, include
from product.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comment', CommentModelViewSet)

urlpatterns = [
    path('get_product/', ProductListAPIView.as_view()),
    path('create_product/', ProductCreateAPIView.as_view()),
    path('change/<int:id>/', ProductRetriveUpdateDestroyAPIView.as_view()),
    path('recom/', SystemOfRecomendation.as_view()),
    # path('<int:pk>/like/', AddLike.as_view()),
    path('<int:pk>/rating/', AddRating.as_view()),
    # path('favorite/', FavoriteModelViewSet.as_view({'post':'create'})),
    path('', include(router.urls)),

]
