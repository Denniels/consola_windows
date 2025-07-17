"""
Módulo 05: Objetos y Pipeline (PowerShell Intermedio)
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    ConsoleSimulator, QuizComponent, CommandPracticeComponent,
    create_learning_objective_card, create_tip_card, create_code_example
)

def render_page():
    """Renderiza la página de PowerShell intermedio"""
    
    # Header principal
    create_section_header(
        title="Objetos y Pipeline en PowerShell",
        description="Aprende a trabajar con objetos y el poder del pipeline para filtrar y procesar datos",
        icon="🔵"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Comprender qué son los objetos en PowerShell",
        "Usar el pipeline (|) para combinar comandos",
        "Filtrar datos con Where-Object",
        "Seleccionar propiedades con Select-Object",
        "Procesar colecciones con ForEach-Object"
    ]
    create_learning_objective_card(objectives)
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Teoría", "🎯 Práctica", "🧩 Cuestionario", "📖 Referencia"])
    
    with tab1:
        render_theory_section()
    
    with tab2:
        render_practice_section()
    
    with tab3:
        render_quiz_section()
    
    with tab4:
        render_reference_section()

def render_theory_section():
    """Renderiza la sección de teoría"""
    
    st.markdown("## 🎯 Objetos en PowerShell")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### ¿Qué son los Objetos?")
        st.markdown("""
        A diferencia de CMD que trabaja solo con texto, **PowerShell trabaja con objetos**. Un objeto tiene propiedades (información) y métodos (acciones que puede realizar).
        """)
        
        create_code_example(
            "Ejemplo: Archivo como objeto",
            """Get-ChildItem archivo.txt | Get-Member
# Muestra todas las propiedades y métodos del archivo""",
            "powershell",
            "Get-Member te muestra todo lo que puedes hacer con un objeto"
        )
        
        st.markdown("### El Pipeline (|)")
        st.markdown("""
        El **pipeline** es el símbolo `|` que permite enviar la salida de un comando como entrada del siguiente. Es el corazón de PowerShell.
        """)
        
        create_code_example(
            "Pipeline básico",
            """Get-Process | Where-Object {$_.CPU -gt 100}
# Obtiene procesos y filtra los que usan más de 100 de CPU""",
            "powershell",
            "El pipeline permite combinar comandos de forma muy potente"
        )
        
        st.markdown("### Cmdlets de Filtrado")
        st.markdown("""
        PowerShell incluye cmdlets especializados para trabajar con objetos en el pipeline:
        """)
        
        create_code_example(
            "Cmdlets principales",
            """# Where-Object: Filtrar objetos
Get-Service | Where-Object {$_.Status -eq "Running"}

# Select-Object: Seleccionar propiedades
Get-Process | Select-Object Name, CPU

# Sort-Object: Ordenar objetos
Get-Process | Sort-Object CPU -Descending""",
            "powershell"
        )
    
    with col2:
        create_tip_card(
            "💡 $_ Variable Automática",
            "$_ representa el objeto actual en el pipeline. Es muy útil en Where-Object y ForEach-Object.",
            "info"
        )
        
        create_tip_card(
            "🚀 Pipeline vs Comandos",
            "Un pipeline Get-Process | Where-Object es más eficiente que ejecutar múltiples comandos separados.",
            "success"
        )
        
        st.markdown("### Operadores Comunes")
        st.code("""
-eq  : Igual a
-ne  : No igual a  
-gt  : Mayor que
-lt  : Menor que
-like: Contiene patrón
-match: Expresión regular
        """)

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Simulador de consola
    st.markdown("### 🔷 Consola PowerShell - Práctica con Objetos")
    ps_simulator = ConsoleSimulator("powershell")
    ps_simulator.render(key_suffix="ps_intermediate")
    
    st.markdown("---")
    st.markdown("## 🎯 Ejercicios Guiados")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Lista solo los procesos que están usando más de 50 MB de memoria",
            "ejemplo": "Get-Process | Where-Object {$_.WorkingSet -gt 50MB}",
            "comando": "Get-Process",
            "tipo_consola": "powershell",
            "pista": "Usa Where-Object con la propiedad WorkingSet y el operador -gt",
            "solucion": "Get-Process | Where-Object {$_.WorkingSet -gt 50MB}"
        },
        {
            "descripcion": "Muestra solo el nombre y el estado de todos los servicios",
            "ejemplo": "Get-Service | Select-Object Name, Status",
            "comando": "Get-Service",
            "tipo_consola": "powershell",
            "pista": "Usa Select-Object para elegir solo las propiedades que necesitas",
            "solucion": "Get-Service | Select-Object Name, Status"
        },
        {
            "descripcion": "Lista los archivos del directorio actual ordenados por tamaño (mayor a menor)",
            "ejemplo": "Get-ChildItem | Sort-Object Length -Descending",
            "comando": "Get-ChildItem",
            "tipo_consola": "powershell",
            "pista": "Usa Sort-Object con la propiedad Length y -Descending",
            "solucion": "Get-ChildItem | Sort-Object Length -Descending"
        },
        {
            "descripcion": "Encuentra todos los servicios que contengan 'Windows' en el nombre",
            "ejemplo": "Get-Service | Where-Object {$_.Name -like '*Windows*'}",
            "comando": "Get-Service",
            "tipo_consola": "powershell",
            "pista": "Usa Where-Object con el operador -like y wildcards *",
            "solucion": "Get-Service | Where-Object {$_.Name -like '*Windows*'}"
        },
        {
            "descripcion": "Cuenta cuántos archivos .txt hay en el directorio actual",
            "ejemplo": "Get-ChildItem *.txt | Measure-Object",
            "comando": "Get-ChildItem",
            "tipo_consola": "powershell",
            "pista": "Combina Get-ChildItem con un patrón y Measure-Object",
            "solucion": "Get-ChildItem *.txt | Measure-Object - Cuenta objetos"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="ps_intermediate_practice")

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: Objetos y Pipeline")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Qué símbolo se usa para el pipeline en PowerShell?",
            "opciones": [">", "|", "&", "\\"],
            "respuesta_correcta": "|",
            "explicacion": "El símbolo | (pipe) se usa para enviar la salida de un comando al siguiente."
        },
        {
            "pregunta": "¿Qué representa $_ en PowerShell?",
            "opciones": [
                "El directorio actual",
                "El usuario actual", 
                "El objeto actual en el pipeline",
                "La variable de entorno"
            ],
            "respuesta_correcta": "El objeto actual en el pipeline",
            "explicacion": "$_ es una variable automática que representa el objeto que se está procesando."
        },
        {
            "pregunta": "¿Qué cmdlet usas para filtrar objetos por una condición?",
            "opciones": ["Filter-Object", "Where-Object", "Find-Object", "Select-Object"],
            "respuesta_correcta": "Where-Object",
            "explicacion": "Where-Object filtra objetos basándose en condiciones que especifiques."
        },
        {
            "pregunta": "¿Cuál es la diferencia principal entre CMD y PowerShell?",
            "opciones": [
                "CMD es más rápido",
                "PowerShell trabaja con objetos, CMD solo con texto",
                "CMD tiene más comandos",
                "No hay diferencias importantes"
            ],
            "respuesta_correcta": "PowerShell trabaja con objetos, CMD solo con texto",
            "explicacion": "PowerShell maneja objetos con propiedades y métodos, no solo texto plano."
        }
    ]
    
    # Componente de quiz
    quiz_component = QuizComponent(quiz_questions)
    quiz_component.render(key_suffix="ps_intermediate_quiz")

