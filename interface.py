import streamlit as st

def launch_streamlit_interface(chain):
    st.title("Intelligent Knowledge Retriever Chatbot")
    st.markdown("Ask me something!")

    # Initialize session state for chat history
    if "history" not in st.session_state:
        st.session_state.history = []
    if "input_processed" not in st.session_state:
        st.session_state.input_processed = False  
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
                      
    if st.session_state.input_processed:
        st.session_state.user_input = ""
        st.session_state.input_processed = False       

    # Display chat history
    for user_input, answer in st.session_state.history:
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Bot:** {answer}")

    # Input box for user question
    user_input = st.text_input("Your question:", key="user_input")

    if user_input.strip() and not st.session_state.input_processed:

        result = chain.invoke({"question": user_input})
        answer = result["answer"]
        st.session_state.history.append((user_input, answer))
        st.session_state.input_processed = True
        st.rerun()

    # Clear chat history
    if st.button("Clear Chat History"):
        st.session_state.history = []
        st.session_state.user_input = ""
        st.session_state.input_processed = False
        st.rerun()