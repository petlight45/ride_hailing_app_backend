class Request:
    @staticmethod
    def get_access_token_from_auth_header(request):
        token = request.META.get("HTTP_AUTHORIZATION")
        token = token and token.startswith("Bearer ") and token.split(" ")[1]
        token = token and token.strip()
        return token
