from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class HomePage(viewsets.GenericViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "home/index.html"

    def list(self, request):
        username = self.request.query_params.get("username")
        if username is None:
            username = "Anon"
        return Response({"username": username.upper()})
