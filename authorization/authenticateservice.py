import base64

from django.contrib.auth import authenticate


def validate(user_name: str, pass_word: str) -> bool:
    user = authenticate(username=user_name, password=pass_word)
    if user is not None:
        return True
    else:
        return False


def header_auth_view(request) -> bool:
    auth_header = request.META['HTTP_AUTHORIZATION']
    encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    return validate(username, password)


def validate_request(request) -> bool:
    username = request.headers.get('username')
    password = request.headers.get('password')
    if username is not None and password is not None:
        return validate(username, password)
    else:
        return header_auth_view(request)
