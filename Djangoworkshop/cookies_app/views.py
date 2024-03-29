from django.http import HttpResponse

def set_cookie(_________):
    response = HttpResponse("cookie set")
    response.set_cookie('username', 'rajesh')

    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Hello, {username} !")