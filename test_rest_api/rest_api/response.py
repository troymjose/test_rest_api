from dataclasses import dataclass
from aiohttp import ClientResponse
from .. import settings


@dataclass(frozen=True)
class RestApiResponse:
    """
    test_rest_api Response object
    Users can use this instead of aiohttp ClientResponse object
    """
    status_code: int
    body: dict
    content_type: str
    headers: dict
    obj: ClientResponse

    def __str__(self):
        #TODO: need to adjust in Rest api creation and send, the gap, because status code is updated
        return f"""
 {settings.logging.sub_point} Status Code {settings.logging.key_val_sep} {self.status_code}
 {settings.logging.sub_point} Body        {settings.logging.key_val_sep} {self.body}
"""
