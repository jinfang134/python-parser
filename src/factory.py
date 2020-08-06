from .handler import DecayHandler,AbstractHandler

class BrdHandlerFactory:

    @classmethod
    def getBrdHandler(cls,type):
        if(type=='decay'):
            return DecayHandler()
        pass

