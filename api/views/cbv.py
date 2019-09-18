from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from api.models import Review, Account
from api.serializers import ReviewSerializer,AccountSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView



class ReviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_superuser:
            reviews = Review.objects.all()
        else:
            reviews = Review.objects.filter(reviewer=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post (self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            ip = ip_address.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.validated_data['client_ip'] = ip
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

