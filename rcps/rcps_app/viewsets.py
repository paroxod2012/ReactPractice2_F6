from rest_framework import viewsets

from .models import *
from .serializers import *

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = self.queryset
        category_id = self.request.query_params.get('category')
        if category_id is not None:
            try:
                category = Categories.objects.get(id=category_id)
                queryset = queryset.filter(category=category)
            except Categories.DoesNotExist:
                pass

        return queryset

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer