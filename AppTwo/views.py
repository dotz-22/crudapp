from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer
from .models import AuthorsModel
from rest_framework import status

# Create your views here.

class ApptwoView(APIView):

    def get(self, request, id=None):
        if id:
            try:
             author = AuthorsModel.objects.get(id=id)
             serializer1 = AuthorSerializer(author)
             return Response({"message": "here are details about", "details" : serializer1.data })
            except AuthorsModel.DoesNotExist :
                return Response('author not in database', status=status.HTTP_404_NOT_FOUND)

        authors = AuthorsModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response ({"message" : "here are all authors", "author": serializer.data})

    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("author added successfully", status=status.HTTP_201_CREATED)
        else :
            return Response("request unsuccessfull", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        data = request.data
        try:
            author = AuthorsModel.objects.get(id=id)
        except AuthorsModel.DoesNotExist:
            return Response ("book deos not exist", status= status.HTTP_204_NO_CONTENT)
        
        serializer = AuthorSerializer(author, data)
        if serializer.is_valid():
            serializer.save()

            return Response ("Author edited successfully", status=status.HTTP_202_ACCEPTED)
        else: 
            return Response ("Update unsuccessful", status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        data = request.data
        try:
            author = AuthorsModel.objects.get(id=id)
        except AuthorsModel.DoesNotExist:
            return Response ("book deos not exist", status= status.HTTP_204_NO_CONTENT)
        
        serializer = AuthorSerializer(author, data, partial= True)
        if serializer.is_valid():
            serializer.save()

            return Response ("partial update edited successfull", status=status.HTTP_202_ACCEPTED)

        else: 
            return Response ("Update unsuccessful", status=status.HTTP_400_BAD_REQUEST)
    
    
        

    def delete(self, request, id):
        try:
            author = AuthorsModel.objects.get(id=id)
        except AuthorsModel.DoesNotExist:
            return Response("author not in library ", status=status.HTTP_404_NOT_FOUND)
        
        author.delete()

        return Response("author deleted successfully")
