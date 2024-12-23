from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BookSerializer
from .models import BooksModel
from rest_framework import status

# Create your views here.


class ApponeView(APIView):

    def get(self, request, id=None):
        if id:
            try:
             book = BooksModel.objects.get(id=id)
             serializer1 = BookSerializer(book)
             return Response({"message": "here are details about", "details" : serializer1.data })
            except BooksModel.DoesNotExist :
                return Response('book not in database', status=status.HTTP_404_NOT_FOUND)
        books = BooksModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"message": "books Get request successful", "data" : serializer.data})
    


    def post(self, request):
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("book has been added to library successfully", status= status.HTTP_201_CREATED)
        else: 
             return Response("request unsuccessfull", status= status.HTTP_206_PARTIAL_CONTENT)
    


    def put(self, request, id):
        data = request.data
        try:
            book = BooksModel.objects.get(id=id)
        except BooksModel.DoesNotExist:
            return Response ("book deos not exist", status= status.HTTP_204_NO_CONTENT)
        
        serializer = BookSerializer(book, data)
        if serializer.is_valid():
            serializer.save()
            return Response ("book edited successfully", status=status.HTTP_202_ACCEPTED)
    


    def patch(self, request, id):
        data = request.data
        try:
            book = BooksModel.objects.get(id=id)
        except BooksModel.DoesNotExist:
            return Response ("book deos not exist", status= status.HTTP_204_NO_CONTENT)
        
        serializer = BookSerializer(book, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response ("book edited successfully", status=status.HTTP_202_ACCEPTED)
 


    def delete(self, request, id):
        
        try:
            book = BooksModel.objects.get(id=id)
        except BooksModel.DoesNotExist:
            return Response ("book deos not exist", status= status.HTTP_204_NO_CONTENT)
        
        book.delete()
        
        return Response ("deleted successfully") 