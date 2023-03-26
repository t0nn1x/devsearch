from django.http import JsonResponse


def getRoutes(request):
    routes = [
        {'GET': '/api/projects/'}, # List all projects
        {'GET': '/api/projects/id'}, # Get a single project
        {'POST': '/api/projects/id/vote'}, # Vote for a project

        {'POST': '/api/users/token'}, # Login
        {'POST': '/api/users/token/refresh'}, # Refresh token
    ]
    return JsonResponse(routes, safe=False)