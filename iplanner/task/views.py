from .serializers import *
from rest_framework import generics



class task_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class create_task(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class tasks(generics.ListAPIView):

    serializer_class =  TaskSerializer

    def get_queryset(self):
        object_type = self.kwargs['object_type']
        object_id = self.kwargs['object_id']
        return Task.objects.filter(object_type=object_type, object_id=object_id)