def render_reference_section():
    """Renderiza la sección de referencia"""
    
    st.markdown("## 📖 Referencia Rápida")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Cmdlets de Pipeline")
        st.code("""
Where-Object {...}   - Filtrar objetos
Select-Object prop   - Seleccionar propiedades  
Sort-Object prop     - Ordenar objetos
Group-Object prop    - Agrupar objetos
Measure-Object       - Contar/medir objetos
ForEach-Object {...} - Procesar cada objeto
        """, language="powershell")
        
        st.markdown("### Operadores de Comparación")
        st.code("""
-eq    Igual a
-ne    No igual a
-gt    Mayor que
-ge    Mayor o igual que
-lt    Menor que
-le    Menor o igual que
-like  Coincide con patrón (*)
-match Coincide con regex
        """, language="powershell")
    
    with col2:
        st.markdown("### Ejemplos de Pipeline")
        st.code("""
# Servicios corriendo
Get-Service | Where-Object {$_.Status -eq "Running"}

# Top 5 procesos por CPU
Get-Process | Sort-Object CPU -Desc | Select-Object -First 5

# Archivos grandes
Get-ChildItem | Where-Object {$_.Length -gt 1MB}

# Contar archivos por extensión
Get-ChildItem | Group-Object Extension
        """, language="powershell")
        
        st.markdown("### Variables Automáticas")
        st.code("""
$_           Objeto actual en pipeline
$PSItem      Alias de $_
$Args        Argumentos de función
$Error       Errores recientes
$Host        Información del host
$Profile     Ruta del perfil de PowerShell
        """, language="powershell")
    
    create_tip_card(
        "🚀 Próximo paso",
        "Con objetos y pipeline dominados, estarás listo para automatización avanzada y scripts complejos en PowerShell.",
        "success"
    )

if __name__ == "__main__":
    render_page()
