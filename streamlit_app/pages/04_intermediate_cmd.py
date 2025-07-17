"""
Módulo 04: Scripts y Variables (CMD Intermedio)
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
    """Renderiza la página de CMD intermedio"""
    
    # Header principal
    create_section_header(
        title="Scripts y Variables en CMD",
        description="Aprende a crear scripts batch y usar variables para automatizar tareas",
        icon="⚫"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Comprender qué son las variables de entorno",
        "Crear y usar variables locales en scripts",
        "Escribir scripts batch básicos (.bat)",
        "Usar estructuras de control simples",
        "Automatizar tareas repetitivas"
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
    
    st.markdown("## � Variables en CMD")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Variables de Entorno")
        st.markdown("""
        Las **variables de entorno** son valores almacenados por el sistema operativo que pueden ser utilizados por programas y scripts. En CMD, puedes acceder a ellas usando `%VARIABLE%`.
        """)
        
        create_code_example(
            "Variables de entorno comunes",
            """echo %USERNAME%
echo %COMPUTERNAME%
echo %PATH%
echo %USERPROFILE%
echo %DATE%
echo %TIME%""",
            "batch",
            "Estas variables contienen información del sistema y usuario"
        )
        
        st.markdown("### Variables Locales")
        st.markdown("""
        Puedes crear tus propias variables usando el comando `set`. Estas variables solo existen durante la sesión actual.
        """)
        
        create_code_example(
            "Crear variables locales",
            """set nombre=Juan
set edad=25
set mensaje=Hola Mundo
echo %nombre%
echo %mensaje%""",
            "batch"
        )
        
        st.markdown("### Scripts Batch (.bat)")
        st.markdown("""
        Un **script batch** es un archivo de texto que contiene comandos CMD. Se ejecuta línea por línea automáticamente.
        """)
        
        create_code_example(
            "Ejemplo de script batch (backup.bat)",
            """@echo off
echo Iniciando respaldo...
set fecha=%DATE%
mkdir "Backup_%fecha%"
copy *.txt "Backup_%fecha%\\"
echo Respaldo completado!
pause""",
            "batch",
            "@echo off evita mostrar los comandos mientras se ejecutan"
        )
    
    with col2:
        create_tip_card(
            "💡 Tip: @echo off",
            "Usa @echo off al inicio de tus scripts para que no se muestren los comandos mientras se ejecutan, solo los resultados.",
            "info"
        )
        
        create_tip_card(
            "⚠️ Cuidado con espacios",
            "Si una variable contiene espacios, usa comillas: set \"ruta=C:\\Mis Documentos\"",
            "warning"
        )
        
        st.markdown("### Caracteres Especiales")
        st.code("""
