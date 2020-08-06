from .handler import DecayHandler,AbstractHandler

class BrdHandlerFactory:

    @classmethod
    def getBrdHandler(cls,type):
        if(type=='decay'):
            return DecayHandler()
        pass


if __name__ == "__main__":
    handler=BrdHandlerFactory.getBrdHandler('decay')
    print(isinstance(handler, AbstractHandler))
    pass