"""
Módulo 04: Few-Shot de Salida.
Ejemplos que enseñan el formato JSON y el comportamiento seguro del asistente.
"""


FEW_SHOT_SALIDA = [
	{
		"contexto_tecnico": """
[MANUAL TÉCNICO SERIE H-500 - IMPRESORAS INDUSTRIALES]
Código de Error: E-301
Descripción: Sobrecalentamiento en el fusor primario.
Procedimiento: Apague el equipo de inmediato y desconecte de la red eléctrica.
Espere 15 minutos a que la temperatura baje. Abra la compuerta B3 y verifique
si hay restos de tóner acumulados.
Precaución: El módulo fusor alcanza temperaturas superiores a 180°C. Manipular
solo con guantes térmicos.
""",
		"consulta_usuario": "La impresora muestra el error E-301, ¿qué hago?",
		"respuesta_esperada": {
			"estado": "resuelto",
			"resumen": "El error E-301 indica sobrecalentamiento en el fusor primario.",
			"diagnostico": "El manual relaciona el código E-301 con el fusor primario.",
			"pasos": [
				"Apague el equipo de inmediato.",
				"Desconéctelo de la red eléctrica.",
				"Espere 15 minutos a que la temperatura baje.",
				"Abra la compuerta B3 y verifique si hay restos de tóner acumulados.",
			],
			"advertencias_seguridad": [
				"El módulo fusor alcanza temperaturas superiores a 180°C.",
				"Manipule el módulo solo con guantes térmicos.",
			],
			"fuentes": ["MANUAL TÉCNICO SERIE H-500 - IMPRESORAS INDUSTRIALES"],
		},
	},
	{
		"contexto_tecnico": """
[INSTRUCTIVO DE CONFIGURACIÓN DE REDES - ROUTER R-80]
Para restablecer los valores de fábrica, mantenga presionado el botón RESET
durante 10 segundos mientras el LED de POWER esté en verde fijo.
""",
		"consulta_usuario": "El LED POWER parpadea en rojo y la red no responde. ¿Cómo lo arreglo?",
		"respuesta_esperada": {
			"estado": "informacion_insuficiente",
			"resumen": "El manual no describe qué hacer cuando el LED POWER parpadea en rojo.",
			"diagnostico": "Solo existe un procedimiento para el estado de LED POWER verde fijo.",
			"pasos": [],
			"advertencias_seguridad": [],
			"fuentes": ["INSTRUCTIVO DE CONFIGURACIÓN DE REDES - ROUTER R-80"],
		},
	},
]


def formatear_few_shot_salida() -> str:
	"""Serializa los ejemplos como XML, preservando el JSON esperado."""
	import json
	from xml.sax.saxutils import escape

	ejemplos = ["<ejemplos_salida>"]
	for indice, ejemplo in enumerate(FEW_SHOT_SALIDA, 1):
		contexto = escape(ejemplo["contexto_tecnico"].strip())
		consulta = escape(ejemplo["consulta_usuario"])
		respuesta = json.dumps(
			ejemplo["respuesta_esperada"], ensure_ascii=False, indent=2
		)
		ejemplos.extend(
			[
				f'  <ejemplo id="{indice}">',
				f"    <contexto_tecnico>{contexto}</contexto_tecnico>",
				f"    <consulta_usuario>{consulta}</consulta_usuario>",
				f"    <respuesta_esperada>{escape(respuesta)}</respuesta_esperada>",
				"  </ejemplo>",
			]
		)
	ejemplos.append("</ejemplos_salida>")
	return "\n".join(ejemplos)