%0 - Nombre del script
%1 - Primer parámetro
%2 - Segundo parámetro
%* - Todos los parámetros
        """)

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Simulador de consola
    st.markdown("### 🖤 Consola CMD - Práctica con Variables")
    cmd_simulator = ConsoleSimulator("cmd")
    cmd_simulator.render(key_suffix="cmd_intermediate")
    
    st.markdown("---")
    st.markdown("## 🎯 Ejercicios Guiados")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Muestra tu nombre de usuario usando una variable de entorno",
            "ejemplo": "echo %USERNAME%",
            "comando": "echo",
            "tipo_consola": "cmd",
            "pista": "Usa la variable %USERNAME% para mostrar el nombre del usuario actual",
            "solucion": "echo %USERNAME% - Muestra el nombre del usuario logueado"
        },
        {
            "descripcion": "Crea una variable llamada 'saludo' con el valor 'Hola CMD'",
            "ejemplo": "set saludo=Hola CMD",
            "comando": "set",
            "tipo_consola": "cmd",
            "pista": "Usa 'set variable=valor' para crear variables locales",
            "solucion": "set saludo=Hola CMD - Crea una variable local"
        },
        {
            "descripcion": "Muestra el contenido de la variable 'saludo' que creaste",
            "ejemplo": "echo %saludo%",
            "comando": "echo",
            "tipo_consola": "cmd",
            "pista": "Usa %nombre_variable% para acceder al valor de una variable",
            "solucion": "echo %saludo% - Muestra el contenido de la variable"
        },
        {
            "descripcion": "Muestra la fecha actual del sistema",
            "ejemplo": "echo %DATE%",
            "comando": "echo",
            "tipo_consola": "cmd",
            "pista": "%DATE% es una variable de entorno que contiene la fecha actual",
            "solucion": "echo %DATE% - Muestra la fecha del sistema"
        },
        {
            "descripcion": "Crea una carpeta con el nombre que incluya la fecha actual",
            "ejemplo": "mkdir Backup_%DATE%",
            "comando": "mkdir",
            "tipo_consola": "cmd",
            "pista": "Combina texto fijo con variables usando _",
            "solucion": "mkdir Backup_%DATE% - Crea carpeta con fecha en el nombre"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="cmd_intermediate_practice")

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: Variables y Scripts CMD")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Cómo accedes al valor de una variable llamada 'nombre' en CMD?",
            "opciones": ["%nombre%", "$nombre", "{nombre}", "var:nombre"],
            "respuesta_correcta": "%nombre%",
            "explicacion": "En CMD, las variables se acceden usando % antes y después del nombre."
        },
        {
            "pregunta": "¿Qué comando usas para crear una variable local?",
            "opciones": ["var", "set", "let", "define"],
            "respuesta_correcta": "set",
            "explicacion": "El comando 'set' se usa para crear y modificar variables locales."
        },
        {
            "pregunta": "¿Qué hace '@echo off' en un script batch?",
            "opciones": [
                "Desactiva el sonido",
                "Evita mostrar los comandos mientras se ejecutan",
                "Borra la pantalla",
                "Termina el script"
            ],
            "respuesta_correcta": "Evita mostrar los comandos mientras se ejecutan",
            "explicacion": "@echo off oculta los comandos y solo muestra sus resultados."
        },
        {
            "pregunta": "¿Cuál es la extensión de los archivos de script de CMD?",
            "opciones": [".cmd", ".bat", ".sh", "Ambas .cmd y .bat"],
            "respuesta_correcta": "Ambas .cmd y .bat",
            "explicacion": "Tanto .bat como .cmd son extensiones válidas para scripts de CMD."
        }
    ]
    
    # Componente de quiz
    quiz_component = QuizComponent(quiz_questions)
    quiz_component.render(key_suffix="cmd_intermediate_quiz")

def render_reference_section():
    """Renderiza la sección de referencia"""
    
    st.markdown("## 📖 Referencia Rápida")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Variables de Entorno Comunes")
        st.code("""
%USERNAME% - Nombre de usuario
%COMPUTERNAME% - Nombre del equipo
%USERPROFILE% - Perfil del usuario
%PATH% - Rutas de ejecutables
%DATE% - Fecha actual
%TIME% - Hora actual
%CD% - Directorio actual
%RANDOM% - Número aleatorio
        """, language="batch")
        
        st.markdown("### Comandos de Variables")
        st.code("""
set var=valor    - Crear variable
set var=         - Borrar variable
set              - Mostrar todas las variables
echo %var%       - Mostrar valor de variable
        """, language="batch")
    
    with col2:
        st.markdown("### Estructura de Script Batch")
        st.code("""
@echo off
rem Esto es un comentario
set variable=valor
echo %variable%
pause
        """, language="batch")
        
        st.markdown("### Parámetros de Script")
        st.code("""
%0 - Nombre del script
%1 - Primer parámetro
%2 - Segundo parámetro
%3 - Tercer parámetro
%* - Todos los parámetros
        %~1 - Primer parámetro sin comillas
        """, language="batch")
    
    create_tip_card(
        "🚀 Próximo paso",
        "Una vez que domines las variables, podrás crear scripts más complejos con estructuras de control y automatización avanzada.",
        "success"
    )

if __name__ == "__main__":
    render_page()
