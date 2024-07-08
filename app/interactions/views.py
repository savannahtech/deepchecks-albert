from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UploadLLMSerializer, InteractionSerializers, AlertSerializers
from .tasks import read_interactions
from .models import LLMFile, LLMInteraction, Alert


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadLLMSerializer

    def list(self, request):
        qs = LLMInteraction.objects.all()
        serializer = InteractionSerializers(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        print(content_type)

        if content_type != "text/csv":
            return Response(
                {"success": False, "errors": "Invalid file format, csv format required!"},
                status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )
        new_int_file = LLMFile.objects.create(file=file_uploaded)
        read_interactions.delay(new_int_file.id)
        return Response(
            {
                "success": True,
                "errors": "Your interaction have been submitted and currently processing!",
            },
            status=status.HTTP_200_OK,
        )


class AlertViewSet(ModelViewSet):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializers
    permission_classes = [
        AllowAny,
    ]
