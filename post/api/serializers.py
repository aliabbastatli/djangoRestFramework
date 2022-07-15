from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modifiedBy'
        ]

    @staticmethod
    def get_username(obj):
        return str(obj.user.username)
