from rest_framework import serializers
from .models import Product
# from feedback.serializers import LikeSerializer, CommentSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    # likes = LikeSerializer(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)

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