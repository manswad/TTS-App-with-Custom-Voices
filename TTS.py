import gradio as gr
from gtts import gTTS
from edge_tts import Communicate
import asyncio
import tempfile
import webbrowser

# Available voices for Edge TTS and gTTS
edge_voices = {
    "English (US - Female)": "en-US-JennyNeural",
    "English (US - Male)": "en-US-GuyNeural",
    "English (UK - Female)": "en-GB-LibbyNeural",
    "English (UK - Male)": "en-GB-RyanNeural",
    "Hindi (Female)": "hi-IN-SwaraNeural",
    "French (Female)": "fr-FR-DeniseNeural",
}

gtts_languages = {
    "English (US)": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
}

# Function for Edge TTS
async def edge_tts_generate(text, voice):
    communicate = Communicate(text, voice)
    output_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    await communicate.save(output_file)
    return output_file

# Function for gTTS
def gtts_generate(text, lang):
    tts = gTTS(text=text, lang=lang)
    output_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    tts.save(output_file)
    return output_file

# Main function for text-to-speech
def text_to_speech(text, tts_engine, voice_choice):
    try:
        if tts_engine == "Edge TTS":
            # Use Edge TTS
            output_path = asyncio.run(edge_tts_generate(text, edge_voices[voice_choice]))
        elif tts_engine == "gTTS":
            # Use gTTS
            output_path = gtts_generate(text, gtts_languages[voice_choice])
        else:
            return "Error: Invalid TTS Engine!"
        return output_path
    except Exception as e:
        return f"Error: {str(e)}"

# Update voice options dynamically
def update_voices(tts_engine):
    if tts_engine == "Edge TTS":
        return gr.update(choices=list(edge_voices.keys()), value=list(edge_voices.keys())[0])
    elif tts_engine == "gTTS":
        return gr.update(choices=list(gtts_languages.keys()), value=list(gtts_languages.keys())[0])

# Create the Gradio interface
def create_gui():
    tts_engines = ["Edge TTS", "gTTS"]

    interface = gr.Interface(
        fn=text_to_speech,
        inputs=[
            gr.Textbox(label="Enter Text", placeholder="Type text to convert to speech here..."),
            gr.Radio(choices=tts_engines, label="Select TTS Engine", value="Edge TTS", elem_id="tts-engine"),
            gr.Dropdown(choices=list(edge_voices.keys()), label="Select Voice", elem_id="voice-dropdown"),
        ],
        outputs=gr.Audio(label="Generated Speech", type="filepath"),
    )

    # Dynamic update for voice selection
    interface = gr.Blocks()
    with interface:
        with gr.Row():
            text_input = gr.Textbox(label="Enter Text", placeholder="Type text to convert to speech here...")
        with gr.Row():
            tts_engine = gr.Radio(choices=tts_engines, label="Select TTS Engine", value="Edge TTS")
            voice_dropdown = gr.Dropdown(choices=list(edge_voices.keys()), label="Select Voice")
        with gr.Row():
            submit_button = gr.Button("Generate Speech")
        output_audio = gr.Audio(label="Generated Speech", type="filepath")

        # Link interactions
        tts_engine.change(update_voices, inputs=tts_engine, outputs=voice_dropdown)
        submit_button.click(
            text_to_speech,
            inputs=[text_input, tts_engine, voice_dropdown],
            outputs=output_audio,
        )

    return interface

# Run the application
if __name__ == "__main__":
    gui = create_gui()
    webbrowser.open_new_tab("http://127.0.0.1:7860")
    gui.launch()