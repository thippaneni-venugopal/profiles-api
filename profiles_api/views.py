from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers


class HelloApiView(APIView):
  """Test API View"""
  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Returns a list of APIView features"""

    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similar to a traditional Django View',
      'Gives you the most controll over your application logic',
      'Is mapped manully to URLs',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})


  def post(self, request):
    """Create a hello message with our name"""

    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f"Hello {name}"
      return Response({'message': message})
    else:
      return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
      )


  def put(self, request, pk=None):
    """ Handling updating object """

    return Response({'method': 'PUT'})


  def patch(self, request, pk=None):
    """ Handling partial updating object """

    return Response({'method': 'PATCH'})


  def delete(self, request, pk=None):
    """ Handling deleting object """

    return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
  """ Test Aoi ViewSet """

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """ retun a hello message """

    a_viewset = [
      'Uses actions (list, create, retrieve, update, partial_update)',
      'Automatically maps to URLs using Routers',
      'Provides more functionality with less code',
    ]

    return Response({'message': 'Hello ViewSet!', 'a_viewset': a_viewset})


  def create(self, request):
    """ Create a new hello message """

    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return  Response({'message': message})
    else:
      return Response(
          serializer.errors,
          status = status.HTTP_400_BAD_REQUEST
        )

  def retrieve(self, request, pk=None):
    """ Handling getiing object """

    return Response({'http_method': 'GET'})

  def update(self, request, pk=None):
    """ Handling updating object """

    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    """ Handling partial updating object """

    return Response({'http_method': 'PATCH'})

  def destroy(self, request, pk=None):
    """ Handling deleting object """

    return Response({'http_method': 'DELETE'})

