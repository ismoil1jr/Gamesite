from django.db import transaction
from django.utils.text import slugify
from django.core.files import File
import os
from django.utils import timezone
from .models import Category, Product, Comment, Contact  # Replace 'myapp' with your app name

@transaction.atomic
def populate_data():
    # Clear existing data (optional, comment out if you want to append)
    Category.objects.all().delete()
    Product.objects.all().delete()
    Comment.objects.all().delete()
    Contact.objects.all().delete()

    # Create Categories
    categories = [
        {'name': 'Racing', 'image': 'category_images/racing.jpg'},
        {'name': 'Adventure', 'image': 'category_images/adventure.jpg'},
        {'name': 'Strategy', 'image': 'category_images/strategy.jpg'},
        {'name': 'Action', 'image': 'category_images/action.jpg'},
    ]

    category_objects = {}
    for cat_data in categories:
        category = Category()
        category.set_current_language('en')
        category.translations.name = cat_data['name']
        category.slug = slugify(cat_data['name'])
        # Assign a placeholder image (ensure the file exists or adjust storage)
        if cat_data['image']:
            category.image = cat_data['image']
        category.save()
        category_objects[cat_data['name']] = category

    # Create Products
    products_data = [
        {'title': 'Speed Racer', 'category': 'Racing', 'genre': 'Racing', 'old_price': 49.99, 'new_price': 39.99, 'play_count': 1000, 'is_trending': True, 'game_id': 'game_001'},
        {'title': 'Track Mania', 'category': 'Racing', 'genre': 'Racing', 'old_price': 59.99, 'new_price': 44.99, 'play_count': 800, 'is_trending': False, 'game_id': 'game_002'},
        {'title': 'Race Legends', 'category': 'Racing', 'genre': 'Racing', 'old_price': 39.99, 'new_price': 29.99, 'play_count': 600, 'is_most_played': True, 'game_id': 'game_003'},
        {'title': 'Turbo Drift', 'category': 'Racing', 'genre': 'Racing', 'old_price': 45.99, 'new_price': 35.99, 'play_count': 500, 'is_trending': True, 'game_id': 'game_004'},
        {'title': 'Fast Lane', 'category': 'Racing', 'genre': 'Racing', 'old_price': 55.99, 'new_price': 42.99, 'play_count': 700, 'is_most_played': False, 'game_id': 'game_005'},
        {'title': 'Jungle Quest', 'category': 'Adventure', 'genre': 'Adventure', 'old_price': 69.99, 'new_price': 54.99, 'play_count': 1200, 'is_trending': True, 'game_id': 'game_006'},
        {'title': 'Mystic Journey', 'category': 'Adventure', 'genre': 'Adventure', 'old_price': 59.99, 'new_price': 49.99, 'play_count': 900, 'is_most_played': True, 'game_id': 'game_007'},
        {'title': 'Lost Explorer', 'category': 'Adventure', 'genre': 'Adventure', 'old_price': 49.99, 'new_price': 39.99, 'play_count': 850, 'is_trending': False, 'game_id': 'game_008'},
        {'title': 'Hidden Realm', 'category': 'Adventure', 'genre': 'Adventure', 'old_price': 65.99, 'new_price': 55.99, 'play_count': 950, 'is_most_played': False, 'game_id': 'game_009'},
        {'title': 'Epic Voyage', 'category': 'Adventure', 'genre': 'Adventure', 'old_price': 55.99, 'new_price': 45.99, 'play_count': 1100, 'is_trending': True, 'game_id': 'game_010'},
        {'title': 'War Tactics', 'category': 'Strategy', 'genre': 'Strategy', 'old_price': 59.99, 'new_price': 49.99, 'play_count': 1300, 'is_trending': True, 'game_id': 'game_011'},
        {'title': 'Battle Plan', 'category': 'Strategy', 'genre': 'Strategy', 'old_price': 49.99, 'new_price': 39.99, 'play_count': 1000, 'is_most_played': True, 'game_id': 'game_012'},
        {'title': 'Kingdom Builder', 'category': 'Strategy', 'genre': 'Strategy', 'old_price': 69.99, 'new_price': 59.99, 'play_count': 1100, 'is_trending': False, 'game_id': 'game_013'},
        {'title': 'Chess Wars', 'category': 'Strategy', 'genre': 'Strategy', 'old_price': 39.99, 'new_price': 29.99, 'play_count': 900, 'is_most_played': False, 'game_id': 'game_014'},
        {'title': 'Tactical Strike', 'category': 'Strategy', 'genre': 'Strategy', 'old_price': 55.99, 'new_price': 45.99, 'play_count': 950, 'is_trending': True, 'game_id': 'game_015'},
        {'title': 'Shadow Ops', 'category': 'Action', 'genre': 'Action', 'old_price': 79.99, 'new_price': 69.99, 'play_count': 1500, 'is_trending': True, 'game_id': 'game_016'},
        {'title': 'Blaze Combat', 'category': 'Action', 'genre': 'Action', 'old_price': 59.99, 'new_price': 49.99, 'play_count': 1400, 'is_most_played': True, 'game_id': 'game_017'},
        {'title': 'Urban Assault', 'category': 'Action', 'genre': 'Action', 'old_price': 69.99, 'new_price': 59.99, 'play_count': 1300, 'is_trending': False, 'game_id': 'game_018'},
        {'title': 'Ninja Strike', 'category': 'Action', 'genre': 'Action', 'old_price': 49.99, 'new_price': 39.99, 'play_count': 1200, 'is_most_played': False, 'game_id': 'game_019'},
        {'title': 'Chaos Arena', 'category': 'Action', 'genre': 'Action', 'old_price': 59.99, 'new_price': 49.99, 'play_count': 1100, 'is_trending': True, 'game_id': 'game_020'},
    ]

    for prod_data in products_data:
        product = Product()
        product.set_current_language('en')
        product.translations.title = prod_data['title']
        product.translations.info = f"Info about {prod_data['title']}"
        product.translations.tags = f"{prod_data['category'].lower()},game"
        product.translations.description = f"<p>Explore the thrilling world of {prod_data['title']}!</p>"
        product.image = f"product_images/{prod_data['game_id']}.jpg"
        product.category_type = category_objects[prod_data['category']]
        product.genre = category_objects[prod_data['genre']]
        product.old_price = prod_data['old_price']
        product.new_price = prod_data['new_price']
        product.game_id = prod_data['game_id']
        product.is_trending = prod_data.get('is_trending', False)
        product.is_most_played = prod_data.get('is_most_played', False)
        product.play_count = prod_data['play_count']
        product.save()

    # Create Comments
    comments_data = [
        {'product_game_id': 'game_001', 'text': 'Amazing racing game!'},
        {'product_game_id': 'game_001', 'text': 'Really fun tracks!'},
        {'product_game_id': 'game_006', 'text': 'Epic adventure!'},
        {'product_game_id': 'game_011', 'text': 'Strategic masterpiece!'},
        {'product_game_id': 'game_016', 'text': 'Action-packed fun!'},
    ]

    for comment_data in comments_data:
        comment = Comment()
        comment.set_current_language('en')
        comment.translations.text = comment_data['text']
        comment.product = Product.objects.get(game_id=comment_data['product_game_id'])
        comment.created_at = timezone.now()
        comment.save()

    # Create Contact
    contact = Contact()
    contact.set_current_language('en')
    contact.translations.info = '<p>Contact us for support!</p>'
    contact.translations.address = '123 Game Street, Virtual City'
    contact.phone = '+1234567890'
    contact.email = 'support@gamecompany.com'
    contact.save() 

    print("Data population completed successfully!")

# Run the function (e.g., in Django shell or management command)
if __name__ == '__main__':
    populate_data()