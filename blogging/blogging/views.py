from django.http import HttpResponse

#404 error
def handler404(request, exception):
    return HttpResponse("404 error")