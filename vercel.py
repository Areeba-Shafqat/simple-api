from main import app  # Import your FastAPI app
from mangum import Mangum  # ASGI adapter for AWS Lambda/Vercel

handler = Mangum(app)
