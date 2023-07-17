
class SerpostView:
    def __init__(self):
        pass

    def print_envio(self, envio):
        print(f'Origen: {envio.origen}')
        print(f'Estado: {envio.estado_envio}')
        print(f'Nro. Tracking: {envio.nro_tracking}')
        print(f'Destino: {envio.destino}')
        print(f'Tipo de envio: {envio.tipo_envio}')
        print(f'Nro. Aviso: {envio.nro_aviso}')
        print(f'Observacion: {envio.observacion}')
        print('-----------------------------------')
    
    def print_envio_detalle(self, envio_detalle):
        self.print_envio(envio_detalle.envio)
        
        for registro in envio_detalle.registros:
            print(f'Fecha: {registro.fecha}')
            print(f'Estado: {registro.estado}')
            print('-----------------------------------')


