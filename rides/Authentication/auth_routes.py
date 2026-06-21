from django.http import JsonResponse
import json
from rides.models import User
from .auth import hash_password,verify_password,create_access_token

def register(request):

    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.create(
            username=data["username"],
            password=hash_password(data["password"]),
            role=data["role"]
        )

        return JsonResponse({
            "message": "User created"
        })
    


def login(request):

    if request.method == "POST":

        data = json.loads(request.body)

        try:
            user = User.objects.get(username=data["username"])

        except User.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid credentials"},
                status=401
            )

        if not verify_password(data["password"],user.password):
            return JsonResponse(
                {"error": "Invalid credentials"},
                status=401
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role
            }
        )

        return JsonResponse({
            "access_token": token
        })
    