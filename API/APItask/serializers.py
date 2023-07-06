from rest_framework import serializers
from .models import PostModel

"""Self writen serializer"""


class PostSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    author = serializers.CharField(required=False)

    def create(self, validated_data):
        return PostModel.objects.create(title=validated_data['title'],
                                        content=validated_data['content'],
                                        author=self.context['user'])


class PostSerializerUpdate(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    time_create = serializers.DateTimeField(read_only=True)
    author = serializers.CharField(read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


"""Model serializer"""
# class PostSerializer(ModelSerializer):
#     class Meta:
#         model = PostModel
#         fields = '__all__'
