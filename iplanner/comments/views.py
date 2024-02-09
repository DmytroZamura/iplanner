from .serializers import *
from rest_framework import generics

#
# class conversation_details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Conversation.objects.all()
#     serializer_class =  ConversationSerializer
#
# class create_conversation(generics.CreateAPIView):
#     queryset = Conversation.objects.all()
#     serializer_class =  ConversationSerializer


class comment_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class create_comment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class comments(generics.ListAPIView):

    serializer_class =  CommentSerializer

    def get_queryset(self):
        object_type = self.kwargs['object_type']
        object_id = self.kwargs['object_id']
        return Comment.objects.filter(object_type=object_type, object_id=object_id)