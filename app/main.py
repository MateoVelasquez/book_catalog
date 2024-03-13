from fastapi import FastAPI


from app.books.infraestructure.api.api_routers import books_router


app = FastAPI(
    title="Books Catalog",
    description="REST API with FastAPI and MongoDB using Ports and Adapters architecture (Hexagonal)",
    version="0.0.1"
)

app.include_router(books_router)