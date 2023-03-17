from rest_framework import serializers
from .models import ShortURL

HOST = 'http://127.0.0.1:8000/'


class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(max_length=8, allow_blank=True, required=False)
    clickable_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ('full_url', 'short_url', 'premium', 'created_at', 'times_clicked', 'clickable_url')

    def get_clickable_url(self, obj):
        base_url = 'url/'
        return f"{HOST}{base_url}{obj.short_url}"
