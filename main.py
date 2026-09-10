import os
from dotenv import load_dotenv
from google import genai

# Imports de la parte de Ingesta y Contexto (Tú)
from prompts.system_prompt_base import obtener_system_prompt
from prompts.few_shot_ingesta import formatear_few_shot_xml

# Imports de la parte de Razonamiento y Salida (Tu compañera)
from prompts.system_prompt_salida import obtener_system_prompt_salida
from prompts.few_shot_salida import formatear_few_shot_salida

# 1. Cargar variables de entorno
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la GEMINI_API_KEY en el archivo .env")

# 2. Inicializar el cliente oficial de Gemini
client = genai.Client(api_key=api_key)

# 3. Ensamblar los componentes del prompt
system_prompt_completo = f"""
{obtener_system_prompt()}

{obtener_system_prompt_salida()}

---
SECCIÓN DE EJEMPLOS DEMOSTRATIVOS (FEW-SHOT):
{formatear_few_shot_xml()}

{formatear_few_shot_salida()}
"""

def consultar_asistente(contexto_manual: str, pregunta: str):
    """
    Formatea la entrada con etiquetas XML y realiza la consulta al modelo.
    """
    user_prompt = f"""
<contexto_tecnico>
{contexto_manual}
</contexto_tecnico>

<consulta_usuario>
{pregunta}
</consulta_usuario>
"""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_prompt,
        config={
            "system_instruction": system_prompt_completo,
            "temperature": 0.2  # Temperatura baja para evitar alucinaciones
        }
    )
    
    return response.text

# --- PRUEBA RÁPIDA ---
if __name__ == "__main__":
    manual_ejemplo = """
    [MANUAL TÉCNICO ROUTER X-200]
    Error R-10: Fallo de sincronización de fibra óptica.
    Solución: Desconecte el latiguillo de fibra, limpie el conector con alcohol isopropílico al 99% y un paño sin pelusa. Vuelva a conectar firmemente hasta escuchar un clic.
    Precaución: No mire directamente hacia el conector de fibra activa (Riesgo de daño ocular por láser invisible Class 1M).
    """
    
    pregunta_ejemplo = "El router marca el error R-10 y no da internet. ¿Qué debo hacer?"
    
    print("Enviando consulta a Gemini...\n")
    resultado = consultar_asistente(manual_ejemplo, pregunta_ejemplo)
    print("=== RESPUESTA DEL ASISTENTE ===")
    print(resultado)