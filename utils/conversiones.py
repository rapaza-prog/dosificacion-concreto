import json
from pathlib import Path


def cargar_unidades():
    ruta = Path("data/unidades_obra.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def aplicar_desperdicio(valor, porcentaje):
    return valor * (1 + porcentaje / 100)


def convertir_unidades(volumen_m3, unidad):
    unidades = cargar_unidades()
    return round(volumen_m3 / unidades[unidad]["volumen_m3"])
