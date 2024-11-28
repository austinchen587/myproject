from fastapi import FastAPI, File, UploadFile
import whisper

# Initialize FastAPI app
app = FastAPI()

# Load the Whisper model
model = whisper.load_model("tiny")  # Use "tiny", "base", etc., depending on your choice

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    """
    Endpoint to accept an audio file and return its transcription.
    """
    # Save the uploaded file temporarily
    audio_path = f"/tmp/{file.filename}"
    with open(audio_path, "wb") as audio_file:
        audio_file.write(await file.read())
    
    # Transcribe the audio
    result = model.transcribe(audio_path)
    
    # Return the transcription
    return {"text": result["text"]}