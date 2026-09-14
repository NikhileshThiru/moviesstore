from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'flagged']
    list_filter = ['flagged']
    actions = ['unflag_reviews', 'flag_reviews']

    @admin.action(description='Unflag selected reviews')
    def unflag_reviews(self, request, queryset):
        updated = queryset.update(flagged=False)

    @admin.action(description='Flag selected reviews')
    def flag_reviews(self, request, queryset):
        updated = queryset.update(flagged=True)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)