"""
Componentes reutilizables para la interfaz de usuario - Versión Modular
Este archivo ahora actúa como hub central de imports para mantener compatibilidad
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Optional

# Importar componentes desde módulos especializados
from .quiz_components import QuizComponent, CommandPracticeComponent
from .console_components import ConsoleSimulator
from .ui_helpers import *

# Mantener solo los componentes específicos que pertenecen aquí
class NavigationComponent:
    """Componente de navegación principal"""
    
    @staticmethod
    def render_sidebar():
        """Renderiza la barra lateral con navegación"""
        st.sidebar.title("🖥️ Consola Windows")
        st.sidebar.markdown("---")
        
        # Información del usuario
        if 'user_data' in st.session_state and st.session_state.user_data:
            st.sidebar.success(f"👤 {st.session_state.user_data['name']}")
            st.sidebar.markdown(f"📧 {st.session_state.user_data['email']}")
            st.sidebar.markdown("---")
        
        # Enlaces de navegación
        st.sidebar.markdown("### 📚 Contenido")
        st.sidebar.markdown("1. [Introducción](./01_intro)")
        st.sidebar.markdown("2. [CMD Básico](./02_cmd_basics)")
        st.sidebar.markdown("3. [PowerShell Básico](./03_powershell_basics)")
        st.sidebar.markdown("4. [CMD Intermedio](./04_intermediate_cmd)")
        st.sidebar.markdown("5. [PowerShell Intermedio](./05_intermediate_ps)")
        st.sidebar.markdown("6. [CMD Avanzado](./06_advanced_cmd)")
        st.sidebar.markdown("7. [PowerShell Avanzado](./07_advanced_ps)")
        st.sidebar.markdown("8. [Evaluaciones](./08_evaluations)")
        st.sidebar.markdown("9. [Resumen](./09_summary)")


class ProgressCard:
    """Tarjeta de progreso del usuario"""
    
    @staticmethod
    def render(progress_data: Dict):
        """Renderiza una tarjeta de progreso"""
        if not progress_data:
            st.info("No hay datos de progreso disponibles")
            return
            
        total_sections = len(progress_data.get('sections', {}))
        completed_sections = sum(1 for section in progress_data.get('sections', {}).values() 
                               if section.get('completed', False))
        
        progress_percentage = (completed_sections / total_sections * 100) if total_sections > 0 else 0
        
        st.markdown("### 📊 Tu Progreso")
        st.progress(progress_percentage / 100)
        st.markdown(f"**{completed_sections}/{total_sections} secciones completadas ({progress_percentage:.1f}%)**")
        
        # Mostrar secciones completadas
        if progress_data.get('sections'):
            with st.expander("Ver detalles del progreso"):
                for section_name, section_data in progress_data['sections'].items():
                    status = "✅" if section_data.get('completed', False) else "⏳"
                    st.markdown(f"{status} {section_name}")
                    
                    if section_data.get('quiz_results'):
                        for quiz_name, result in section_data['quiz_results'].items():
                            score_text = f"({result['score']}/{result['total']})"
                            st.markdown(f"   📝 {quiz_name}: {score_text}")