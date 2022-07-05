from .models import Category


def menu_categories(request):
    categories = Category.objects.filter(CATParent=None)

    return {'menu_categories': categories}
