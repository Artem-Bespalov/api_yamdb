from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reviews.models import Category, Comment, Genre, Review, Title, User


class SignupSerializer(serializers.Serializer):
    """Сериализатор регистрации пользователя."""
    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        """Проверка: username не равен me."""
        if value.lower() == "me":
            raise serializers.ValidationError(
                'Username "me" не разрешено.'
            )
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор получения токена авторизации."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор модели пользователя'''
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        exclude = ('id', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
