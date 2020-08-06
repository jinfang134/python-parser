

from src.factory import BrdHandlerFactory
from src.handler import AbstractHandler


handler = BrdHandlerFactory.getBrdHandler('decay')
print(handler)
pass

