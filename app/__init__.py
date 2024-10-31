from fastapi import FastAPI
from .db import migrate



app = FastAPI(debug=True)


from .routes import auth_app, default_app, create_mock_data




# app.mount("/auth", auth_app)
app.mount("/default", default_app)


app.include_router(auth_app)
migrate()
create_mock_data()