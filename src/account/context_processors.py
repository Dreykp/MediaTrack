from django.conf import settings

def global_settings(request):
    """
    Додає вибрані змінні з settings.py до контексту шаблону.
    """
    return {
        'BRAND_NAME': getattr(settings, 'BRAND_NAME', 'MediaTrack'),
    }