import json
from pathlib import Path


def cargar_dosificaciones():
    ruta = Path("data/dosificaciones_rne.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def calcular_materiales(volumen_m3, fc, desperdicio=0):
    datos = cargar_dosificaciones()
    fc = str(fc)

    if fc not in datos:
        raise ValueError(f"f'c {fc} no disponible según RNE E.060")

    d = datos[fc]

    cemento = d["cemento"] * volumen_m3
    arena = d["arena"] * volumen_m3
    grava = d["grava"] * volumen_m3
    agua = d["agua"] * volumen_m3

    if desperdicio > 0:
        factor = 1 + desperdicio / 100
        cemento *= factor
        arena *= factor
        grava *= factor
        agua *= factor

    return {
        "cemento_bolsas": round(cemento, 2),
        "arena_m3": round(arena, 2),
        "grava_m3": round(grava, 2),
        "agua_litros": round(agua, 0),
        "relacion_ac": d["ac"]
    }

