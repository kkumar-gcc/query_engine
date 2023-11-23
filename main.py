import os
import uvicorn

from fastapi import FastAPI
from routes import router

api = FastAPI()

# Mount the API router
api.include_router(router)

# Run the FastAPI server
if __name__ == "__main__":
    # Get the port from the environment variable or use the default value
    port = int(os.getenv("APP_PORT", 8000))

    # Start the FastAPI server
    uvicorn.run("main:api", host="0.0.0.0", port=port, reload=True)