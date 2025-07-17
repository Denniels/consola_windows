"""
Módulo 03: Comandos Básicos en PowerShell
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
    """Renderiza la página de comandos básicos PowerShell"""
    
    # Header principal
    create_section_header(
        title="Comandos Básicos en PowerShell",
        description="Descubre la potencia de PowerShell con cmdlets estructurados y orientados a objetos",
        icon="🔵"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Entender la sintaxis Verbo-Sustantivo de PowerShell",
        "Dominar cmdlets básicos de navegación y administración",
        "Aprender a usar Get-Help para obtener información",
        "Comprender la diferencia con CMD en filosofía y funcionamiento"
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
        st.session_state.progress_tracker.update_module_progress("03_powershell_basics", "powershell_basics_viewed")

def render_theory_section():
    """Renderiza la sección de teoría"""
    
    st.markdown("## 🔤 Filosofía de PowerShell: Verbo-Sustantivo")
    
    create_info_card(
        "🎯 Estructura de Cmdlets",
        "PowerShell usa la sintaxis Verbo-Sustantivo para todos sus comandos. Ejemplos: Get-Process, Set-Location, New-Item. Esto hace que los comandos sean más descriptivos y fáciles de recordar.",
        "💡"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Verbos Comunes")
        st.markdown("""
        - **Get** - Obtener información
        - **Set** - Establecer/cambiar valores
        - **New** - Crear elementos nuevos
        - **Remove** - Eliminar elementos
        - **Start** - Iniciar procesos/servicios
        - **Stop** - Detener procesos/servicios
        - **Test** - Probar/verificar estado
        """)
    
    with col2:
        st.markdown("### 📋 Sustantivos Comunes")
        st.markdown("""
        - **Process** - Procesos del sistema
        - **Service** - Servicios de Windows
        - **ChildItem** - Archivos y directorios
        - **Content** - Contenido de archivos
        - **Location** - Ubicación/directorio actual
        - **Help** - Sistema de ayuda
        - **Command** - Comandos disponibles
        """)
    
    st.markdown("---")
    st.markdown("## 🗂️ Cmdlets de Navegación y Archivos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `Get-ChildItem` - Listar contenido")
        st.code("""Get-ChildItem
Get-ChildItem -Path C:\\Users
Get-ChildItem *.txt""", language="powershell")
        st.markdown("""
        **Función:** Equivalente a `dir` en CMD, pero más potente
        
        **Alias:** `gci`, `ls`, `dir`
        **Parámetros útiles:**
        - `-Recurse` - Buscar en subdirectorios
        - `-Filter` - Filtrar por patrón
        - `-Hidden` - Incluir archivos ocultos
        """)
        
        st.markdown("### `Set-Location` - Cambiar directorio")
        st.code("""Set-Location C:\\Users
Set-Location ..
Set-Location ~""", language="powershell")
        st.markdown("""
        **Función:** Cambia el directorio actual
        
        **Alias:** `sl`, `cd`, `chdir`
        **Nota:** `~` representa el directorio home del usuario
        """)
    
    with col2:
        st.markdown("### `Get-Location` - Directorio actual")
        st.code("Get-Location", language="powershell")
        st.markdown("**Alias:** `gl`, `pwd`")
        
        st.markdown("### `Clear-Host` - Limpiar pantalla")
        st.code("Clear-Host", language="powershell")
        st.markdown("**Alias:** `cls`, `clear`")
        
        st.markdown("### `Write-Output` - Mostrar texto")
        st.code("""Write-Output "Hola PowerShell"
Write-Output $env:USERNAME""", language="powershell")
        st.markdown("**Alias:** `echo`, `write`")
    
    st.markdown("---")
    st.markdown("## 📁 Cmdlets de Manipulación de Archivos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `New-Item` - Crear elementos")
        st.code("""New-Item -ItemType Directory -Name "NuevaCarpeta"
New-Item -ItemType File -Name "archivo.txt"
New-Item -Path "C:\\Temp\\test.txt" -ItemType File""", language="powershell")
        
        st.markdown("### `Copy-Item` - Copiar elementos")
        st.code("""Copy-Item "archivo.txt" "backup.txt"
