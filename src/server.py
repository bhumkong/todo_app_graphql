from src.api import schema
from src.data import load_data
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.on_event('startup')(load_data)
