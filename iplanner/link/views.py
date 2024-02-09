from .serializers import *
from rest_framework import generics
from .models import Link


class links(generics.ListAPIView):
    serializer_class = LinkSerializer

    def get_queryset(self):
        object_type = self.kwargs['object_type']
        object_id = self.kwargs['object_id']
        return Link.objects.filter(object_type=object_type, object_id=object_id)


class link_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class create_link(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
