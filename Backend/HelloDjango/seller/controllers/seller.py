from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..serializers import SellerSerializer
from ..models import Seller


class SellerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=201)
        return Response(status=400)

    def get(self, request):
        seller = Seller.objects.get(user=request.user)
        serializer = SellerSerializer(seller, many=False)
        return Response(serializer.data)

    def put(self, request):
        seller = Seller.objects.get(user=request.user)
        serializer = SellerSerializer(seller, data=request.data)
        return Response(status=200)
