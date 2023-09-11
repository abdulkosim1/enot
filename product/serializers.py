from rest_framework import serializers
from .models import Product
from .models import Comment, Rating
from rest_framework import serializers

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ('rating',)

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['profile_image'] = instance.owner.profile_image.url
        return representation
    
    class Meta:
        model = Comment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    # likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)
    #     representation['total_likes'] = instance.likes.filter(is_like=True).count()
    #     representation['profile_image'] = instance.owner.profile_image.url
    #     return representation
    
    class Meta:
        model = Product
        fields = '__all__'

# class PostGetSerializer(serializers.ModelSerializer):
    # owner = serializers.EmailField(required=False)
    # likes = LikeSerializer(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)

    # def to_representation(self, instance):
    #     representation =  super().to_representation(instance)
    #     representation['total_likes'] = instance.likes.filter(is_like=True).count()
    #     representation['profile_image'] = instance.owner.profile_image.url
    #     return representation
    

    # class Meta:
    #     model = Post
    #     fields = '__all__'


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '__all__'



# class FavoriteSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.email')
    
#     class Meta:
#         model = Favorite
#         fields = '__all__'