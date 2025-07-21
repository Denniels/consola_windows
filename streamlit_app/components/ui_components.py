"""
Componentes reutilizables para la interfaz de usuario - Versión Modular Simplificada
Este archivo now sirve como hub central de imports
"""

import streamlit as st
import pandas as pd
import sys
import os
from typing import List, Dict, Optional

# Agregar paths necesarios
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

# Solo las clases que realmente necesitamos aquí
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


# Importar todas las funciones helper desde ui_helpers
try:
    from ui_helpers import *
except ImportError:
    # Funciones helper simplificadas si no se pueden importar
    def create_info_box(title, content, icon="ℹ️"):
        st.info(f"{icon} **{title}**\n\n{content}")
    
    def create_tip_card(title, content, tip_type="info"):
        if tip_type == "info":
            st.info(f"**{title}**\n\n{content}")
        elif tip_type == "success":
            st.success(f"**{title}**\n\n{content}")
        elif tip_type == "warning":
            st.warning(f"**{title}**\n\n{content}")
        elif tip_type == "error":
            st.error(f"**{title}**\n\n{content}")

# Importar componentes dinámicamente solo cuando se necesiten
def get_quiz_component():
    """Importar QuizComponent dinámicamente"""
    try:
        from quiz_components import QuizComponent
        return QuizComponent
    except ImportError:
        return None

def get_console_simulator():
    """Importar ConsoleSimulator dinámicamente"""
    try:
        from console_components import ConsoleSimulator
        return ConsoleSimulator
    except ImportError:
        return None

def get_command_practice_component():
    """Importar CommandPracticeComponent dinámicamente"""
    try:
        from quiz_components import CommandPracticeComponent
        return CommandPracticeComponent
    except ImportError:
        return None

# Hacer disponibles las clases principales para import directo
try:
    import sys
    import os
    # Asegurar que el path está disponible
    current_dir = os.path.dirname(__file__)
    sys.path.insert(0, current_dir)
    
    # Importar usando imports absolutos directos
    from console_components import ConsoleSimulator
    from quiz_components import QuizComponent, CommandPracticeComponent
    print("✅ Componentes originales importados correctamente")
        
except ImportError as e:
    print(f"⚠️ Error importing components: {e}")
    ConsoleSimulator = None
    QuizComponent = None
    CommandPracticeComponent = None

# Crear versiones alternativas si los imports fallan
if ConsoleSimulator is None:
    class ConsoleSimulator:
        """Versión simplificada del simulador de consola"""
        def __init__(self, console_type="cmd"):
            self.console_type = console_type
            
        def render(self, commands=None):
            st.info("🔧 Simulador de consola en mantenimiento. Funcionalidad limitada.")
            if commands:
                for cmd in commands:
                    st.code(f"{self.console_type}> {cmd}", language="bash")

if QuizComponent is None:
    class QuizComponent:
        """Versión simplificada del componente de quiz"""
        def __init__(self, questions):
            self.questions = questions
            
        def render(self, key_suffix: str = ""):
            st.info("🔧 Componente de quiz en mantenimiento. Funcionalidad limitada.")
            st.write("📚 **Preguntas disponibles:**")
            for i, q in enumerate(self.questions):
                st.write(f"{i+1}. {q.get('pregunta', 'Pregunta sin texto')}")

if CommandPracticeComponent is None:
    class CommandPracticeComponent:
        """Versión simplificada del componente de práctica"""
        def __init__(self, commands):
            self.commands = commands
            
        def render(self, key_suffix: str = ""):
            st.info("🔧 Componente de práctica en mantenimiento. Funcionalidad limitada.")
            st.write("💻 **Ejercicios disponibles:**")
            for i, cmd in enumerate(self.commands):
                st.write(f"{i+1}. {cmd.get('descripcion', 'Ejercicio sin descripción')}")
