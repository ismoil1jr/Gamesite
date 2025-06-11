from django.contrib import admin
from .models import Category, Product, Comment,Contact
from parler.admin import TranslatableAdmin



@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('__str__', 'image')

@admin.register(Comment)
class CommentAdmin(TranslatableAdmin):
    list_display = ('product', '__str__', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('translations__text', 'product__translations__title')

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('__str__', 'category_type', 'genre', 'new_price', 'game_id', 'is_trending', 'is_most_played', 'play_count')
    list_filter = ('category_type', 'genre', 'is_trending', 'is_most_played')
    search_fields = ('translations__title', 'game_id')
    list_editable = ('is_trending', 'is_most_played', 'play_count')
    ordering = ['-play_count']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('category_type', 'genre')


@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('__str__', 'phone', 'email')
    search_fields = ('translations__info', 'translations__address', 'phone', 'email')
