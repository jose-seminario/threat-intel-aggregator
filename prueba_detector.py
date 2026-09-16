from detector import DetectorIOC

detector = DetectorIOC()

valores = [
    "8.8.8.8",
    "ejemplo.com",
    "d41d8cd98f00b204e9800998ecf8427e",
    "hola mundo",
    "999.999.999.999",
]

for v in valores:
    print(v, "→", detector.detectar(v))