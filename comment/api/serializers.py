from rest_framework import serializers

from comment.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]

    def validate(self, attrs):
        if attrs["parent"]:
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("something went wrong")

        return attrs


class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]