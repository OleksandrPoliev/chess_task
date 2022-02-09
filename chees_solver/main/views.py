"""
function :
            start
            :return main page
            index
            :return possible move for url figure/position
            validate_move_for_chess
            :return validate_move for figure/position/needed_position

"""

from django.http import HttpResponse
from .figure import get_position, validate_move_for
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError


def start(request):
    return HttpResponse(
        "Hi, if you need chess helper just write in url field  something "
        "like this:   /pawn/a3   and you get json with all possible move for pawn "
        "from this chess field or write:   /pawn/a3/b2   and you get json with "
        "info is that move possible or not "
    )


def index(request, figure, fild):
    figure = figure.lower()
    data = {
        r"figure": f"{figure}",
        r"currentField ": f"{fild}",
    }
    if get_position(figure, fild) == "invalid data":
        datadict = {"error": "invalid data try agen"}
        datadict.update(data)
        return JsonResponse(datadict)

    if get_position(figure, fild) != "invalid data":
        datadict = {"availableMoves": get_position(figure, fild)}
        datadict.update(data)
        return JsonResponse(datadict)


def validate_move_for_chess(request, figure, fild, second):
    figure = figure.lower()
    if validate_move_for(figure, fild, second) == "invalid data":
        return HttpResponse("invalid data try again ")
    data = {
        "figure": f"{figure}",
        "currentField": f"{fild}",
        "destField": f"{second}",
    }
    if validate_move_for(figure, fild, second) == "invalid data":
        datadict = {"error": "invalid data try again"}
        datadict.update(data)
        return JsonResponse(datadict)
    if validate_move_for(figure, fild, second) != "invalid data":
        datadict = {"move": validate_move_for(figure, fild, second)}
        datadict.update(data)
        return JsonResponse(datadict)
    return JsonResponse(data)


def error_404(request, exception):
    request.status_code = 404
    return HttpResponseNotFound(
        "<h1>Sorry someting wrong please try another figure</h1>"
    )


def error_500(request, *args, **argv):
    return HttpResponseServerError(
        "<h1>We have problem(( with server please wait </h1>"
    )


def error_409(request, exception):
    return HttpResponse("<h1>Sorry this url does not exist</h1>")
