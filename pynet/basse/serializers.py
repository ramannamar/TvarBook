from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """ serializer for filtering comments and outputting only root comments
    """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ This class is a serializer for recursive output of child objects
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
