#!/usr/bin/env python3
"""Revisa la estructura de un informe de laboratorio escrito en Markdown.

Uso:
    python validar_informe.py informe.md

Comprueba:
  - que estén las secciones esperadas (por título),
  - que no queden marcadores [DATO FALTANTE: ...] sin resolver,
  - que cada tabla y figura numerada se cite en el texto,
  - que exista una declaración de uso de IA.

Solo usa la biblioteca estándar de Python.
"""

import re
import sys
import unicodedata
from pathlib import Path

SECCIONES = [
    "resumen",
    "introduccion",
    "marco teorico",
    "procedimiento",
    "resultados",
    "analisis",
    "conclusiones",
    "referencias",
    "declaracion de uso de ia",
]


def normalizar(texto: str) -> str:
    """Pasa a minúsculas y quita tildes para comparar títulos."""
    sin_tildes = unicodedata.normalize("NFD", texto)
    sin_tildes = "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn")
    return sin_tildes.lower()


def revisar(ruta: Path) -> list[str]:
    texto = ruta.read_text(encoding="utf-8")
    problemas: list[str] = []

    titulos = [normalizar(t) for t in re.findall(r"^#{1,6}\s+(.+)$", texto, re.MULTILINE)]
    for seccion in SECCIONES:
        if not any(seccion in titulo for titulo in titulos):
            problemas.append(f"Falta la sección: {seccion}")

    for marcador in re.findall(r"\[DATO FALTANTE:[^\]]*\]", texto):
        problemas.append(f"Marcador sin resolver: {marcador}")

    for tipo in ("Tabla", "Figura"):
        numeros = set(re.findall(rf"{tipo}\s+(\d+)\.", texto))
        for numero in sorted(numeros, key=int):
            menciones = re.findall(rf"{tipo}\s+{numero}\b", texto)
            if len(menciones) < 2:
                problemas.append(f"La {tipo.lower()} {numero} no se cita en el texto")

    return problemas


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python validar_informe.py informe.md")
        return 2

    ruta = Path(sys.argv[1])
    if not ruta.is_file():
        print(f"No se encontró el archivo: {ruta}")
        return 2

    problemas = revisar(ruta)
    if not problemas:
        print("Sin problemas de estructura.")
        return 0

    print(f"Se encontraron {len(problemas)} problema(s):")
    for problema in problemas:
        print(f"- {problema}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
