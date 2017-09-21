from rest_framework import serializers
from management.models import Category,Advertisement
from account.models import User



class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'phonenumber')


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
                        default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Advertisement
        fields = ('id','product_name', 'price', 'description', 'ad_date', 
                    'category', 'user', 'image')


class AdvertisementSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(read_only=True)
    class Meta:
        model = Advertisement
        fields = ('id', 'product_name', 'price', 'description', 'ad_date',
                 'category', 'user', 'image', 'view_count')


class CategorySerializer(serializers.ModelSerializer):
    advertisement_set = AdvertisementSerializer(many = True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'advertisement_set',)


# class AdvertisementSerializer(serializers.ModelSerializer):
#     user = BaseUserSerializer(read_only=True)
#     username = serializers.HiddenField(
#                     default=serializers.CurrentUserDefault()
#         )
#     view_count = serializers.HiddenField(
#                     default=0)

#     class Meta:
#         model = Advertisement
#         fields = ('id', 'product_name', 'price', 'description', 'ad_date', 'category', 'username', 'image', 'view_count')
