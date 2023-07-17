from app.parsers.serpost_parser import SerpostParser
from app.views.serpost_view import SerpostView

class SerpostController:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.serpostView = SerpostView()
        self.serpostParser = SerpostParser(tracking_number)
    
    async def get_tracking_information(self):
        envio_detalle = await self.serpostParser.parse_tracking_information()
        
        if envio_detalle == None:
            print('No se encontraron resultados')
            return
        
        self.serpostView.print_envio_detalle(envio_detalle)

