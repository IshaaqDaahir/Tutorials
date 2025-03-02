from rest_framework.decorators import api_view
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return JsonResponse(routes, safe=False)