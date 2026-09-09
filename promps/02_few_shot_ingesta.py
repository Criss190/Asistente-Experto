"""
Módulo 02: Few-Shot Ingesta (Rol 1 - Extracción de Información Téknica)
Ejemplos de entrenamiento para guiar al modelo a analizar y extraer datos de manuales ruidosos.
"""

FEW_SHOT_INGESTA = [
    {
        "contexto_tecnico": """
        [MANUAL TÉCNICO SERIE H-500 - IMPRESORAS INDUSTRIALES]
        Código de Error: E-301
        Descripción: Sobrecalentamiento en el fusor primario.
        Procedimiento: Apague el equipo de inmediato y desconecte de la red eléctrica. Espere 15 minutos a que la temperatura baje. Abra la compuerta B3 y verifique si hay restos de tóner acumulados.
        Precaución: El módulo fusor alcanza temperaturas superiores a 180°C. Manipular solo con guantes térmicos.
        """,
        "consulta_usuario": "La impresora muestra el error E-301 en la pantalla, ¿qué hago?",
        "extraccion_esperada": """
        <extraccion_datos>
          - Equipo / Modelo: Impresora Industrial Serie H-500
          - Código de Error: E-301
          - Fallo identificado: Sobrecalentamiento en el fusor primario
          - Componentes clave: Fusor primario, Red eléctrica, Compuerta B3
          - Advertencia de Seguridad: Riesgo de quemaduras (temperaturas > 180°C). Usar guantes térmicos.
          - Acciones encontradas en manual: Sí (Apagar, desconectar, esperar 15 min, revisar compuerta B3).
        </extraccion_datos>
        """
    },
    {
        "contexto_tecnico": """
        [INSTRUCTIVO DE CONFIGURACIÓN DE REDES - ROUTER R-80]
        Para restablecer los valores de fábrica, mantenga presionado el botón RESET ubicado en la parte posterior durante 10 segundos mientras el LED de POWER esté en verde fijo.
        """,
        "consulta_usuario": "El LED de POWER está parpadeando en rojo y la red no responde. ¿Cómo lo arreglo?",
        "extraccion_esperada": """
        <extraccion_datos>
          - Equipo / Modelo: Router R-80
          - Estado reportado: LED POWER parpadeando en rojo
          - Información en manual: El manual solo describe el procedimiento cuando el LED POWER está en 'verde fijo'. No hay instrucciones para estado 'rojo parpadeante'.
          - Estado de la consulta: INFORMACIÓN INSUFICIENTE EN EL MANUAL
        </extraccion_datos>
        """
    }
]


def formatear_few_shot_xml() -> str:
    """
    Convierte la lista de ejemplos Few-Shot en un bloque formateado en XML 
    listo para concatenar en el prompt final.
    """
    bloque_xml = "<ejemplos_demostrativos>\n"
    for i, ejemplo in enumerate(FEW_SHOT_INGESTA, 1):
        bloque_xml += f'  <ejemplo id="{i}">\n'
        bloque_xml += f'    <contexto_tecnico>\n{ejemplo["contexto_tecnico"].strip()}\n    </contexto_tecnico>\n'
        bloque_xml += f'    <consulta_usuario>{ejemplo["consulta_usuario"]}</consulta_usuario>\n'
        bloque_xml += f'    {ejemplo["extraccion_esperada"].strip()}\n'
        bloque_xml += f'  </ejemplo>\n'
    bloque_xml += "</ejemplos_demostrativos>"
    return bloque_xml