# import os
# import sys
import uvicorn
from fastapi import FastAPI

from template.settings import settings
from template.signals import setup_signals
from template.api import router

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()
app.include_router(router)
setup_signals(app)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
