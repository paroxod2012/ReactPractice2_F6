from rest_framework import routers
from .viewsets import RecipeViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipe')
router.register('api/categories', CategoriesViewSet, 'categories')

urlpatterns = router.urls