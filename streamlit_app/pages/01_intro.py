"""
Módulo 01: Introducción a las Consolas Windows
"""

import streamlit as st
import sys
import os

# Agregar paths necesarios
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from progress_tracker import create_section_header, create_info_card
from ui_components import create_learning_objective_card, create_tip_card

def render_page():
    """Renderiza la página de introducción"""
    
    # Header principal
    create_section_header(
        title="Introducción a las Consolas Windows",
        description="Descubre el poder de CMD y PowerShell para automatizar y administrar Windows",
        icon="🏠"
    )
    
    # Objetivos de aprendizaje
    objectives = [
        "Comprender qué es una consola y para qué sirve",
        "Conocer las diferencias entre CMD y PowerShell",
        "Aprender cuándo usar cada consola",
        "Familiarizarse con la interfaz de cada terminal"
    ]
    create_learning_objective_card(objectives)
    
    # Contenido principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🖥️ ¿Qué es una Consola?")
        st.markdown("""
        Una **consola** o **terminal** es una interfaz de línea de comandos que te permite interactuar con el sistema operativo usando texto en lugar de hacer clic en iconos. Es una herramienta poderosa que los profesionales de IT utilizan para:
        
        - **Automatizar tareas repetitivas**
        - **Administrar sistemas remotos**
        - **Ejecutar scripts y programas**
        - **Diagnosticar problemas del sistema**
        - **Realizar tareas avanzadas de administración**
        """)
        
        st.markdown("## ⚫ CMD (Command Prompt)")
        st.markdown("""
        **CMD** es el intérprete de comandos tradicional de Windows, heredado de MS-DOS. Características:
        
        - **Simplicidad:** Comandos directos y sencillos
        - **Compatibilidad:** Funciona en todas las versiones de Windows
        - **Velocidad:** Excelente para tareas básicas y scripts batch
        - **Limitaciones:** Menos potente para tareas complejas
        """)
        
        create_tip_card(
            "💡 ¿Cuándo usar CMD?",
            "Perfecto para tareas básicas como navegar directorios, copiar archivos, ejecutar programas simples y crear scripts batch (.bat).",
            "info"
        )
        
        st.markdown("## 🔵 PowerShell")
        st.markdown("""
        **PowerShell** es la consola moderna de Microsoft, diseñada para administradores de sistemas y desarrolladores. Características:
        
        - **Potencia:** Lenguaje de scripting completo
        - **Objetos:** Trabaja con objetos .NET, no solo texto
        - **Cmdlets:** Comandos estructurados y consistentes
        - **Automatización:** Ideal para tareas complejas y administración
        """)
        
        create_tip_card(
            "🚀 ¿Cuándo usar PowerShell?",
            "Ideal para administración avanzada, automatización, manejo de servicios de Windows, Active Directory y tareas que requieren programación.",
            "success"
        )
    
    with col2:
        st.markdown("### 📊 Comparación Rápida")
        
        comparison_data = {
            "Aspecto": ["Año de creación", "Tipo", "Sintaxis", "Potencia", "Curva de aprendizaje"],
            "CMD": ["1981", "Intérprete simple", "Comando argumentos", "Básica", "Fácil"],
            "PowerShell": ["2006", "Shell + lenguaje", "Verbo-Sustantivo", "Avanzada", "Moderada"]
        }
        
        st.table(comparison_data)
        
        st.markdown("### 🎯 Tu Camino de Aprendizaje")
        st.info("""
        **Recomendación:**
        1. Comienza con CMD para entender conceptos básicos
        2. Aprende PowerShell para tareas avanzadas
        3. Usa ambas según la situación
        """)
        
        st.markdown("### 📈 Estadísticas de Uso")
        st.metric("Profesionales IT que usan consolas", "85%")
        st.metric("Tiempo ahorrado con automatización", "60%")
        st.metric("Tareas que se pueden automatizar", "90%")
    
    # Sección de ejemplos visuales
    st.markdown("---")
    st.markdown("## 👀 Primeros Vistazo a las Consolas")
    
    tab1, tab2 = st.tabs(["🖤 CMD", "🔷 PowerShell"])
    
    with tab1:
        st.markdown("### Aspecto de CMD")
        st.code("""
C:\\Users\\Usuario>dir
 El volumen de la unidad C es Windows
 El número de serie del volumen es: A1B2-C3D4

 Directorio de C:\\Users\\Usuario

22/12/2024  14:30    <DIR>          Desktop
22/12/2024  09:45    <DIR>          Documents
22/12/2024  11:20    <DIR>          Downloads
               3 dirs   25,789,456,384 bytes libres

C:\\Users\\Usuario>echo Hola Mundo
Hola Mundo
        """, language="batch")
        
        st.markdown("**Características de CMD:**")
        st.markdown("- Fondo negro, texto blanco")
        st.markdown("- Prompt simple: `C:\\ruta>`")
        st.markdown("- Comandos cortos y directos")
    
    with tab2:
        st.markdown("### Aspecto de PowerShell")
        st.code("""
PS C:\\Users\\Usuario> Get-ChildItem

    Directorio: C:\\Users\\Usuario

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        22/12/2024     14:30                Desktop
d-----        22/12/2024      9:45                Documents
d-----        22/12/2024     11:20                Downloads

PS C:\\Users\\Usuario> Write-Output "Hola Mundo"
Hola Mundo

PS C:\\Users\\Usuario> Get-Process | Where-Object {$_.Name -eq "notepad"}
        """, language="powershell")
        
        st.markdown("**Características de PowerShell:**")
        st.markdown("- Fondo azul oscuro, texto blanco")
        st.markdown("- Prompt: `PS C:\\ruta>`")
        st.markdown("- Cmdlets estructurados (Verbo-Sustantivo)")
    
    # Sección de preparación
    st.markdown("---")
    st.markdown("## 🎓 Prepárate para Aprender")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🧠 Mentalidad")
        st.markdown("""
        - **Paciencia:** Es normal cometer errores al principio
        - **Práctica:** La repetición es clave
        - **Curiosidad:** Experimenta con comandos seguros
        """)
    
    with col2:
        st.markdown("### 📚 Recursos")
        st.markdown("""
        - **Ayuda integrada:** `help` en CMD, `Get-Help` en PowerShell
        - **Este curso:** Ejemplos y práctica guiada
        - **Documentación oficial:** Microsoft Docs
        """)
    
    with col3:
        st.markdown("### ⚠️ Precauciones")
        st.markdown("""
        - **No ejecutes comandos desconocidos**
        - **Haz respaldos importantes**
        - **Usa cuentas sin privilegios para practicar**
        """)
    
    # Próximos pasos
    create_tip_card(
        "🚀 ¿Listo para continuar?",
        "En el siguiente módulo comenzaremos con comandos básicos de CMD. ¡Empezarás a usar la consola de inmediato!",
        "success"
    )
    
    # Marcar progreso
    if 'progress_tracker' in st.session_state:
        st.session_state.progress_tracker.update_module_progress("01_intro", "introduction_completed")
    
    # Navegación rápida
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("➡️ Comenzar con CMD Básico", type="primary"):
            st.session_state.current_page = "02_cmd_basics"
            st.rerun()

if __name__ == "__main__":
    render_page()
