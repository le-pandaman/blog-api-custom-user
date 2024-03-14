from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:

        model = Posts

        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )

    def to_representation(self, instance) -> str:

        data = super().to_representation(instance)
        data['author'] = instance.author.username
        return data
