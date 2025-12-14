import json
from pathlib import Path


def cargar_dosificaciones():
    ruta = Path("data/dosificaciones_rne.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def calcular_materiales(volumen_m3, fc):
    datos = cargar_dosificaciones()

    fc = str(fc)
    if fc not in datos:
        raise ValueError(f"f'c {fc} no disponible según RNE E.060")

    d = datos[fc]

    return {
        "cemento_bolsas": round(d["cemento"] * volumen_m3, 2),
        "arena_m3": round(d["arena"] * volumen_m3, 2),
        "grava_m3": round(d["grava"] * volumen_m3, 2),
        "agua_litros": round(d["agua"] * volumen_m3, 0),
        "relacion_ac": d["ac"]
    }