Copy-Item "*.txt" "C:\\Backup\\" -Recurse""", language="powershell")
        
        st.markdown("### `Move-Item` - Mover/renombrar")
        st.code("""Move-Item "archivo.txt" "NuevaCarpeta\\"
Move-Item "viejo.txt" "nuevo.txt\"""", language="powershell")
    
    with col2:
        st.markdown("### `Remove-Item` - Eliminar elementos")
        st.code("""Remove-Item "archivo.txt"
Remove-Item "Carpeta" -Recurse
Remove-Item "*.tmp" -Force""", language="powershell")
        
        st.markdown("### `Get-Content` - Leer archivos")
        st.code("""Get-Content "archivo.txt"
Get-Content "log.txt" -Tail 10""", language="powershell")
        
        st.markdown("### `Set-Content` - Escribir archivos")
        st.code("""Set-Content "archivo.txt" "Nuevo contenido"
"Texto" | Set-Content "archivo.txt\"""", language="powershell")
    
    create_tip_card(
        "🔥 Poder de los Objetos",
        "A diferencia de CMD que trabaja con texto, PowerShell trabaja con objetos. Esto significa que puedes acceder a propiedades y métodos de los elementos que obtienes.",
        "success"
    )
    
    st.markdown("---")
    st.markdown("## 🔧 Cmdlets de Sistema y Administración")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### `Get-Process` - Procesos activos")
        st.code("""Get-Process
Get-Process notepad
Get-Process | Where-Object {$_.CPU -gt 100}""", language="powershell")
        
        st.markdown("### `Get-Service` - Servicios")
        st.code("""Get-Service
Get-Service -Name "Spooler"
Get-Service | Where-Object {$_.Status -eq "Running"}""", language="powershell")
        
        st.markdown("### `Test-Connection` - Ping mejorado")
        st.code("""Test-Connection google.com
Test-Connection -ComputerName google.com -Count 2""", language="powershell")
    
    with col2:
        st.markdown("### `Get-Help` - Sistema de ayuda")
        st.code("""Get-Help
Get-Help Get-Process
Get-Help Get-Process -Examples
Get-Help Get-Process -Full""", language="powershell")
        
        st.markdown("### `Get-Command` - Comandos disponibles")
        st.code("""Get-Command
Get-Command *Process*
Get-Command -Verb Get""", language="powershell")
        
        st.markdown("### `Get-Date` - Fecha y hora")
        st.code("""Get-Date
Get-Date -Format "yyyy-MM-dd HH:mm:ss\"""", language="powershell")

def render_practice_section():
    """Renderiza la sección de práctica"""
    
    st.markdown("## 🎯 Simulador de PowerShell")
    st.markdown("Practica los cmdlets en este simulador que imita el comportamiento real de PowerShell:")
    
    # Crear simulador de PowerShell
    ps_simulator = ConsoleSimulator("powershell")
    ps_simulator.render(key_suffix="ps_basics")
    
    st.markdown("---")
    st.markdown("## 🏆 Ejercicios Prácticos")
    
    # Definir ejercicios prácticos
    practice_commands = [
        {
            "descripcion": "Lista archivos y directorios usando el cmdlet Get-ChildItem",
            "ejemplo": "Get-ChildItem",
            "comando": "Get-ChildItem",
            "tipo_consola": "powershell",
            "pista": "Get-ChildItem es equivalente a 'dir' en CMD",
            "solucion": "Get-ChildItem - Lista archivos y carpetas del directorio actual"
        },
        {
            "descripcion": "Muestra la ubicación actual donde te encuentras",
            "ejemplo": "Get-Location",
            "comando": "Get-Location",
            "tipo_consola": "powershell",
            "pista": "Get-Location es como 'pwd' en otros sistemas",
            "solucion": "Get-Location - Muestra el directorio de trabajo actual"
        },
        {
            "descripcion": "Muestra información sobre los procesos en ejecución",
            "ejemplo": "Get-Process",
            "comando": "Get-Process",
            "tipo_consola": "powershell",
            "pista": "Get-Process lista todos los procesos activos",
            "solucion": "Get-Process - Lista procesos en ejecución en el sistema"
        },
        {
            "descripcion": "Obtén ayuda sobre el cmdlet Get-ChildItem",
            "ejemplo": "Get-Help Get-ChildItem",
            "comando": "Get-Help",
            "tipo_consola": "powershell",
            "pista": "Get-Help seguido de cualquier cmdlet te da información",
            "solucion": "Get-Help Get-ChildItem - Muestra ayuda sobre este cmdlet"
        },
        {
            "descripcion": "Muestra el mensaje 'Aprendiendo PowerShell' en la consola",
            "ejemplo": "Write-Output 'Aprendiendo PowerShell'",
            "comando": "Write-Output",
            "tipo_consola": "powershell",
            "pista": "Write-Output es como 'echo' pero más potente",
            "solucion": "Write-Output 'Aprendiendo PowerShell' - Muestra texto en consola"
        },
        {
            "descripcion": "Lista los servicios de Windows en el sistema",
            "ejemplo": "Get-Service",
            "comando": "Get-Service",
            "tipo_consola": "powershell",
            "pista": "Get-Service muestra todos los servicios de Windows",
            "solucion": "Get-Service - Lista servicios del sistema operativo"
        }
    ]
    
    # Componente de práctica
    practice_component = CommandPracticeComponent(practice_commands)
    practice_component.render(key_suffix="ps_practice")
    
    create_tip_card(
        "💡 Tip: Usa Tab para autocompletar",
        "PowerShell tiene excelente autocompletado. Escribe las primeras letras de un cmdlet y presiona Tab para ver opciones.",
        "info"
    )

