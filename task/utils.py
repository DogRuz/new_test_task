from django.db.models import Q


def validate_parametrs_from_product(params):
    params = dict(
        company_id=params['company_id'],
        category_id=params['category_id'],
        title=(Q(title__iexact=params['title']) | Q(title__icontains=params['title'])) if params.get('title',
                                                                                                     None) != None else Q())
    return params


def validate_for_update_company(params, company):
    return dict(description=params['description'] if params.get('description', None) != None else company.description,
                is_active=params['is_active'] if params.get('is_active', None) != None else company.is_active)


def validate_company_parametrs_from_insert(params):
    try:
        return dict(description=params['description'], is_active=params['is_active'])
    except:
        return Exception


def validate_for_update_category(params, category):
    return dict(title=params['description'] if params.get('title', None) != None else category.title)


def validate_for_update_product(params, product):
    return dict(description=params['description'] if params.get('description', None) != None else product.description,
                is_active=params['is_active'] if params.get('is_active', None) != None else product.is_active,
                title=params['title'] if params.get('title', None) != None else product.title,
                category_id=params['category_id'] if params.get('category_id', None) != None else product.category_id,
                company_id=params['company_id'] if params.get('company_id', None) != None else product.company_id)


def validate_product_parametrs_from_insert(params):
    try:
        return dict(description=params.get('description', None), is_active=params.get('is_active', False),
                    title=params.get('title', None),
                    category_id=params.get('category_id', None), company_id=params.get('company_id', None))
    except:
        return Exception
