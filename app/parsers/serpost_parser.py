import asyncio
from app.models.shipment_dataclass import Envio, EnvioDetalle, RegistroEnvio
from app.services.serpost_requests import SerpostRequests

class SerpostParser:
    def __init__(self, tracking_number):
        self.serpostRequests = SerpostRequests(tracking_number)
        self.tracking_number = tracking_number
    
    async def parse_tracking_information(self):
        try:
            tracking_information, tracking_details = await asyncio.gather(self.serpostRequests.get_tracking_information(), self.serpostRequests.tracking_details())
        except Exception as e:
            print(f'Error: {e}')
        
    
        if tracking_information.json()['d'] == None or 'bject reference not set to an instance of an object' in tracking_information.text:
            return None
        
        envio = Envio(
            origen = tracking_information.json()['d'][0].get('RetornoCadena5', ''),
            estado_envio = tracking_information.json()['d'][0].get('RetornoCadena3', ''),
            nro_tracking = tracking_information.json()['d'][0].get('RetornoCadena2', ''),
            destino = tracking_information.json()['d'][0].get('RetornoCadena6', ''),
            tipo_envio = tracking_information.json()['d'][0].get('RetornoCadena7', ''),
            nro_aviso = tracking_information.json()['d'][0].get('RetornoCadena4', ''),
            observacion = tracking_information.json()['d'][0].get('RetornoCadena8', ''),
        )
        
        envio_detalle = EnvioDetalle(envio)
        
        registros = [RegistroEnvio(fecha=registro.get('RetornoCadena3'), estado=registro.get('RetornoCadena4')) for registro in tracking_details.json()['d']]
        
        envio_detalle.registros.extend(registros)
        
        return envio_detalle
    
