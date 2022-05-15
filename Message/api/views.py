from django.http import JsonResponse
from pytz import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from datetime import datetime,timedelta, timezone


class MessageRoute(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        msg=request.GET.get('msg')
        user=request.user
        time_now=datetime.now(timezone.utc)
        time_threshold = time_now-timedelta(hours=1)
        result = Message.objects.filter(created_byId=user.id,created_at__gt=time_threshold)
        if result.count()>10:
            return Response({"error":"Message per hour limited exceeded"})

        obj=Message(msg=msg,created_byId=user.id,username=user.username,email=user.email)
        obj.save()
        data={

                "id": obj.id,

                "message": msg,

                "created_at": obj.created_at,

                "updated_at": obj.updated_at,

                "created_by": {

                "id": user.id,

                "username": user.username,

                "email": user.email
                }

            }
        return Response(data)

class UpdateMessage(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,id):
        try:
            obj = Message.objects.get(id=id)
            user=request.user
            if obj.created_byId==user.id:
                msg=request.GET.get('msg')
                obj.msg=msg
                obj.updated_at=datetime.now(timezone.utc)
                obj.save()

                data={

                "id": obj.id,

                "message": msg,

                "created_at": obj.created_at,

                "updated_at": obj.updated_at,

                "created_by": {

                "id": user.id,

                "username": user.username,

                "email": user.email
                }

            }
                return Response(data)


            else:
                return Response({"error":"This message is not created by you"})    
        except:
            return Response({"error":"Message id doesn't exist"})
