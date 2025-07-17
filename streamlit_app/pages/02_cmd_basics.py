"""
Módulo 02: Comandos Básicos en CMD
"""

import streamlit as st
import sys
import os

# Agregar paths necesarios
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import (
    ConsoleSimulator, QuizComponent, CommandPracticeComponent,
    create_learning_objective_card, create_tip_card
)

def render_page():
    """Renderiza la página de comandos básicos CMD"""
    
    # Header principal
    create_section_header(
        title="Comandos Básicos en CMD",
        description="Aprende los comandos esenciales para navegar y manipular archivos en Command Prompt",
        icon="⚫"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Dominar los comandos básicos de navegación (dir, cd)",
        "Aprender a manipular archivos y directorios",
        "Usar comandos de información del sistema",
        "Crear y ejecutar comandos simples"
    ]
    create_learning_objective_card(objectives)
    
    # Pestañas para organizar el contenido
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Teoría", "🎯 Práctica", "🧩 Quiz", "📖 Referencia"])
    
    with tab1:
        render_theory_section()
    
    with tab2:
        render_practice_section()
    
    with tab3:
        render_quiz_section()
    
    with tab4:
        render_reference_section()
    
    # Marcar progreso
    if 'progress_tracker' in st.session_state:
        st.session_state.progress_tracker.update_module_progress("02_cmd_basics", "cmd_basics_viewed")

