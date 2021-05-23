from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import uuid


# Create your views here.


class TimestampUUID:

    def __init__(self):
        self.output = []

    def add(self, key, value):
        self.output.insert(0, {str(key): value})

    def all(self):
        return self.output


timestamp_uuid = TimestampUUID()


class TimestampUUIDView(APIView):

    def get(self, request):
        """
        :param request:
        :return: list of dictionary of timestamp as key and generated uuid as value
        """
        key = datetime.now()
        value = uuid.uuid4().hex
        timestamp_uuid.add(key, value)
        return Response(timestamp_uuid.all(), status=status.HTTP_200_OK)
