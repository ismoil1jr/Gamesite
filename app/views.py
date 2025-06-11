from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category,Contact,Comment

class HomeView(View):
    def get(self, request):
        trending_products = Product.objects.filter(is_trending=True)[:5]
        most_played_products = Product.objects.filter(is_most_played=True).order_by('-play_count')[:6]
        categories = Category.objects.language(request.LANGUAGE_CODE).all()[:5]
        context = {
            'trending_products': trending_products,
            'most_played_products': most_played_products,
            'categories': categories,
        }
        return render(request, 'index.html', context)

class ShopView(View):
    def get(self, request):
        # URL manzilidan filtr parametrini oling (masalan, ?filter=adv)
        filter_param = request.GET.get('filter', '*')
        if filter_param == '*':
            products = Product.objects.all()
        else:
            # Map filter classes to category slugs
            filter_map = {'adv': 'adventure', 'str': 'strategy', 'rac': 'racing'}
            category_slug = filter_map.get(filter_param)
            products = Product.objects.filter(genre__slug=category_slug) if category_slug else Product.objects.all()

        # Pagination
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Filtr havolalari uchun barcha toifalarni oling
        categories = Category.objects.language(request.LANGUAGE_CODE).all()

        context = {
            'products': page_obj,
            'categories': categories,
            'current_filter': filter_param,
        }
        return render(request, 'shop.html', context)

class ContactView(View):
    def get(self, request):
        contact = Contact.objects.all()

        context = {
            'contact': contact
        }
        return render(request, 'contact.html', context)



class ProductDetailsView(DetailView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        related_products = Product.objects.filter(genre=product.genre).exclude(id=product.id)[:5]
        context = {
            'product': product,
            'related_products': related_products
        }
        return render(request, 'product-details.html', context)



