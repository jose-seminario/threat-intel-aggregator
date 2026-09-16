from ioc import IOC
from detector import DetectorIOC

def create_ioc(texto, detector):
    tipo = detector.detectar(texto)
    if tipo == "Desconocido":
        raise ValueError(f"No se pudo determinar el tipo de IOC para el texto: {texto}")
    return IOC(valor=texto, tipo=tipo)