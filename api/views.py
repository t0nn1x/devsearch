from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects/'}, # List all projects
        {'GET': '/api/projects/id'}, # Get a single project
        {'POST': '/api/projects/id/vote'}, # Vote for a project

        {'POST': '/api/users/token'}, # Login
        {'POST': '/api/users/token/refresh'}, # Refresh token
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)