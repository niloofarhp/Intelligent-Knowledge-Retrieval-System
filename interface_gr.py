import gradio as gr

def launch_gradio_interface(chain):
    def ask_question(user_input, history=[]):
        result = chain.invoke({"question": user_input})
        answer = result["answer"]
        print("\nAnswer:", answer)
        history.append((user_input, answer))
        return history, history, ""

    with gr.Blocks() as demo:
        gr.Markdown("## Intelligent Knowledge Retriever Chatbot")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Ask me something...")
        clear = gr.Button("Clear")

        state = gr.State([])

        msg.submit(ask_question, [msg, state], [chatbot, state, msg])
        clear.click(lambda: ([], [], ""), None, [chatbot, state, msg])
    
    demo.launch()
