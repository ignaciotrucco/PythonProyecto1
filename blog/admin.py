from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]