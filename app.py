

from generate_service_model import model_generate_text, processed_model_outputs, calculate_coherence


from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, HTTPException, Query, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn
import time



app = FastAPI(
    title="Eason's Chat_AI",
    description="歡迎來測試！",
    version="0.0.1.1"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/generate-text/")
def generateText(input_text: str = "你好[喜歡]", nsamples: int = 1):
    input_text = text_preprocessing(input_text)
    result = model_generate_text(input_text, nsamples)
    result = processed_model_outputs(result, input_text)
    result = calculate_coherence(result)
    return result
    
def text_preprocessing(text):
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    text = text.lower()
    if "[噁心]" in text:
        text.replace("[噁心]", "[厭惡]")
    return text



if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)