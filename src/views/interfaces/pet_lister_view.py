from src.views.interfaces.view_interface import ViewsInterface
from src.controllers.interfaces.pet_lister_controller import PetsListerControllerInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse


class PetListerView(ViewsInterface):
    def __init__(self, controller: PetsListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response= self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)
