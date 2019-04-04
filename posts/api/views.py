from rest_framework import generics

from django.contrib.auth.models import User
from posts.models import Post, Category
from rest_framework import serializers

#from posts.api.serializers import PostSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]
        ookup_field = 'slug'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug','status', 'category', 'author']


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer
    def get_queryset(self):
        category1 = self.kwargs.get('category')
        posts = Post.objects.filter(category__slug=category1)
        return posts





class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
