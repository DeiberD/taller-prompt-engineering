#!/usr/bin/env python3
"""Agente con un subagente especializado usando el Claude Agent SDK.

El agente principal recibe un pedido y delega la revisión de referencias
en el subagente "revisor-de-fuentes", que trabaja con su propio contexto
y solo con herramientas de lectura y búsqueda.

Requisitos:
    pip install claude-agent-sdk
    export ANTHROPIC_API_KEY="tu-clave"

Uso (desde esta carpeta):
    python agente_sdk.py ../../taller/04-agentes/informe-de-prueba.md

Documentación: https://platform.claude.com/docs/en/agent-sdk/overview
"""

import sys

import anyio
from claude_agent_sdk import (
    AgentDefinition,
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)

REVISOR_DE_FUENTES = AgentDefinition(
    description=(
        "Verifica que las referencias de un documento existan y respalden "
        "lo que se les atribuye."
    ),
    prompt=(
        "Eres un revisor de fuentes académicas. Para cada referencia: búscala, "
        "confirma autores, año y publicación, y verifica si respalda la "
        "afirmación del documento. Si no puedes acceder a la fuente, márcala "
        "como 'No verificable'. Devuelve solo una tabla con las columnas: "
        "#, Referencia, ¿Existe?, ¿Respalda la afirmación?, Observaciones."
    ),
    tools=["Read", "WebSearch", "WebFetch"],
    model="sonnet",
)

OPCIONES = ClaudeAgentOptions(
    system_prompt=(
        "Ayudas a estudiantes a revisar sus documentos antes de entregarlos. "
        "No modificas archivos: solo revisas y reportas."
    ),
    # El agente principal no puede escribir archivos ni ejecutar comandos.
    disallowed_tools=["Write", "Edit", "Bash"],
    agents={"revisor-de-fuentes": REVISOR_DE_FUENTES},
    max_turns=20,
)


async def main(ruta_documento: str) -> None:
    pedido = (
        f"Usa el subagente revisor-de-fuentes para revisar las referencias de "
        f"{ruta_documento}. Luego resume en tres viñetas qué debe corregir el "
        f"estudiante antes de entregar."
    )

    async for mensaje in query(prompt=pedido, options=OPCIONES):
        if isinstance(mensaje, AssistantMessage):
            for bloque in mensaje.content:
                if isinstance(bloque, TextBlock):
                    print(bloque.text)
        elif isinstance(mensaje, ResultMessage) and mensaje.total_cost_usd:
            print(f"\nCosto aproximado: USD {mensaje.total_cost_usd:.4f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python agente_sdk.py ruta/al/documento.md")
        sys.exit(2)
    anyio.run(main, sys.argv[1])
