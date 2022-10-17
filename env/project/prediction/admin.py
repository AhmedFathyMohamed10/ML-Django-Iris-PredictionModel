from django.contrib import admin
from .models import ModelPredict


class ModelAdminPredict(admin.ModelAdmin):
    list_display = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'prediction')
    list_filter = ('prediction',)
    search_fields = ('prediction',)
    ordering = ('prediction',)

admin.site.register(ModelPredict, ModelAdminPredict)
