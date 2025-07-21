"""
Componentes para cuestionarios interactivos y práctica de comandos
"""

import streamlit as st
import sys
import os
from typing import List, Dict

# Agregar utils al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from ui_helpers import render_protected_command, render_command_option
from progress_tracker import ProgressTracker
from console_components import ConsoleSimulator

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
        if not self.questions:
            st.error("No hay preguntas disponibles")
            return
        st.markdown("""
        <style>
        .stCode {
            translate: no !important;
            -webkit-translate: no !important;
        }
        </style>
        """, unsafe_allow_html=True)
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
        if current_question >= len(self.questions):
            st.session_state[question_key] = 0
            current_question = 0
        elif current_question < 0:
            st.session_state[question_key] = 0
            current_question = 0
        question = self.questions[current_question]
        st.subheader(f"Pregunta {current_question + 1} de {len(self.questions)}")
        st.write(question["pregunta"])
        st.write("**Selecciona la opción correcta:**")
        for i, option in enumerate(question["opciones"]):
            option_letter = chr(65 + i)
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
                # Usar protección anti-traducción para comandos
                if any(char in option for char in ['-', '/', '\\', '>', '<', '|']):
                    # Es un comando, usar protección completa
                    st.markdown(render_protected_command(option, "bash"), unsafe_allow_html=True)
                else:
                    # Texto normal o conceptos técnicos
                    st.code(option, language="bash")
        if current_question in st.session_state[answer_key]:
            selected = st.session_state[answer_key][current_question]
            st.divider()
            st.write("**Tu respuesta seleccionada:**")
            # Usar protección para la respuesta seleccionada también
            if any(char in selected for char in ['-', '/', '\\', '>', '<', '|']):
                st.markdown(render_protected_command(selected, "bash"), unsafe_allow_html=True)
            else:
                st.code(selected, language="bash")
            if selected == question["respuesta_correcta"]:
                st.success("✅ ¡Correcto!")
            else:
                st.error("❌ Incorrecto")
                st.write("**La respuesta correcta es:**")
                st.code(question["respuesta_correcta"], language="bash")
            if "explicacion" in question:
                st.info(question["explicacion"])
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
        quiz_complete = len(st.session_state[answer_key]) == len(self.questions)
        if quiz_complete and not st.session_state[completed_key]:
            score = self.calculate_score(st.session_state[answer_key], key_suffix)
            if hasattr(st.session_state, 'progress_tracker'):
                module_id = self._get_module_from_suffix(key_suffix)
                st.session_state.progress_tracker.add_quiz_score(
                    module_id, 
                    score, 
                    100
                )
                if score >= 70:
                    st.session_state.progress_tracker.update_module_progress(
                        module_id, 
                        "quiz_completed"
                    )
                with st.expander("📊 Información de Progreso", expanded=False):
                    st.success(f"✅ Quiz guardado: {module_id} ({score}%)")
                    progress = st.session_state.progress_tracker.get_overall_progress()
                    st.info(f"📈 Progreso actualizado: {progress:.1f}%")
                    completed_modules, total_modules = st.session_state.progress_tracker.get_completed_modules_count()
                    st.info(f"📚 Módulos completados: {completed_modules}/{total_modules}")
                    quizzes_completed = st.session_state.progress_tracker.get_completed_quizzes_count()
                    st.info(f"🎯 Evaluaciones completadas: {quizzes_completed}")
            st.session_state[completed_key] = True
            st.balloons()
            if score >= 70:
                st.success(f"🎉 ¡Felicitaciones! Has completado el quiz con {score}% de acierto.")
            else:
                st.warning(f"Has obtenido {score}% de acierto. Te recomendamos revisar el material y volver a intentar.")
        return quiz_complete

    def _get_module_from_suffix(self, key_suffix: str) -> str:
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
            return key_suffix

class CommandPracticeComponent:
    """Componente para práctica de comandos con simuladores consistentes"""
    def __init__(self, exercises: List[Dict]):
        self.exercises = exercises
        if 'current_exercise' not in st.session_state:
            st.session_state.current_exercise = 0

    def render(self, key_suffix: str = ""):
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
        console_type = exercise.get("tipo_consola", "cmd")
        simulator = ConsoleSimulator(console_type)
        simulator.render(key_suffix=f"{key_suffix}_{current_idx}")
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