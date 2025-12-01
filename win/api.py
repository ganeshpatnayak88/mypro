from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_api(request):
    return Response({"status": "ok", "message": "registered!"})

@api_view(['POST'])
def login_api(request):
    return Response({"status": "ok", "message": "login successful"})
