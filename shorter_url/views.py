from django.shortcuts import get_object_or_404, redirect
from rest_framework import status, generics
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer


class CreateShortURLAPIView(generics.GenericAPIView):
    serializer_class = ShortURLSerializer

    def post(self, request, *args, **kwargs):
        custom_short_url = request.data.get('short_url')
        premium = bool(custom_short_url)

        data = request.data.copy()
        data['premium'] = premium

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAllURLsAPIView(generics.ListAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer


class ShortURLDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = 'short_url'


class RetrieveFullURLAPIView(generics.GenericAPIView):
    def get(self, request, short_url, *args, **kwargs):
        shortened_url = get_object_or_404(ShortURL, short_url=short_url)
        shortened_url.times_clicked += 1
        shortened_url.save()
        return redirect(shortened_url.full_url)