def render_theory_section():
    """Renderiza la sección de teoría"""
    
    st.markdown("## 🗂️ Comandos de Navegación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `dir` - Listar contenido")
        st.code("dir", language="batch")
        st.markdown("""
        **Función:** Muestra archivos y carpetas del directorio actual
        
        **Variaciones útiles:**
        - `dir /w` - Vista amplia (columnas)
        - `dir /p` - Pausa cada pantalla
        - `dir *.txt` - Solo archivos .txt
        """)
        
        st.markdown("### `cd` - Cambiar directorio")
        st.code("""cd Documents
cd ..
cd C:\\Users""", language="batch")
        st.markdown("""
        **Función:** Navega entre directorios
        
        **Variaciones:**
        - `cd ..` - Subir un nivel
        - `cd \\` - Ir a la raíz
        - `cd` (solo) - Mostrar directorio actual
        """)
    
    with col2:
        st.markdown("### `cls` - Limpiar pantalla")
        st.code("cls", language="batch")
        st.markdown("**Función:** Borra todo el contenido de la pantalla")
        
        st.markdown("### `help` - Obtener ayuda")
        st.code("""help
help dir
help cd""", language="batch")
        st.markdown("**Función:** Muestra ayuda de comandos")
    
    st.markdown("---")
    st.markdown("## 📁 Comandos de Archivos y Directorios")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `mkdir` / `md` - Crear directorio")
        st.code("""mkdir NuevaCarpeta
md "Carpeta con espacios\"""", language="batch")
        
        st.markdown("### `copy` - Copiar archivos")
        st.code("""copy archivo.txt backup.txt
copy *.txt C:\\Backup\\""", language="batch")
        
        st.markdown("### `move` - Mover/renombrar")
        st.code("""move archivo.txt NuevaCarpeta\\
move viejo.txt nuevo.txt""", language="batch")
    
    with col2:
        st.markdown("### `del` - Eliminar archivos")
        st.code("""del archivo.txt
del *.tmp""", language="batch")
        
        st.markdown("### `rmdir` / `rd` - Eliminar directorio")
        st.code("""rmdir CarpetaVacia
rd /s CarpetaConContenido""", language="batch")
        
        st.markdown("### `type` - Ver contenido")
        st.code("type archivo.txt", language="batch")
    
    create_tip_card(
        "⚠️ Cuidado con rutas que tienen espacios",
        'Usa comillas cuando la ruta tenga espacios: cd "Mis Documentos"',
        "warning"
    )
    
    st.markdown("---")
    st.markdown("## 🔧 Comandos de Sistema")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `echo` - Mostrar texto")
        st.code("""echo Hola Mundo
echo %DATE%
echo Mensaje > archivo.txt""", language="batch")
        
        st.markdown("### `ver` - Versión de Windows")
        st.code("ver", language="batch")
        
        st.markdown("### `date` y `time`")
        st.code("""date
time""", language="batch")
    
    with col2:
        st.markdown("### `ipconfig` - Configuración de red")
        st.code("""ipconfig
ipconfig /all""", language="batch")
        
        st.markdown("### `ping` - Probar conectividad")
        st.code("ping google.com", language="batch")
        
        st.markdown("### `tasklist` - Procesos activos")
        st.code("tasklist", language="batch")

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🎯 Simulador de CMD")
    st.markdown("Practica los comandos en este simulador que imita el comportamiento real de CMD:")
    
    # Crear simulador de CMD
    cmd_simulator = ConsoleSimulator("cmd")
    cmd_simulator.render(key_suffix="cmd_basics")
    
    st.markdown("---")
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Aprende a listar archivos y directorios con el comando 'dir'",
            "ejemplo": "dir",
            "comando": "dir",
            "tipo_consola": "cmd",
            "pista": "Simplemente escribe 'dir' y presiona Enter",
            "solucion": "dir - Lista todos los archivos y carpetas del directorio actual"
        },
        {
            "descripcion": "Muestra el directorio actual donde te encuentras",
            "ejemplo": "cd",
            "comando": "cd",
            "tipo_consola": "cmd",
            "pista": "Usa 'cd' sin argumentos para ver la ubicación actual",
            "solucion": "cd - Sin argumentos muestra el directorio actual"
        },
        {
            "descripcion": "Crea un nuevo directorio llamado 'MiPrueba'",
            "ejemplo": "mkdir MiPrueba",
            "comando": "mkdir",
            "tipo_consola": "cmd",
            "pista": "Usa 'mkdir' seguido del nombre del directorio",
            "solucion": "mkdir MiPrueba - Crea un nuevo directorio"
        },
        {
            "descripcion": "Muestra el mensaje 'Aprendiendo CMD' en la consola",
            "ejemplo": "echo Aprendiendo CMD",
            "comando": "echo",
            "tipo_consola": "cmd",
            "pista": "Usa 'echo' seguido del texto que quieres mostrar",
            "solucion": "echo Aprendiendo CMD - Muestra texto en la consola"
        },
        {
            "descripcion": "Obtén información sobre la versión de Windows",
            "ejemplo": "ver",
            "comando": "ver",
            "tipo_consola": "cmd",
            "pista": "Simplemente escribe 'ver' para ver información del sistema",
            "solucion": "ver - Muestra la versión del sistema operativo"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="cmd_practice")
    
    create_tip_card(
        "💡 Consejos para practicar",
        "No te preocupes si cometes errores. Los comandos en el simulador son seguros y no afectan tu sistema real.",
        "info"
    )

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: Comandos Básicos CMD")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Qué comando usas para ver el contenido de un directorio?",
            "opciones": ["list", "dir", "show", "ls"],
            "respuesta_correcta": "dir",
            "explicacion": "El comando 'dir' muestra los archivos y directorios en la ubicación actual."
        },
        {
            "pregunta": "¿Cómo cambias al directorio padre (un nivel arriba)?",
            "opciones": ["cd ..", "cd up", "cd parent", "cd back"],
            "respuesta_correcta": "cd ..",
            "explicacion": "El comando 'cd ..' te lleva al directorio padre."
        },
        {
            "pregunta": "¿Qué comando usar para limpiar la pantalla de CMD?",
            "opciones": ["cls", "clear", "clean", "clr"],
            "respuesta_correcta": "cls",
            "explicacion": "El comando 'cls' (clear screen) borra todo el contenido visible en la consola."
        },
        {
            "pregunta": "¿Cuál es la diferencia entre 'del' y 'rmdir'?",
            "opciones": [
                "No hay diferencia",
                "del elimina archivos, rmdir elimina directorios",
                "del elimina directorios, rmdir elimina archivos",
                "Ambos hacen lo mismo"
            ],
            "respuesta_correcta": "del elimina archivos, rmdir elimina directorios",
            "explicacion": "'del' elimina archivos, mientras que 'rmdir' elimina directorios vacíos."
        },
        {
            "pregunta": "Escribe el comando para crear un directorio llamado 'Proyecto':",
            "opciones": ["mkdir Proyecto", "create Proyecto", "makedir Proyecto", "new Proyecto"],
            "respuesta_correcta": "mkdir Proyecto",
            "explicacion": "Usas 'mkdir' (make directory) seguido del nombre del directorio."
        }
    ]
    
    # Crear componente de quiz
    quiz = QuizComponent(quiz_questions)
    
    if quiz.render(key_suffix="cmd_basics_quiz"):
        # Quiz completado, registrar puntuación
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score(
                "02_cmd_basics", 
                quiz.score, 
                100
            )
            st.session_state.progress_tracker.update_module_progress(
                "02_cmd_basics", 
                "quiz_completed"
            )

