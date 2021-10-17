from django.core import mail
from django.http import Http404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import Contact
from .permissions import IsOperationAllowed
from .serializer import ContactSerializer
from project.settings import EMAIL_HOST_USER, EMAIL_RECEIVER


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsOperationAllowed]
    serializer_class = ContactSerializer

    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

        except Http404:
            pass

        connection = mail.get_connection()

        message = mail.EmailMessage(
            'Contact list',
            'One of contacts was delete.',
            EMAIL_HOST_USER,
            [EMAIL_RECEIVER],
            connection=connection,
        )
        message.send()

        return Response(status=HTTP_204_NO_CONTENT)
