from rest_framework.serializers import Serializer, FileField, ModelSerializer
from .models import LLMInteraction, Alert


# Serializers define the API representation.
class UploadLLMSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


class InteractionSerializers(ModelSerializer):
    class Meta:
        model = LLMInteraction
        fields = "__all__"


class AlertSerializers(ModelSerializer):
    llm = InteractionSerializers()

    class Meta:
        model = Alert
        fields = "__all__"