def render_reference_section():
    """Renderiza la sección de referencia rápida"""
    
    st.markdown("## 📖 Referencia Rápida de Comandos CMD")
    
    # Tabla de comandos básicos
    commands_data = {
        "Comando": [
            "dir", "cd", "cls", "mkdir/md", "rmdir/rd", 
            "copy", "move", "del", "type", "echo", 
            "help", "ver", "date", "time", "exit"
        ],
        "Función": [
            "Listar archivos y directorios",
            "Cambiar directorio",
            "Limpiar pantalla",
            "Crear directorio",
            "Eliminar directorio",
            "Copiar archivos",
            "Mover/renombrar archivos",
            "Eliminar archivos",
            "Mostrar contenido de archivo",
            "Mostrar texto",
            "Mostrar ayuda",
            "Mostrar versión de Windows",
            "Mostrar/cambiar fecha",
            "Mostrar/cambiar hora",
            "Salir de CMD"
        ],
        "Ejemplo": [
            "dir /w",
            "cd Documents",
            "cls",
            "mkdir NuevaCarpeta",
            "rmdir CarpetaVacia",
            "copy archivo.txt backup.txt",
            "move archivo.txt carpeta\\",
            "del archivo.txt",
            "type readme.txt",
            "echo Hola Mundo",
            "help dir",
            "ver",
            "date",
            "time",
            "exit"
        ]
    }
    
    # Protección anti-traducción para tablas
    st.markdown("""
    <style>
    .stTable, .dataframe {
        translate: no !important;
        -webkit-translate: no !important;
    }
    .stTable code, .dataframe code {
        translate: no !important;
        -webkit-translate: no !important;
        font-family: 'Consolas', 'Courier New', monospace !important;
        background-color: #f0f0f0 !important;
        padding: 2px 4px !important;
        border-radius: 3px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.table(commands_data)
    
    st.markdown("---")
    st.markdown("### 🔍 Caracteres Especiales y Comodines")
    
    wildcards_data = {
        "Símbolo": ["*", "?", "..", "\\", ">", ">>"],
        "Significado": [
            "Cualquier cantidad de caracteres",
            "Un solo caracter",
            "Directorio padre",
            "Separador de rutas",
            "Redireccionar salida (sobrescribir)",
            "Redireccionar salida (anexar)"
        ],
        "Ejemplo": [
            "dir *.txt",
            "dir archivo?.txt",
            "cd ..",
            "cd C:\\Users\\Usuario",
            "echo Texto > archivo.txt",
            "echo Más texto >> archivo.txt"
        ]
    }
    
    # Aplicar la misma protección anti-traducción
    st.markdown("""
    <div translate="no" data-translate="no">
    """, unsafe_allow_html=True)
    
    st.table(wildcards_data)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    create_tip_card(
        "📚 ¿Quieres saber más?",
        "Usa 'help comando' para obtener ayuda detallada de cualquier comando. Por ejemplo: 'help dir'",
        "info"
    )

if __name__ == "__main__":
    render_page()
