from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Scopes, Article, Tag
from django.core.exceptions import ValidationError


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                count += 1
                if count > 1:
                    raise ValidationError('Только один основной')
            else:
                return super().clean()


class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopesInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links = ['id', 'title']
    inlines = [ScopesInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']



