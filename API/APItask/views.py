from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import PostModel
from .serializers import PostSerializer, PostSerializerUpdate
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostApiListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

    def get(self, request):
        """Получение списка постов"""
        posts = PostModel.objects.all()
        return Response({'posts': PostSerializer(posts, many=True).data})

    def post(self, request):
        """Создание поста"""
        serializer = PostSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except:
            return Response({'error': 'You have to be authenticated'})
        return Response({'added': serializer.data})


class PostApiUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializerUpdate
    queryset = PostModel.objects.all()

    def get(self, request, pk):
        """Получить одну запись"""
        try:
            post = PostModel.objects.get(pk=pk)
            return Response({'post': PostSerializer(post).data})
        except:
            return Response({'error': 'This post does not exists'})

    def patch(self, request, pk):
        """Обновить одну запись"""
        try:
            update_post = PostModel.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        if request.user == update_post.author or request.user.username == 'admin':
            serializer = PostSerializerUpdate(data=request.data, instance=update_post)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response({'error': 'This function only for admin or author'})
        return Response({'updated': serializer.data})

    def put(self, request, pk):
        """Обновить одну запись"""
        try:
            update_post = PostModel.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        if request.user == update_post.author or request.user.username == 'admin':
            serializer = PostSerializerUpdate(data=request.data, instance=update_post)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response({'error': 'This function only for admin or author'})
        return Response({'updated': serializer.data})

    def delete(self, request, pk):
        """Удалить одну запись"""
        try:
            delete_post = PostModel.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        if request.user == delete_post.author or request.user.username == 'admin':
            delete_post.delete()
        else:
            return Response({'error': 'This function only for admin or author'})
        return Response({'deleted': PostSerializer(delete_post).data})
