"""
Página de debug para verificar el progreso del usuario
"""

import streamlit as st
import json
from datetime import datetime

def show_debug_page():
    """Muestra información de debug del progreso"""
    st.title("🔧 Debug - Estado del Progreso")
    
    if not hasattr(st.session_state, 'progress_tracker'):
        st.error("ProgressTracker no está inicializado")
        return
    
    tracker = st.session_state.progress_tracker
    
    # Información básica
    st.subheader("📋 Información Básica")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("User ID", tracker.get_user_id())
        progress = tracker.get_overall_progress()
        st.metric("Progreso General", f"{progress:.1f}%")
    
    with col2:
        completed_modules, total_modules = tracker.get_completed_modules_count()
        st.metric("Módulos Completados", f"{completed_modules}/{total_modules}")
        
        quizzes_completed = tracker.get_completed_quizzes_count()
        st.metric("Evaluaciones Completadas", quizzes_completed)
    
    # Datos de progreso completos
    st.subheader("💾 Datos de Progreso")
    user_id = tracker.get_user_id()
    
    if "user_progress" in tracker.progress_data and user_id in tracker.progress_data["user_progress"]:
        user_data = tracker.progress_data["user_progress"][user_id]
        
        for module_id, module_data in user_data.items():
            with st.expander(f"📚 {module_id}"):
                st.json({
                    "sections_completed": module_data.get("sections_completed", []),
                    "quiz_scores": module_data.get("quiz_scores", []),
                    "time_spent": module_data.get("time_spent", 0),
                    "last_accessed": module_data.get("last_accessed", "Never")
                })
    else:
        st.warning("No hay datos de progreso para este usuario")
    
    # Acciones de debug
    st.subheader("🛠️ Acciones de Debug")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🧪 Agregar Quiz de Prueba"):
            tracker.add_quiz_score("debug_test", 85, 100)
            st.success("Quiz de prueba agregado")
            st.rerun()
    
    with col2:
        if st.button("📊 Recalcular Progreso"):
            progress = tracker.get_overall_progress()
            st.success(f"Progreso recalculado: {progress:.1f}%")
    
    with col3:
        if st.button("🗑️ Limpiar Debug"):
            if "debug_test" in tracker.progress_data["user_progress"].get(user_id, {}):
                del tracker.progress_data["user_progress"][user_id]["debug_test"]
                tracker._save_progress_data()
                st.success("Datos de debug limpiados")
                st.rerun()
    
    # Datos completos del archivo JSON
    with st.expander("🗂️ Datos Completos del JSON"):
        st.json(tracker.progress_data)

if __name__ == "__main__":
    show_debug_page()
