# Text-to-Speech (TTS) Application

A simple yet powerful text-to-speech application built with Python, featuring both Edge TTS and gTTS engines. This application provides a user-friendly Gradio interface for converting text to speech with multiple language and voice options.

## Features

- Dual TTS Engine Support:
  - Microsoft Edge TTS: High-quality neural voices
  - Google Text-to-Speech (gTTS): Wide language support
- Multiple Voice Options:
  - English (US/UK) with male and female voices
  - Support for Hindi and French
  - Additional language options through gTTS
- User-Friendly Interface:
  - Clean and intuitive Gradio web interface
  - Real-time voice option updates based on selected engine
  - Easy-to-use controls for text input and voice selection

## Prerequisites

Before running the application, ensure you have the following installed:

1. Python 3.7+
2. FFmpeg (required for audio processing)
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: Install via Homebrew: `brew install ffmpeg`
   - **Linux**: Install via package manager:
     ```bash
     # Ubuntu/Debian
     sudo apt-get update && sudo apt-get install ffmpeg
     # Fedora
     sudo dnf install ffmpeg
     ```

3. Python packages:
```bash
pip install gradio
pip install edge-tts
pip install gTTS
pip install asyncio
```

## Installation

1. Clone this repository or download the source code:
```bash
git clone <repository-url>
cd TTS-App-with-Custom-Voices
```

2. Verify FFmpeg installation:
```bash
ffmpeg -version
```

## Usage

1. Run the application:
```bash
python tts_app.py
```

2. The application will automatically open in your default web browser at `http://127.0.0.1:7860`

3. Using the interface:
   - Enter your text in the input box
   - Select your preferred TTS engine (Edge TTS or gTTS)
   - Choose a voice/language from the dropdown menu
   - Click "Generate Speech" to create the audio
   - Play the generated audio directly in the browser or download it

## Available Voices

### Edge TTS Voices
- English (US):
  - Female: en-US-JennyNeural
  - Male: en-US-GuyNeural
- English (UK):
  - Female: en-GB-LibbyNeural
  - Male: en-GB-RyanNeural
- Hindi: hi-IN-SwaraNeural
- French: fr-FR-DeniseNeural

### gTTS Languages
- English (US)
- French
- German
- Spanish
- Hindi

## Technical Details

The application is built using the following components:

- `gradio`: Provides the web interface
- `edge-tts`: Microsoft Edge's Text-to-Speech engine
- `gTTS`: Google's Text-to-Speech engine
- `asyncio`: Handles asynchronous operations for Edge TTS
- `tempfile`: Manages temporary audio file creation
- `FFmpeg`: Handles audio processing and conversion

## Error Handling

The application includes error handling for:
- Invalid TTS engine selection
- Text-to-speech conversion failures
- File system operations
- Invalid voice/language selections
- FFmpeg-related issues

## Troubleshooting

Common issues and solutions:

1. **FFmpeg not found error**:
   - Verify FFmpeg is installed: `ffmpeg -version`
   - Check if FFmpeg is in your system PATH
   - Try reinstalling FFmpeg

2. **Audio conversion errors**:
   - Ensure FFmpeg is properly installed
   - Check system permissions for temp file creation
   - Verify internet connection for TTS services

## Limitations

- Internet connection required for both TTS engines
- FFmpeg must be installed and accessible
- Temporary files are created for audio storage
- Voice options vary between engines
- Audio quality depends on the selected engine and internet connection

## Contributing

Feel free to contribute to this project by:
- Reporting issues
- Suggesting new features
- Submitting pull requests
- Adding support for new languages/voices