from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def test_context(request):
    context = {
        'title': 'store',
        'header': 'Welcome!',
        'username': "Ivan Ivanov",
        'products': [
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 234000},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 234000},
        ]
    }
    return render(request, 'products/test-context.html', context)
