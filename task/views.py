from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import status
from task.models import Category, Company, Product
from task.utils import validate_parametrs_from_product, validate_for_update_company, \
    validate_company_parametrs_from_insert, validate_for_update_product, validate_product_parametrs_from_insert


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_list_categories(request):
    """
    Контроллер для получения категорий
    """
    return Response(Category.objects.all().values('id', 'title'), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_list_active_company(request):
    """
    Контроллер для получения активных компаний
    """
    return Response(Company.objects.filter(is_active=True).values('id', 'description'), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_list_active_product(request):
    """
    Контроллер для получения активных продуктов по компаниям и категориям
    """
    try:
        params = validate_parametrs_from_product(request.GET)
    except Exception:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    return Response(Product.objects.filter(is_active=True, company_id=params['company_id'],
                                           category_id=params['category_id']).filter(params['title']).values('id',
                                                                                                             'title'),
                    status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_product_detail_card(request, pk):
    """
    Контроллер для получения детальной карточки продукта
    """
    try:
        id_product = int(pk)
    except Exception:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    return Response(Product.objects.filter(id=id_product).values('id', 'description', 'title', 'category__title',
                                                                 'company__description', 'is_active'),
                    status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
def changes_company(request, pk):
    """
    Контроллер для изменения и удаления компании
    """
    try:
        company = Company.objects.get(pk=pk)
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        params = validate_for_update_company(request.POST, company)
        company.description = params['description']
        company.is_active = params['is_active']
        company.save()
        return Response('Update id={}'.format(pk), status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        Product.objects.filter(company_id=pk).delete()
        company.delete()
        return Response('Delete id={}'.format(pk), status=status.HTTP_200_OK)


@api_view(['POST'])
def insert_company(request):
    """
    Контроллер для добавления компании
    """
    try:
        new_company = validate_company_parametrs_from_insert(request.POST)
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    new_company_insert, create = Company.objects.get_or_create(*new_company)
    status_company = 'Insert id={}'.format(new_company_insert.id) if create else 'Get id={}'.format(
        new_company_insert.id)
    return Response(status_company, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
def changes_category(request, pk):
    """
    Контроллер для изменения категории
    """
    try:
        category = Category.objects.get(pk=pk)
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        params = validate_for_update_company(request.POST, category)
        category.title = params['title']
        category.save()
        return Response('Update id={}'.format(pk), status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        Product.objects.filter(category_id=pk).delete()
        category.delete()
        return Response('Delete id={}'.format(pk), status=status.HTTP_200_OK)


@api_view(['POST'])
def insert_category(request):
    """
    Контроллер для добавления категории
    """
    try:
        new_category = request.POST['title']
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    new_category_insert, create = Category.objects.get_or_create(title=new_category)
    status_company = 'Insert id={}'.format(new_category_insert.id) if create else 'Get id={}'.format(
        new_category_insert.id)
    return Response(status_company, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
def changes_product(request, pk):
    """
    Контроллер для изменеия или удаления продукта
    """
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        params = validate_for_update_product(request.POST, product)
        product.description = params['description']
        product.is_active = params['is_active']
        product.title = params['title']
        product.company_id = params['company_id']
        product.category_id = params['category_id']
        product.save()
        return Response('Update id={}'.format(pk), status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response('Delete id={}'.format(pk), status=status.HTTP_200_OK)


@api_view(['POST'])
def insert_product(request):
    """
    Контроллер для добавления продукта
    """
    try:
        new_product = validate_product_parametrs_from_insert(request.POST)
    except:
        return Response('incorrect request params', status=status.HTTP_400_BAD_REQUEST)
    new_product_insert, create = Product.objects.get_or_create(**new_product)
    status_company = 'Insert id={}'.format(new_product_insert.id) if create else 'Get id={}'.format(
        new_product_insert.id)
    return Response(status_company, status=status.HTTP_200_OK)
