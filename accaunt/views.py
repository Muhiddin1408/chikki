import random

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from rest_framework_jwt.settings import api_settings

from api.models import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accaunt.models import User
from accaunt.serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    try:
        first_name = request.data.get('first_name')
        phone = request.data.get('phone')
        print(phone)
        sms_code = request.data.get('sms_code')
        if not phone:
            res = {
                'msg': 'Login empty',
                'status': 0,
            }
            return Response(res)

        number = User.objects.filter(username=phone).first()
        if not number:
            number = User.objects.create(
                username=phone,
                first_name=first_name,

            )
        elif number:
            sms_code = random.randint(1000, 9999)
            number.phone = int(phone)
            number.sms_code = sms_code
            number.save()
            send_sms(phone, "Tasdiqlash codi " + str(sms_code))
            if number:
                result = {
                    'status': 1,
                    'msg': 'The SMS was sent again',
                    'user': CustomuserSerializer(number, many=False, context={"request": request}).data,
                }
                return Response(result, status=status.HTTP_200_OK)
            else:
                res = {
                    'status': 0,
                    'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
                }
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        sms_code = random.randint(1000, 9999)
        number.phone = int(phone)
        number.sms_code = sms_code
        number.save()
        send_sms(phone, "Tasdiqlash codi " + str(sms_code))
        if number:
            result = {
                'status': 1,
                'msg': 'Sms sended',
                'user': CustomuserSerializer(number, many=False, context={"request": request}).data,
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register_accepted(request):
    try:
        phone = request.data.get('phone')
        sms_code = request.data.get('sms_code')
        user = User.objects.filter(username=phone).first()
        if user and user.sms_code == int(sms_code):
            if user.sms_status == False:
                user.sms_status = True
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            result = {
                'status': 1,
                'msg': 'Sms sended',
                'user': CustomuserSerializer(user, many=False, context={"request": request}).data,
                'token': token,
            }

            return Response(result, status=status.HTTP_200_OK)
        else:
            result = {
                'status': 2,
                'msg': 'Sms send not equal',
            }
            return Response(result, status=status.HTTP_200_OK)

    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def profil(request):
    try:
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        avatar = request.data.get('avatar')
        user = request.user
        user.avatar = avatar
        user.first_name = first_name
        user.last_name = last_name
        user.complete = 2
        if 'avatar' in request.data:
            user.avatar = request.data['avatar']
        user.save()
        result = {
            'status': 1,
            'msg': 'User updated',
            'user': CustomuserSerializer(user, many=False, context={"request": request}).data
        }
        return Response(result, status=status.HTTP_200_OK)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


import requests
from requests.auth import HTTPBasicAuth


def send_sms(phone, message):
    code = 'td_1'
    login = "onlinestartup"
    password = "gR82S3z"
    posturl = 'http://91.204.239.44/broker-api/send'
    jsonData = {
        'messages': [
            {
                'recipient': phone,
                'message-id': code,
                'sms': {
                    'originator': '3700',
                    'content': {
                        'text': message
                    }
                }
            }
        ]
    }
    r = requests.post(posturl, json=jsonData, auth=HTTPBasicAuth(login, password))
    if r.status_code == 200:
        print('sms_code=>', r, r.status_code, jsonData)
        return r


class Home(viewsets.ModelViewSet):
    queryset = Restorant.objects.all()
    serializer_class = RestorantSerializer

    @action(methods=['post'], detail=False)
    def search(self, request):
        f = request.GET.get('f')
        filter = Restorant.objects.filter(name=f)
        d = RestorantSerializer(filter, many=True).data
        return Response(d)


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    @action(methods=['get'], detail=False)
    def by_id(self, request):
        id = int(request.GET.get('id'))
        b = Product.objects.filter(restaurant_id=id)
        page = self.paginate_queryset(b)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(b, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def by_type(self, request):
        restaurant = int(request.GET.get('restaurant'))
        type = int(request.GET.get('type'))
        b = Product.objects.filter(restaurant=restaurant, type=type)
        page = self.paginate_queryset(b)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(b, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def id(self, request):
        id = request.GET.get('id')
        b = Product.objects.filter(id=id)
        serializer = self.get_serializer(b, many=True)
        return Response(serializer.data)


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination
