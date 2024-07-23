import gradio as gr
from main import search_engine

def process_search(query, files):
    if files is None:
        return "No files uploaded", 0.0
    return search_engine(query, files)

interface = gr.Interface(
    fn=process_search,
    inputs=[gr.Textbox(label="Search Query"), gr.File(file_count="multiple", label="Upload PDF Files")],
    outputs=[gr.Textbox(label="Summary"), gr.Textbox(label="Relevance Score")]
)

if __name__ == "__main__":
    interface.launch()



