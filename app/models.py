from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel,TranslatedFields
from parler.managers import TranslatableManager
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext_lazy as _
import os

class Category(TranslatableModel):
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=100),
        )
    slug = models.SlugField(unique=True, blank=True, null=True)

    @property
    def imageURL(self):
        if self.image and self.image.storage.exists(self.image.name):
            return self.image.url
        return ''

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.safe_translation_getter('name', any_language=True)
            if name:
                base_slug = slugify(name)
                self.slug = base_slug
                counter = 1
                current_language = self.get_current_language()
                while Category.objects.language(current_language).filter(slug=self.slug).exists():
                    self.slug = f"{base_slug}-{counter}"
                    counter += 1
        super().save(*args, **kwargs)


class Comment(TranslatableModel):
    translations = TranslatedFields(
        text=models.TextField(_('Text'), max_length=500)
    )
    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter('text', any_language=True)



class Product(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=200),
        info = models.CharField(_('Info'), max_length=300, blank=True, null=True),
        tags = models.CharField(_('Tags'), max_length=200, blank=True, null=True),
        description = CKEditor5Field(_('Description'), config_name='extends')
    )
    image = models.ImageField(upload_to='product_images/')
    category_type = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products_by_category',verbose_name='Category Type')
    old_price = models.FloatField()
    new_price = models.FloatField()
    game_id = models.CharField(max_length=100, unique=True)
    genre = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products_by_genre',verbose_name='Genre')
    is_trending = models.BooleanField(default=False, verbose_name='Is Trending')
    is_most_played = models.BooleanField(default=False, verbose_name='Is Most Played')
    play_count = models.PositiveIntegerField(default=0, verbose_name='Play Count')

    @property
    def imageURL(self):
        if self.image and self.image.storage.exists(self.image.name):
            return self.image.url
        return ''

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        ordering = ['-play_count', 'new_price']  # Play count, title, va narx bo'yicha tartiblash



class Contact(TranslatableModel):
    translations = TranslatedFields(
        info = CKEditor5Field('Text', config_name='extends'),
        address = models.CharField(max_length=300)
    )
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    def __str__(self):
        return self.safe_translation_getter('info', any_language=True) or self.address
