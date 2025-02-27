from typing import Dict
from abc import ABC, abstractmethod

@abstractmethod
class PetsListerControllerInterface(ABC):

    def list(self) -> Dict:
        pass
