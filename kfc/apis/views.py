from rest_framework.views import APIView, Response, status
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from menu.serializers import ProductSerializer
from menu.models import Menu


class ProductsAPIView(APIView):
    def get(self, request):
        product_list = Menu.objects.all()

        query_params = request.query_params
        category_id = query_params.get("category_id")
        if category_id is not None:
            product_list = product_list.filter(category=category_id)

        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created Successfully"},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status. HTTP_404_NOT_FOUND)


class ProductDetailsAPIView(APIView):
    def get(self, request, product_id):
        product = Menu.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


def home(request):
    data_list = Menu.objects.all()
    api = {"data": data_list}
    return render(request, "index.html", api)