def render_quiz_section():
    """Renderiza la sección de quiz"""
    
    st.markdown("## 🧩 Evaluación: Comandos Básicos PowerShell")
    
    # Definir preguntas del quiz
    quiz_questions = [
        {
            "pregunta": "¿Cuál es la estructura básica de los cmdlets en PowerShell?",
            "opciones": ["Sustantivo-Verbo", "Verbo-Sustantivo", "Comando-Argumento", "Función-Parámetro"],
            "respuesta_correcta": "Verbo-Sustantivo",
            "explicacion": "PowerShell usa la sintaxis Verbo-Sustantivo, como Get-Process, Set-Location, etc."
        },
        {
            "pregunta": "¿Qué cmdlet usas para ver el contenido de un directorio?",
            "opciones": ["Get-Directory", "Get-ChildItem", "Get-Files", "List-Items"],
            "respuesta_correcta": "Get-ChildItem",
            "explicacion": "Get-ChildItem es el equivalente de 'dir' en CMD."
        },
        {
            "pregunta": "¿Cuál es el cmdlet para obtener ayuda sobre Get-Process?",
            "opciones": ["Get-Help Get-Process", "Help Get-Process", "? Get-Process", "Todas las anteriores"],
            "respuesta_correcta": "Todas las anteriores",
            "explicacion": "Get-Help, Help y ? son formas válidas de obtener ayuda en PowerShell."
        },
        {
            "pregunta": "¿Cuál es el alias de Set-Location?",
            "opciones": ["sl", "cd", "chdir", "Todas las anteriores"],
            "respuesta_correcta": "Todas las anteriores",
            "explicacion": "PowerShell mantiene compatibilidad con comandos conocidos mediante alias."
        },
        {
            "pregunta": "¿Qué cmdlet usas para ver los procesos en ejecución?",
            "opciones": ["Get-Process", "Show-Process", "List-Process", "View-Process"],
            "respuesta_correcta": "Get-Process",
            "explicacion": "Get-Process muestra todos los procesos activos en el sistema."
        },
        {
            "pregunta": "¿Cuál es la principal diferencia entre PowerShell y CMD?",
            "opciones": [
                "PowerShell es más rápido",
                "PowerShell trabaja con objetos, CMD con texto",
                "PowerShell solo funciona en Windows 10",
                "No hay diferencias importantes"
            ],
            "respuesta_correcta": "PowerShell trabaja con objetos, CMD con texto",
            "explicacion": "Esta es la diferencia fundamental: PowerShell es orientado a objetos."
        }
    ]
    
    # Crear componente de quiz
    quiz = QuizComponent(quiz_questions)
    
    if quiz.render(key_suffix="ps_basics_quiz"):
        # Quiz completado, registrar puntuación
        if 'progress_tracker' in st.session_state:
            st.session_state.progress_tracker.add_quiz_score(
                "03_powershell_basics", 
                quiz.score, 
                100
            )
            st.session_state.progress_tracker.update_module_progress(
                "03_powershell_basics", 
                "quiz_completed"
            )

