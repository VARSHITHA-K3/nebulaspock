from django.http import HttpResponse
from django.http import JsonResponse

from nebulaspock.authorization.authenticateservice import validate_request
from nebulaspock.chatbot import chatbot


def default(request):
    return HttpResponse("Nebula Spock Version 2.1.00.474")


def chat_response(request, name):
    swordsmen = len(name.split(" "))
    if swordsmen == 1:
        name = "Incomplete context"

    if name != "":
        content = chatbot.return_response(name)
        return JsonResponse(content)

if __name__ == "__main__":
    chat_response(None,"hi there")
