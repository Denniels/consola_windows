"""
Módulo 09: Resumen y Evaluación Final
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'components'))

from utils.progress_tracker import create_section_header
from components.ui_helpers import create_tip_card

def render_page():
    create_section_header(
        title="Resumen del Curso y Evaluación Final",
        description="Consolida tu aprendizaje y demuestra tu dominio de ambas consolas",
        icon="🎓"
    )
    
    st.success("🏆 **¡Felicitaciones por llegar hasta aquí!**")
    
    st.markdown("""
    ## 📋 Resumen de conocimientos adquiridos
    
    A lo largo de este curso has aprendido:
    
    ### 🟨 CMD (Símbolo del Sistema)
    - ✅ Navegación básica y gestión de archivos
    - ✅ Variables de entorno y configuración
    - ✅ Procesamiento de texto y redirección
    - ✅ Automatización con archivos batch
    
    ### 🔵 PowerShell
    - ✅ Sintaxis moderna orientada a objetos
    - ✅ Gestión avanzada del sistema
    - ✅ Scripts y funciones complejas
    - ✅ Administración profesional
    
    ### 🔄 Integración y Comparación
    - ✅ Cuándo usar cada herramienta
    - ✅ Migración de scripts CMD a PowerShell
    - ✅ Mejores prácticas combinadas
    """)
    
    st.info("🚧 Próximamente incluirá:")
    st.markdown("""
    - **Evaluación final integral**
    - **Certificado de finalización**
    - **Recursos adicionales de estudio**
    - **Proyecto final práctico**
    - **Descargar resumen en PDF**
    """)
    
    create_tip_card(
        "🌟 ¡Continúa practicando!",
        "El dominio real viene con la práctica constante. Sigue experimentando con ambas consolas en tus proyectos diarios.",
        "success"
    )
    
    if 'progress_tracker' in st.session_state:
        st.session_state.progress_tracker.update_module_progress("09_summary", "viewed")

if __name__ == "__main__":
    render_page()
