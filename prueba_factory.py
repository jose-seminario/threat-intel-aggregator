from detector import DetectorIOC
from factory import create_ioc


def probar_caso_valido(detector):
    ioc = create_ioc("8.8.8.8", detector)
    print("valor:", ioc.valor)
    print("tipo:", ioc.tipo)
    print("score:", ioc.score)


def probar_caso_invalido(detector):
    try:
        create_ioc("hola mundo", detector)
        print("ERROR: debió lanzar excepción pero no lo hizo")
    except ValueError as e:
        print("OK: se lanzó ValueError correctamente")
        print("Mensaje:", e)


def main():
    detector = DetectorIOC()
    probar_caso_valido(detector)
    probar_caso_invalido(detector)


if __name__ == "__main__":
    main()