def render_reference_section():
    """Renderiza la sección de referencia rápida"""
    
    st.markdown("## 📖 Referencia Rápida de Cmdlets PowerShell")
    
    # Tabla de cmdlets básicos
    cmdlets_data = {
        "Cmdlet": [
            "Get-ChildItem", "Set-Location", "Get-Location", "Clear-Host",
            "New-Item", "Remove-Item", "Copy-Item", "Move-Item",
            "Get-Content", "Set-Content", "Get-Process", "Get-Service",
            "Get-Help", "Get-Command", "Write-Output", "Test-Connection"
        ],
        "Función": [
            "Listar archivos y directorios",
            "Cambiar directorio",
            "Mostrar directorio actual",
            "Limpiar pantalla",
            "Crear archivos/directorios",
            "Eliminar elementos",
            "Copiar elementos",
            "Mover/renombrar elementos",
            "Leer contenido de archivos",
            "Escribir contenido a archivos",
            "Mostrar procesos",
            "Mostrar servicios",
            "Obtener ayuda",
            "Listar comandos disponibles",
            "Mostrar texto",
            "Probar conectividad de red"
        ],
        "Alias Comunes": [
            "gci, ls, dir", "sl, cd", "gl, pwd", "cls",
            "ni", "ri, del", "ci, cp", "mi, mv",
            "gc, cat", "sc", "gps, ps", "gsv",
            "help, man", "gcm", "echo, write", "ping"
        ]
    }
    
    # Protección anti-traducción para cmdlets
    st.markdown("""
    <style>
    .stTable, .dataframe {
        translate: no !important;
        -webkit-translate: no !important;
    }
    .stTable code, .dataframe code, .stTable td, .dataframe td {
        translate: no !important;
        -webkit-translate: no !important;
        font-family: 'Consolas', 'Courier New', monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div translate="no" data-translate="no">', unsafe_allow_html=True)
    st.table(cmdlets_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔍 Parámetros Comunes")
    
    parameters_data = {
        "Parámetro": ["-Path", "-Name", "-Recurse", "-Force", "-Filter", "-WhatIf"],
        "Descripción": [
            "Especifica la ruta del elemento",
            "Especifica el nombre del elemento",
            "Incluye subdirectorios",
            "Fuerza la operación",
            "Filtra por patrón",
            "Muestra qué haría sin ejecutar"
        ],
        "Ejemplo": [
            "Get-ChildItem -Path C:\\Users",
            "New-Item -Name 'test.txt'",
            "Get-ChildItem -Recurse",
            "Remove-Item -Force",
            "Get-ChildItem -Filter '*.txt'",
            "Remove-Item -WhatIf"
        ]
    }
    
    st.markdown('<div translate="no" data-translate="no">', unsafe_allow_html=True)
    st.table(parameters_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Verbos Más Comunes en PowerShell")
    
    col1, col2 = st.columns(2)
    
    with col1:
        verbs_data = {
            "Verbo": ["Get", "Set", "New", "Remove", "Start", "Stop"],
            "Propósito": [
                "Obtener/consultar información",
                "Establecer/cambiar valores",
                "Crear nuevos elementos",
                "Eliminar elementos",
                "Iniciar procesos/servicios",
                "Detener procesos/servicios"
            ]
        }
        st.markdown('<div translate="no" data-translate="no">', unsafe_allow_html=True)
        st.table(verbs_data)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        create_tip_card(
            "🔍 Descubrir más cmdlets",
            "Usa 'Get-Command -Verb Get' para ver todos los cmdlets que empiezan con Get, o 'Get-Command *Process*' para buscar cmdlets relacionados con procesos.",
            "info"
        )
    
    create_tip_card(
        "📚 Recursos adicionales",
        "PowerShell tiene documentación excelente. Usa 'Get-Help about_*' para ver temas conceptuales, como 'Get-Help about_Variables'.",
        "success"
    )

if __name__ == "__main__":
    render_page()
