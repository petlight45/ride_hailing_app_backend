from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class Others:
    @staticmethod
    def render_response_object(response: Response) -> Response:
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response
