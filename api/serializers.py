from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

class FavoritsSerialaizer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = FavoriteItem
        fields = ['user']


class ItemListSerializer(serializers.ModelSerializer):
    users_favorited_count = serializers.SerializerMethodField()

    added_by = UserSerializer()

    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields = ['image', 'name', 'detail', 'added_by', 'users_favorited_count']

    def get_users_favorited_count(self , obj):
        return obj.favs.count()






class ItemDetailSerializer(serializers.ModelSerializer):
    favs = FavoritsSerialaizer(many = True)
    class Meta:
        model = Item
        fields = '__all__'

    




    



