from rest_framework import serializers

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:

        model = Posts
        fields = '__all__'

    def to_representation(self, instance) -> str:

        data = super().to_representation(instance)
        data['author'] = instance.author.username
        return data
