from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status

from organizer.models import Startup
from .serializers import StartupSerializer

def check_auth(func):
    ''' check authorization '''
    def wrapper(self,  *args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated:
            return Response( status=status.HTTP_401_UNAUTHORIZED) # redirect!!!
        return func(self, args, kwargs)
    return wrapper


class StartupListAPIView(APIView):
    @check_auth
    def get(self, *args, **kwargs):
        startups = Startup.objects.all()
        serializer = StartupSerializer(startups, many=True)
        return Response(serializer.data)

class StartupDetailAPIView(APIView):
    
    @check_auth
    def get(self, *args, **kwargs):
        slug = args[1]['slug']
        try:
            startup = Startup.objects.get(slug=slug)
            print(startup.name)
        except Startup.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StartupSerializer(startup)
        return Response(serializer.data)

    @check_auth
    def put(self, *args, **kwargs):
        request = args[0]
        print(args)
        serializer = StartupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
