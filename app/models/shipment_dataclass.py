from dataclasses import dataclass

@dataclass
class Envio:
    origen: str
    estado_envio: str
    nro_tracking: str
    destino: str
    tipo_envio: str
    nro_aviso: str
    observacion: str

@dataclass
class RegistroEnvio:
    fecha: str
    estado: str

@dataclass
class EnvioDetalle:
    envio: Envio
    registros: list[RegistroEnvio]
    
    def __init__(self, envio):
        self.envio = envio
        self.registros = []
    
    def add_registro(self, registro):
        self.registros.append(registro)
