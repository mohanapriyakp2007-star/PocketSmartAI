import sys
import uvicorn
from pathlib import Path

# Project root path-ஐ Python-க்கு அடையாளம் காட்டுகிறது
sys.path.append(str(Path(__file__).resolve().parent))

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

