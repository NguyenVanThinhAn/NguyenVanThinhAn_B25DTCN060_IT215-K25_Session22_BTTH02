from fastapi import FastAPI
from app.routers.__init__ import router_list
from app.database import Base, engine

app = FastAPI()

for v in router_list:
    app.include_router(v)

Base.metadata.create_all(bind=engine)
