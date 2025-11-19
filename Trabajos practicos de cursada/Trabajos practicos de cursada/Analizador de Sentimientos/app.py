"""
Análisis de Sentimiento en Español - Interfaz Gradio
MVP con comparación BETO vs RoBERTuito
"""

import gradio as gr
from sentiment_analyzer import analyzer
from utils import clean_text, format_sentiment_result, get_example_texts, validate_input
import time

def analyze_sentiment(text: str, model_choice: str):
    """
    Función principal para análisis de sentimiento

    Args:
        text: Texto a analizar
        model_choice: 'beto', 'robertuito', o 'compare'

    Returns:
        Resultado formateado para Gradio
    """
    # Validar input
    is_valid, message = validate_input(text)
    if not is_valid:
        return message, "", ""

    # Limpiar texto
    clean_input = clean_text(text)

    try:
        if model_choice == "compare":
            # Comparación side-by-side
            result = analyzer.compare_models(clean_input)

            if "error" in result:
                return result["error"], "", ""

            beto_formatted = format_sentiment_result({
                "label": result["beto"]["label"],
                "score": result["beto"]["score"]
            })

            robertuito_formatted = format_sentiment_result({
                "label": result["robertuito"]["label"],
                "score": result["robertuito"]["score"]
            })

            # Información adicional
            agreement = "✅ Acuerdan" if result["agreement"] else "❌ Difieren"
            info = f"""
            **Comparación de Modelos:**
            - {agreement} en la clasificación
            - Longitud del texto: {result['text_length']} caracteres
            """

            return beto_formatted, robertuito_formatted, info

        else:
            # Análisis con un solo modelo
            result = analyzer.analyze_text(clean_input, model_choice)

            if "error" in result:
                return result["error"], "", ""

            formatted = format_sentiment_result(result)
            model_info = analyzer.get_model_info()[model_choice]

            info = f"""
            **Modelo usado:** {model_info['name']}
            - {model_info['description']}
            - Longitud del texto: {result['text_length']} caracteres
            """

            return formatted, "", info

    except Exception as e:
        return f"Error inesperado: {str(e)}", "", ""

def load_example(example_text: str):
    """Carga un ejemplo en el textbox"""
    return example_text

# Crear la interfaz Gradio
with gr.Blocks(
    title="Análisis de Sentimiento en Español",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 900px;
        margin: auto;
    }
    .sentiment-positive { color: #28a745; }
    .sentiment-negative { color: #dc3545; }
    .sentiment-neutral { color: #ffc107; }
    """
) as demo:

    gr.Markdown("""
    # 😊 Análisis de Sentimiento en Español

    **MVP** para comparar modelos de transformers pre-entrenados en español.

    Esta aplicación utiliza **BETO** (modelo formal) y **RoBERTuito** (especializado en redes sociales) para analizar el sentimiento de textos en español.
    """)

    with gr.Row():
        # Panel izquierdo - Inputs
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Input")

            text_input = gr.Textbox(
                label="Texto a analizar",
                placeholder="Ingresa un texto en español...",
                lines=4,
                max_lines=6
            )

            model_choice = gr.Radio(
                label="Modelo a usar",
                choices=["beto", "robertuito", "compare"],
                value="compare",
                info="BETO: formal | RoBERTuito: redes sociales | Comparar: ambos modelos"
            )

            analyze_btn = gr.Button(
                "🔍 Analizar Sentimiento",
                variant="primary",
                size="lg"
            )

            clear_btn = gr.Button("🗑️ Limpiar", size="sm")

        # Panel derecho - Outputs
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Resultados")

            # Resultado BETO
            with gr.Group():
                gr.Markdown("#### 🤖 BETO (Spanish BERT)")
                gr.Markdown("*Modelo formal entrenado en Wikipedia española*")
                result_beto = gr.Markdown(
                    value="Resultado aparecerá aquí..."
                )

            # Resultado RoBERTuito
            with gr.Group():
                gr.Markdown("#### 🐦 RoBERTuito (Redes Sociales)")
                gr.Markdown("*Modelo especializado en jerga y expresiones coloquiales*")
                result_robertuito = gr.Markdown(
                    value="Resultado aparecerá aquí..."
                )

            # Información adicional
            with gr.Group():
                info_output = gr.Markdown(
                    label="📋 Información adicional",
                    value=""
                )

    # Sección de ejemplos
    with gr.Accordion("💡 Ejemplos de prueba", open=False):
        examples = get_example_texts()
        example_buttons = []

        for i, example in enumerate(examples):
            btn = gr.Button(
                f"📝 '{example[:50]}...'",
                size="sm"
            )
            example_buttons.append(btn)

    # Conectar eventos
    analyze_btn.click(
        fn=analyze_sentiment,
        inputs=[text_input, model_choice],
        outputs=[result_beto, result_robertuito, info_output]
    )

    # Botón limpiar
    clear_btn.click(
        fn=lambda: ("", "", ""),
        inputs=[],
        outputs=[result_beto, result_robertuito, info_output]
    )

    # Conectar ejemplos
    for i, btn in enumerate(example_buttons):
        btn.click(
            fn=lambda ex=examples[i]: ex,
            inputs=[],
            outputs=[text_input]
        )

    # Footer
    gr.Markdown("""
    ---
    **Desarrollado con:** 🤗 Transformers + Gradio | **Modelos:** BETO & RoBERTuito
    """)

if __name__ == "__main__":
    print("Iniciando aplicación de análisis de sentimiento...")
    print("Cargando modelos (puede tardar unos minutos)...")

    # Forzar carga de modelos al inicio
    try:
        analyzer.models
        print("Modelos listos. Iniciando interfaz...")
        demo.launch(
            server_name="0.0.0.0",
            server_port=7860,
            show_error=True
        )
    except Exception as e:
        print(f"Error al cargar modelos: {e}")
        print("Revisa tu conexión a internet e intenta nuevamente.")