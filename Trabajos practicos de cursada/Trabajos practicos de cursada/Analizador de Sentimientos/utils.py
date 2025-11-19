"""
Utilidades para el análisis de sentimiento
"""

import re

def clean_text(text: str) -> str:
    """
    Limpia y normaliza el texto de entrada

    Args:
        text: Texto a limpiar

    Returns:
        Texto limpio
    """
    if not text:
        return ""

    # Remover espacios extra
    text = re.sub(r'\s+', ' ', text.strip())

    # Limitar longitud (BERT max 512 tokens)
    if len(text) > 500:
        text = text[:500] + "..."

    return text

def format_sentiment_result(result: dict) -> str:
    """
    Formatea el resultado del análisis para display

    Args:
        result: Dict con resultado del modelo

    Returns:
        String formateado
    """
    if "error" in result:
        return f"❌ Error: {result['error']}"

    label = result['label']
    score = result['score']

    # Emojis y colores por sentimiento
    if label == "POS":
        emoji = "😊"
        color = "green"
    elif label == "NEG":
        emoji = "😞"
        color = "red"
    else:  # NEU
        emoji = "😐"
        color = "orange"

    return f"{emoji} **{label}** (Confianza: {score:.1%})"

def get_example_texts() -> list:
    """
    Retorna ejemplos de textos para testing

    Returns:
        Lista de textos de ejemplo
    """
    return [
        "La comida estaba deliciosa, muy recomendable.",
        "El servicio fue pésimo, nunca volveré.",
        "Está bien, nada especial.",
        "¡Re copado el lugar! 🔥",
        "Qué garrón, tardaron una banda.",
        "Excelente atención del personal.",
        "No me gustó para nada la experiencia.",
        "Todo perfecto, superó mis expectativas.",
        "Regular nomás, podría mejorar.",
        "¡La rompieron! Todo increíble."
    ]

def validate_input(text: str) -> tuple:
    """
    Valida el input del usuario

    Args:
        text: Texto a validar

    Returns:
        (is_valid: bool, message: str)
    """
    if not text.strip():
        return False, "Por favor ingresa un texto."

    if len(text.strip()) < 3:
        return False, "El texto debe tener al menos 3 caracteres."

    if len(text) > 1000:
        return False, "El texto es muy largo (máximo 1000 caracteres)."

    return True, "Texto válido."