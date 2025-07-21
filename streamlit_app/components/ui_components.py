"""
Componentes reutilizables para la interfaz de usuario
"""

import streamlit as st
import pandas as pd
import sys
import os
from typing import List, Dict, Optional, Callable

# Agregar paths para imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from command_parser import CommandParser
from progress_tracker import ProgressTracker

class ConsoleSimulator:
    """Simulador de consola interactivo con formateo consistente"""
    
    def __init__(self, console_type: str = "cmd"):
        self.console_type = console_type
        self.parser = CommandParser()
        self._initialize_history()
    
    def _initialize_history(self):
        """Inicializa el historial de la consola en session state"""
        if f'{self.console_type}_history' not in st.session_state:
            st.session_state[f'{self.console_type}_history'] = []
        
        self.history = st.session_state[f'{self.console_type}_history']
    
    def _build_console_text(self, console_type: str):
        """Construye el contenido de texto plano de la consola con formateo correcto"""
        if console_type == "cmd":
            if not self.history:
                return "Microsoft Windows [Versión 10.0.19045.3570]\n(c) Microsoft Corporation. Todos los derechos reservados.\n\nC:\\Users\\Usuario>"
            
            lines = [
                "Microsoft Windows [Versión 10.0.19045.3570]",
                "(c) Microsoft Corporation. Todos los derechos reservados.",
                ""
            ]
            
            for entry in self.history:
                lines.append(f"C:\\Users\\Usuario>{entry['command']}")
                # Asegurar que cada línea de output se muestre correctamente
                output_lines = entry['output'].split('\n')
                for line in output_lines:
                    lines.append(line)
                lines.append("")
            
            lines.append("C:\\Users\\Usuario>")
            return '\n'.join(lines)
        
        else:  # PowerShell
            if not self.history:
                return "Windows PowerShell\nCopyright (C) Microsoft Corporation. Todos los derechos reservados.\n\nPS C:\\Users\\Usuario>"
            
            lines = [
                "Windows PowerShell",
                "Copyright (C) Microsoft Corporation. Todos los derechos reservados.",
                ""
            ]
            
            for entry in self.history:
                lines.append(f"PS C:\\Users\\Usuario>{entry['command']}")
                # Asegurar que cada línea de output se muestre correctamente
                output_lines = entry['output'].split('\n')
                for line in output_lines:
                    lines.append(line)
                lines.append("")
            
            lines.append("PS C:\\Users\\Usuario>")
            return '\n'.join(lines)
    
    def _apply_console_styles(self, console_type: str):
        """Aplica estilos CSS específicos para cada tipo de consola"""
        if console_type == "cmd":
            st.markdown("""
            <style>
            div[data-testid="stCodeBlock"] {
                background-color: #000000 !important;
                border: 1px solid #333333 !important;
                border-radius: 4px !important;
            }
            div[data-testid="stCodeBlock"] code {
                color: #c0c0c0 !important;
                background-color: #000000 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                font-size: 14px !important;
                line-height: 1.2 !important;
                white-space: pre !important;
            }
            </style>
            """, unsafe_allow_html=True)
        else:  # PowerShell
            st.markdown("""
            <style>
            div[data-testid="stCodeBlock"] {
                background-color: #012456 !important;
                border: 1px solid #1e3a5f !important;
                border-radius: 4px !important;
            }
            div[data-testid="stCodeBlock"] code {
                color: #ffffff !important;
                background-color: #012456 !important;
                font-family: 'Consolas', 'Courier New', monospace !important;
                font-size: 14px !important;
                line-height: 1.2 !important;
                white-space: pre !important;
            }
            </style>
            """, unsafe_allow_html=True)
    
    def _render_cmd_console(self, height: int, key_suffix: str):
        """Renderiza la consola CMD con formateo mejorado"""
        
        # Aplicar estilos CSS
        self._apply_console_styles("cmd")
        
        # Construir contenido de texto plano
        console_text = self._build_console_text("cmd")
        
        # Mostrar en un code block que preserva formato
        st.code(console_text, language=None)
        
        # Campo de entrada
        command = st.text_input(
            "Escribe un comando CMD:", 
            key=f"cmd_input_{key_suffix}", 
            placeholder="Ej: dir, cd, echo Hola",
            help="Presiona Enter o haz clic en Ejecutar para correr el comando"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("🚀 Ejecutar", key=f"cmd_execute_{key_suffix}", type="primary") and command:
                self._execute_command(command)
                st.rerun()
        with col2:
            if st.button("🗑️ Limpiar", key=f"cmd_clear_{key_suffix}"):
                self.clear_history()
                st.rerun()
    
    def _render_ps_console(self, height: int, key_suffix: str):
        """Renderiza la consola PowerShell con formateo mejorado"""
        
        # Aplicar estilos CSS
        self._apply_console_styles("powershell")
        
        # Construir contenido de texto plano
        console_text = self._build_console_text("powershell")
        
        # Mostrar en un code block que preserva formato
        st.code(console_text, language=None)
        
        # Campo de entrada
        command = st.text_input(
            "Escribe un comando PowerShell:", 
            key=f"ps_input_{key_suffix}", 
            placeholder="Ej: Get-ChildItem, Get-Date, Write-Host Hola",
            help="Presiona Enter o haz clic en Ejecutar para correr el comando"
        )
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("🚀 Ejecutar", key=f"ps_execute_{key_suffix}", type="primary") and command:
                self._execute_command(command)
                st.rerun()
        with col2:
            if st.button("🗑️ Limpiar", key=f"ps_clear_{key_suffix}"):
                self.clear_history()
                st.rerun()
    
    def render(self, height: int = 400, key_suffix: str = ""):
        """Renderiza la consola según el tipo"""
        # Agregar título de la consola
        if self.console_type == "cmd":
            st.markdown("### 🖤 Consola CMD")
            self._render_cmd_console(height, key_suffix)
        else:
            st.markdown("### 🔷 Consola PowerShell")
            self._render_ps_console(height, key_suffix)
    
    def _execute_command(self, command: str):
        """Ejecuta un comando y agrega el resultado al historial"""
        output = self.parser.parse_command(command, self.console_type)
        
        # Agregar al historial
        self.history.append({
            'command': command,
            'output': output
        })
        
        # Actualizar session state
        st.session_state[f'{self.console_type}_history'] = self.history
    
    def clear_history(self):
        """Limpia el historial de la consola"""
        self.history = []
        st.session_state[f'{self.console_type}_history'] = []

class QuizComponent:
    """Componente para cuestionarios interactivos"""
    
    def __init__(self, questions: List[Dict]):
        self.questions = questions
        self._score = 0
    
    @property
    def score(self):
        """Devuelve la puntuación actual del quiz"""
        return self._score
    
    def calculate_score(self, answers: Dict, key_suffix: str = "") -> int:
        """
        Calcula la puntuación basada en las respuestas
        
        Args:
            answers: Diccionario con las respuestas del usuario
            key_suffix: Sufijo para identificar las respuestas específicas
        
        Returns:
            Puntuación como porcentaje (0-100)
        """
        if not answers or not self.questions:
            return 0
        
        correct_answers = 0
        total_questions = len(self.questions)
        
        for i, question in enumerate(self.questions):
            if i in answers and answers[i] == question["respuesta_correcta"]:
                correct_answers += 1
        
        self._score = int((correct_answers / total_questions) * 100)
        return self._score
        
    def render(self, key_suffix: str = ""):
        """Renderiza el quiz con protección anti-traducción mejorada"""
        if not self.questions:
            st.error("No hay preguntas disponibles")
            return
        
        # CSS específico simplificado para proteger comandos
        st.markdown("""
        <style>
        .stCode {
            translate: no !important;
            -webkit-translate: no !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Session state management
        question_key = f"quiz_current_{key_suffix}"
        answer_key = f"quiz_answer_{key_suffix}"
        completed_key = f"quiz_completed_{key_suffix}"
        
        if question_key not in st.session_state:
            st.session_state[question_key] = 0
        if answer_key not in st.session_state:
            st.session_state[answer_key] = {}
        if completed_key not in st.session_state:
            st.session_state[completed_key] = False
        
        current_question = st.session_state[question_key]
        
        # Validación para evitar IndexError
        if current_question >= len(self.questions):
            st.session_state[question_key] = 0
            current_question = 0
        elif current_question < 0:
            st.session_state[question_key] = 0
            current_question = 0
            
        question = self.questions[current_question]
        
        # Título y pregunta
        st.subheader(f"Pregunta {current_question + 1} de {len(self.questions)}")
        st.write(question["pregunta"])
        
        st.write("**Selecciona la opción correcta:**")
        
        # Mostrar opciones con protección robusta anti-traducción
        for i, option in enumerate(question["opciones"]):
            option_letter = chr(65 + i)  # A, B, C, D
            
            # Crear columnas para botón y comando
            col1, col2 = st.columns([0.2, 0.8])
            
            with col1:
                button_key = f"quiz_btn_{key_suffix}_{current_question}_{i}"
                if st.button(
                    f"Opción {option_letter}", 
                    key=button_key,
                    use_container_width=True
                ):
                    st.session_state[answer_key][current_question] = option
                    st.rerun()
            
            with col2:
                # Usar st.code para mejor protección anti-traducción
                st.code(option, language="bash")
        
        # Mostrar resultado si hay respuesta
        if current_question in st.session_state[answer_key]:
            selected = st.session_state[answer_key][current_question]
            st.divider()
            
            st.write("**Tu respuesta seleccionada:**")
            st.code(selected, language="bash")
            
            if selected == question["respuesta_correcta"]:
                st.success("✅ ¡Correcto!")
            else:
                st.error("❌ Incorrecto")
                st.write("**La respuesta correcta es:**")
                st.code(question["respuesta_correcta"], language="bash")
            
            if "explicacion" in question:
                st.info(question["explicacion"])
        
        # Navegación
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("◀ Anterior", key=f"quiz_prev_{key_suffix}", disabled=current_question == 0):
                st.session_state[question_key] = current_question - 1
                st.rerun()
        
        with col2:
            answered = len(st.session_state[answer_key])
            progress = answered / len(self.questions)
            st.progress(progress)
            st.caption(f"{answered}/{len(self.questions)} respondidas")
        
        with col3:
            if st.button("Siguiente ▶", key=f"quiz_next_{key_suffix}", disabled=current_question >= len(self.questions) - 1):
                st.session_state[question_key] = current_question + 1
                st.rerun()
        
        # Verificar si quiz está completo y calcular puntuación
        quiz_complete = len(st.session_state[answer_key]) == len(self.questions)
        if quiz_complete and not st.session_state[completed_key]:
            # Calcular puntuación final
            score = self.calculate_score(st.session_state[answer_key], key_suffix)
            
            # Guardar en el progress tracker
            if hasattr(st.session_state, 'progress_tracker'):
                # Determinar el módulo basado en el key_suffix
                module_id = self._get_module_from_suffix(key_suffix)
                
                st.session_state.progress_tracker.add_quiz_score(
                    module_id, 
                    score, 
                    100  # máximo score
                )
                
                # Marcar el módulo como completado si el score es >= 70%
                if score >= 70:
                    st.session_state.progress_tracker.update_module_progress(
                        module_id, 
                        "quiz_completed"
                    )
                
                # Mostrar mensaje de éxito con información de guardado
                with st.expander("📊 Información de Progreso", expanded=False):
                    st.success(f"✅ Quiz guardado: {module_id} ({score}%)")
                    progress = st.session_state.progress_tracker.get_overall_progress()
                    st.info(f"📈 Progreso actualizado: {progress:.1f}%")
                    
                    completed_modules, total_modules = st.session_state.progress_tracker.get_completed_modules_count()
                    st.info(f"📚 Módulos completados: {completed_modules}/{total_modules}")
                    
                    quizzes_completed = st.session_state.progress_tracker.get_completed_quizzes_count()
                    st.info(f"🎯 Evaluaciones completadas: {quizzes_completed}")
            
            # Marcar como completado para evitar guardado múltiple
            st.session_state[completed_key] = True
            
            # Mostrar resultado final
            st.balloons()
            if score >= 70:
                st.success(f"🎉 ¡Felicitaciones! Has completado el quiz con {score}% de acierto.")
            else:
                st.warning(f"Has obtenido {score}% de acierto. Te recomendamos revisar el material y volver a intentar.")
        
        return quiz_complete
    
    def _get_module_from_suffix(self, key_suffix: str) -> str:
        """Determina el módulo basado en el key_suffix"""
        if "cmd_basics" in key_suffix:
            return "02_cmd_basics"
        elif "ps_basics" in key_suffix:
            return "03_powershell_basics"
        elif "cmd_intermediate" in key_suffix:
            return "04_intermediate_cmd"
        elif "ps_intermediate" in key_suffix:
            return "05_intermediate_ps"
        elif "cmd_advanced" in key_suffix:
            return "06_advanced_cmd"
        elif "ps_advanced" in key_suffix:
            return "07_advanced_ps"
        elif "general_eval" in key_suffix:
            return "08_evaluations"
        elif "evaluation_cmd_advanced" in key_suffix:
            return "08_evaluations_cmd"
        elif "evaluation_ps_advanced" in key_suffix:
            return "08_evaluations_ps"
        # Mantener compatibilidad con nombres anteriores
        elif "basico" in key_suffix:
            return "basico"
        elif "intermedio" in key_suffix:
            return "intermedio" 
        elif "avanzado" in key_suffix:
            return "avanzado"
        elif "archivos" in key_suffix:
            return "archivos"
        elif "redes" in key_suffix:
            return "redes"
        elif "seguridad" in key_suffix:
            return "seguridad"
        elif "automatizacion" in key_suffix:
            return "automatizacion"
        elif "administracion" in key_suffix:
            return "administracion"
        elif "personalizacion" in key_suffix:
            return "personalizacion"
        else:
            # Si no se puede determinar, usar el key_suffix como está
            return key_suffix

class CommandPracticeComponent:
    """Componente para práctica de comandos con simuladores consistentes"""
    
    def __init__(self, exercises: List[Dict]):
        self.exercises = exercises
        if 'current_exercise' not in st.session_state:
            st.session_state.current_exercise = 0
    
    def render(self, key_suffix: str = ""):
        """Renderiza el componente de práctica"""
        if not self.exercises:
            st.error("No hay ejercicios disponibles")
            return
        
        current_idx = st.session_state.current_exercise
        if current_idx >= len(self.exercises):
            st.session_state.current_exercise = 0
            current_idx = 0
        
        exercise = self.exercises[current_idx]
        
        st.subheader(f"Ejercicio {current_idx + 1} de {len(self.exercises)}")
        st.write(exercise["descripcion"])
        
        if "ejemplo" in exercise:
            st.markdown("**Ejemplo:**")
            st.code(exercise["ejemplo"], language="bash")
        
        # Simulador de consola con tipo específico
        console_type = exercise.get("tipo_consola", "cmd")
        simulator = ConsoleSimulator(console_type)
        simulator.render(key_suffix=f"{key_suffix}_{current_idx}")
        
        # Controles de navegación
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        with col1:
            if st.button("◀ Anterior", key=f"practice_prev_{key_suffix}", disabled=current_idx == 0):
                st.session_state.current_exercise -= 1
                st.rerun()
        
        with col2:
            if st.button("💡 Pista", key=f"practice_hint_{key_suffix}"):
                if "pista" in exercise:
                    st.info(f"**Pista:** {exercise['pista']}")
                else:
                    st.info("No hay pistas disponibles para este ejercicio")
        
        with col3:
            if "solucion" in exercise and st.button("✅ Solución", key=f"practice_solution_{key_suffix}"):
                st.success(f"**Solución:** {exercise['solucion']}")
        
        with col4:
            if st.button("Siguiente ▶", key=f"practice_next_{key_suffix}", disabled=current_idx >= len(self.exercises) - 1):
                st.session_state.current_exercise += 1
                st.rerun()
        
        # Registrar progreso
        if hasattr(st.session_state, 'progress_tracker'):
            st.session_state.progress_tracker.add_command_practice(
                exercise.get("comando", "unknown"),
                {
                    "exercise_id": current_idx,
                    "console_type": console_type,
                    "timestamp": st.session_state.get("current_time", "")
                },
                success=True
            )

class NavigationComponent:
    """Componente de navegación mejorado"""
    
    def __init__(self, pages: List[Dict]):
        self.pages = pages
    
    def render_sidebar(self):
        """Renderiza la barra lateral de navegación"""
        st.sidebar.title("🖥️ Aprende CMD y PowerShell")
        
        # Progreso general
        if hasattr(st.session_state, 'progress_tracker'):
            progress = st.session_state.progress_tracker.get_overall_progress()
            st.sidebar.progress(progress / 100)
            st.sidebar.caption(f"Progreso general: {progress:.1f}%")
        
        st.sidebar.markdown("---")
        
        # Lista de páginas
        for i, page in enumerate(self.pages):
            icon = page.get('icon', '📄')
            title = page.get('title', f'Página {i+1}')
            
            # Marcar página actual
            if st.session_state.get('current_page', 1) == i + 1:
                st.sidebar.markdown(f"**{icon} {title}** ⭐")
            else:
                if st.sidebar.button(f"{icon} {title}", key=f"nav_page_{i+1}"):
                    st.session_state.current_page = i + 1
                    st.rerun()
        
        st.sidebar.markdown("---")
        
        # Opciones adicionales
        if st.sidebar.button("🔄 Reiniciar Progreso"):
            if hasattr(st.session_state, 'progress_tracker'):
                st.session_state.progress_tracker.reset_progress()
            st.success("Progreso reiniciado")
            st.rerun()
    
    def render_header(self):
        """Renderiza el encabezado de la página"""
        current_page_num = st.session_state.get('current_page', 1)
        if 1 <= current_page_num <= len(self.pages):
            page = self.pages[current_page_num - 1]
            st.title(f"{page.get('icon', '📄')} {page.get('title', f'Página {current_page_num}')}")
            
            if 'description' in page:
                st.markdown(page['description'])

# Funciones auxiliares para crear componentes específicos
def create_info_box(title: str, content: str, box_type: str = "info"):
    """Crea una caja de información estilizada"""
    if box_type == "info":
        st.info(f"**{title}**\n\n{content}")
    elif box_type == "warning":
        st.warning(f"**{title}**\n\n{content}")
    elif box_type == "success":
        st.success(f"**{title}**\n\n{content}")
    elif box_type == "error":
        st.error(f"**{title}**\n\n{content}")

def create_code_example(title: str, code: str, language: str = "bash", explanation: str = ""):
    """Crea un ejemplo de código con explicación"""
    st.subheader(title)
    st.code(code, language=language)
    if explanation:
        st.markdown(f"**Explicación:** {explanation}")

def create_comparison_table(cmd_data: List[str], ps_data: List[str], headers: List[str]):
    """Crea una tabla de comparación entre CMD y PowerShell"""
    
    df = pd.DataFrame({
        headers[0]: cmd_data,
        headers[1]: ps_data
    })
    
    st.dataframe(df, use_container_width=True)

def create_learning_objective_card(objectives: List[str]):
    """Crea una tarjeta con objetivos de aprendizaje"""
    with st.container():
        st.markdown("### 🎯 Objetivos de Aprendizaje")
        for i, objective in enumerate(objectives, 1):
            st.markdown(f"{i}. {objective}")

def create_tip_card(title: str, content: str, tip_type: str = "info"):
    """Crea una tarjeta de consejos"""
    if tip_type == "info":
        st.info(f"**{title}**\n\n{content}")
    elif tip_type == "success":
        st.success(f"**{title}**\n\n{content}")
    elif tip_type == "warning":
        st.warning(f"**{title}**\n\n{content}")
    elif tip_type == "error":
        st.error(f"**{title}**\n\n{content}")

def create_dual_console_demo(cmd_example: str, ps_example: str, description: str = ""):
    """Crea una demostración lado a lado de CMD y PowerShell"""
    if description:
        st.markdown(description)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🖤 CMD**")
        cmd_simulator = ConsoleSimulator("cmd")
        cmd_simulator.render(key_suffix="demo_cmd")
        
    with col2:
        st.markdown("**🔷 PowerShell**")
        ps_simulator = ConsoleSimulator("powershell")
        ps_simulator.render(key_suffix="demo_ps")

class ProgressCard:
    """Componente para mostrar tarjetas de progreso"""
    
    def __init__(self, progress_tracker):
        self.progress_tracker = progress_tracker
    
    def render(self):
        """Renderiza la tarjeta de progreso"""
        if self.progress_tracker:
            progress = self.progress_tracker.get_overall_progress()
            
            st.markdown("### 📊 Tu Progreso")
            
            # Barra de progreso principal
            st.progress(progress / 100)
            st.caption(f"Progreso general: {progress:.1f}%")
            
            # Estadísticas adicionales
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Usar el nuevo método para obtener módulos completados
                completed_modules, total_modules = self.progress_tracker.get_completed_modules_count()
                st.metric("Módulos completados", f"{completed_modules}/{total_modules}")
            
            with col2:
                commands_practiced = self.progress_tracker.get_commands_practiced_count()
                st.metric("Comandos practicados", commands_practiced)
            
            with col3:
                quizzes_completed = self.progress_tracker.get_completed_quizzes_count()
                st.metric("Evaluaciones completadas", quizzes_completed)
        else:
            st.info("Progreso no disponible")

def render_protected_command(command_text: str, language: str = "bash") -> str:
    """
    Renderiza un comando con protección anti-traducción máxima
    
    Args:
        command_text: El texto del comando a proteger
        language: El lenguaje para el highlighting (bash, powershell, etc.)
    
    Returns:
        HTML string con protección anti-traducción
    """
    # Múltiples técnicas de protección combinadas
    protected_html = f"""
    <div class="protected-command" 
         translate="no" 
         data-translate="no" 
         data-google="notranslate"
         lang="en"
         dir="ltr">
        <code translate="no" 
              data-translate="no" 
              data-google="notranslate"
              class="language-{language}">
            {command_text}
        </code>
    </div>
    """
    return protected_html

def render_command_option(option_text: str, option_letter: str) -> None:
    """
    Renderiza una opción de comando con protección anti-traducción
    
    Args:
        option_text: El texto de la opción (comando)
        option_letter: La letra de la opción (A, B, C, D)
    """
    # Crear HTML protegido
    protected_html = f"""
    <div style="margin: 8px 0; padding: 12px; background-color: #f8f9fa; 
                border: 1px solid #dee2e6; border-radius: 6px;">
        <div style="font-weight: bold; margin-bottom: 4px; color: #495057;">
            Opción {option_letter}:
        </div>
        <div class="protected-command" 
             translate="no" 
             data-translate="no" 
             data-google="notranslate"
             lang="en">
            <code translate="no" 
                  data-translate="no" 
                  data-google="notranslate"
                  style="font-family: 'Consolas', 'Courier New', monospace; 
                         font-size: 14px; color: #212529; background: transparent;">
                {option_text}
            </code>
        </div>
    </div>
    """
    st.markdown(protected_html, unsafe_allow_html=True)

def create_command_reference_table(title: str, commands_data: dict):
    """
    Crea una tabla de referencia de comandos con protección anti-traducción robusta
    
    Args:
        title: Título de la tabla
        commands_data: Diccionario con los datos de los comandos
    """
    st.markdown(f"### {title}")
    
    # CSS específico para proteger comandos en tablas
    st.markdown("""
    <style>
    .command-ref-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    
    .command-row {
        display: flex;
        align-items: center;
        padding: 8px 0;
        border-bottom: 1px solid #dee2e6;
    }
    
    .command-col {
        flex: 1;
        padding: 0 8px;
    }
    
    .command-code {
        translate: no !important;
        -webkit-translate: no !important;
        font-family: 'Consolas', 'Courier New', monospace !important;
        background-color: #e9ecef !important;
        padding: 4px 8px !important;
        border-radius: 4px !important;
        font-size: 13px !important;
        color: #495057 !important;
        display: inline-block !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Detectar las columnas disponibles dinámicamente
    available_keys = list(commands_data.keys())
    
    # Identificar la columna principal (comando/parámetro/verbo)
    main_key = None
    for key in ["Comando", "Parámetro", "Verbo", "Cmdlet", "Símbolo"]:
        if key in available_keys:
            main_key = key
            break
    
    if not main_key:
        # Si no encuentra ninguna clave conocida, usar la primera disponible
        main_key = available_keys[0]
    
    # Identificar la columna de descripción
    desc_key = None
    for key in ["Función", "Descripción", "Propósito", "Significado"]:
        if key in available_keys:
            desc_key = key
            break
    
    # Identificar columna adicional (ejemplo/alias)
    extra_key = None
    for key in ["Ejemplo", "Alias Comunes"]:
        if key in available_keys:
            extra_key = key
            break
    
    # Crear contenedor con protección
    html_content = '<div class="command-ref-container" translate="no" data-translate="no">'
    
    # Header
    html_content += f'''
    <div class="command-row" style="font-weight: bold; background-color: #e9ecef; border-bottom: 2px solid #dee2e6;">
        <div class="command-col">{main_key}</div>
    '''
    
    if desc_key:
        html_content += f'<div class="command-col">{desc_key}</div>'
    
    if extra_key:
        html_content += f'<div class="command-col">{extra_key}</div>'
    
    html_content += '</div>'
    
    # Filas de datos
    num_entries = len(commands_data[main_key])
    
    for i in range(num_entries):
        html_content += '<div class="command-row">'
        
        # Columna principal con protección
        main_value = commands_data[main_key][i]
        html_content += f'''
        <div class="command-col">
            <code class="command-code" translate="no" data-translate="no">{main_value}</code>
        </div>
        '''
        
        # Descripción
        if desc_key:
            desc_value = commands_data[desc_key][i]
            html_content += f'<div class="command-col">{desc_value}</div>'
        
        # Ejemplo o Alias si existe
        if extra_key:
            extra_value = commands_data[extra_key][i]
            html_content += f'''
            <div class="command-col">
                <code class="command-code" translate="no" data-translate="no">{extra_value}</code>
            </div>
            '''
        
        html_content += '</div>'
    
    html_content += '</div>'
    
    # Renderizar el HTML
    st.markdown(html_content, unsafe_allow_html=True)
