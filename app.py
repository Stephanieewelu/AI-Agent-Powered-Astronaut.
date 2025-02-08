import streamlit as st
from ai_agent import MedicalAgent, TechSupportAgent, NavigationAgent

# Title
st.title("🚀 AI Agent Assistant")
st.write("Ask an AI Agent about space-related issues.")

# Agent Selection
agents = {
    "Medical": MedicalAgent(),
    "Tech Support": TechSupportAgent(),
    "Navigation": NavigationAgent()
}
selected_agent_name = st.selectbox("Select an AI Agent:", list(agents.keys()))

# User Input
user_query = st.text_area("Enter your query:", placeholder="Type your question here...")

# Submit Button
if st.button("Ask AI"):
    if not user_query.strip():
        st.warning("Please enter a question!")
    else:
        # Get AI Response
        agent = agents[selected_agent_name]
        response = agent.respond(user_query)
        st.success(f"🤖 {selected_agent_name} AI Response:\n{response}")
