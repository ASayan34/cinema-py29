from applications.films.models import Film
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from applications.films.models import Film, Like, Rating
from applications.films.permissions import IsOwnerOrAdminOrReadOnly
from applications.films.serializers import FilmSerializer, LikeSerializer, RatingtSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter, OrderingFilter

# class FilmsListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
    

# class CreateFilmAPIView(generics.CreateAPIView):
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
       

# class RetrieveFilmAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAdminOrIsOwner]


# class UpdateFilmAPIView(generics.UpdateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = BookSerializer    
#     permission_classes = [IsAdminOrIsOwner]


# class DeleteFilmAPIView(generics.DestroyAPIView):
#     queryset = Film.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAdminOrIsOwner]
    
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    
    
class FilmAPIView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = LargeResultsSetPagination
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    
    search_fields = ['title']
    ordering_fields = ['id']
    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwagrs):
        user = request.user
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        if not like_obj.is_like:
            status = 'unliked'
        
        return Response({'status': status}) 

    @action(methods=['POST'], detail=True) # post/obj_id/rating
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingtSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

