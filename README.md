# Book Catalog Project

![Static Badge](https://img.shields.io/badge/fastapi-v0.110.0-%23009688?logo=FastAPI)
![Static Badge](https://img.shields.io/badge/PyMongo-v4.6-%2347A248?logo=MongoDB)
![Static Badge](https://img.shields.io/badge/pytest-v8.1-%230A9EDC?logo=pytest)
![GitHub License](https://img.shields.io/github/license/MateoVelasquez/book_catalog)
![GitHub watchers](https://img.shields.io/github/watchers/MateoVelasquez/book_catalog)
![GitHub forks](https://img.shields.io/github/forks/MateoVelasquez/book_catalog)

### Table of Contents

- [About the project](#about-the-project)
    - [Built with](#built-with)
- [Getting started](#getting-started)
    - [Installation](#installation)
    - [Folder structure](#folder-structure)
    - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

# About the project

This project is part of a study to learn advanced software development concepts, focusing on hexagonal architecture (ports and adapters) and the FastAPI framework in Python. The project is a book catalog that allows performing CRUD operations (Create, Read, Update, Delete). Operations include retrieving all books, retrieving books by ISBN, adding new books, deleting, and updating.

The book catalog uses MongoDB as the data storage system, but it is designed to support the inclusion of other storage and/or communication systems through the development of new adapters that plug into the main service.

The development environment for this project was set up using Anaconda, although it is compatible with other virtual environment management tools such as pip and virtualenv.

## Built with

The Book Catalog project was built with the following technologies:

- [FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python.
- [MongoDB](https://www.mongodb.com/): NoSQL database used for data storage.
- [Pydantic](https://docs.pydantic.dev/latest/): Data validation and settings management library.
- [Uvicorn](https://www.uvicorn.org/): ASGI server used to run the FastAPI application.
- [Pytest](https://docs.pytest.org/en/8.0.x/): Testing framework used for unit and integration tests.

These technologies were chosen to provide a robust, scalable, and efficient solution.


# Getting Started

## Installation

To install the Book Catalog Project in your machine, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/book-catalog.git
    ```
2. Navigate to the project directory:
    ```bash
    cd book-catalog
    ```
3. You can install the Book Catalog project using either venv with pip or Conda. Choose one of the following methods:

    Using venv with pip:
    ```bash
    pip install -r requirements.txt
    ```

    Using conda:
    ```bash
    conda env create -f environment.yml
    conda activate books_catalog_env
    ```

4. Set up the MongoDB database connection by configuring the environment variables. You can do this by creating a .env file in the root directory of the project and adding the following lines: 

    ```plaintext
    MONGO_URL=mongodb://localhost:27017/
    MONGO_DATABASE_NAME=local
    ```
    Note: If these variables are not defined, the code will use default MongoDB connection settings.


5. Run the FastAPI application:

    With uvicorn:
    ```bash
    uvicorn app.main:app --reload
    ```
    Alternatively:
    ```bash
    python run.py
    ```



## Folder structure
The project directory structure is organized as follows:
```
book_catalog/
┣ app/                      
┃ ┣ books/
┃ ┃ ┣ application/
┃ ┃ ┃ ┣ books_service.py
┃ ┃ ┃ ┗ dtos.py
┃ ┃ ┣ domain/
┃ ┃ ┃ ┣ entity.py
┃ ┃ ┃ ┣ exceptions.py
┃ ┃ ┃ ┗ repository.py
┃ ┃ ┗ infraestructure/
┃ ┃   ┣ adapters/
┃ ┃   ┃ ┣ in_memory_adapter.py
┃ ┃   ┃ ┗ mongo_adapter.py
┃ ┃   ┗ api/
┃ ┃     ┗ api_routers.py
┃ ┣ database.py
┃ ┣ error_handlers.py
┃ ┗ main.py
┗ run.py
```
The application follows a hexagonal architecture structure, divided into the following layers:

- **Domain:** Contains domain logic and business entities.
- **Application:** Defines application services that implement business logic using domain repositories.
- **Infrastructure:** Contains adapters that connect the application with different storage and communication technologies, such as MongoDB or in-memory storage. Additionally, it includes API routers for module interaction.
- **Database:** Handles the database connection and configuration.
- **Error Handlers:** Registers and manages custom error handlers for the application.
- **Main:** Entry point of the application.

For more information, please refer to this document: [folder structure](https://github.com/MateoVelasquez/book_catalog/docs/folder_structure.md).

## Usage
Access the Book Catalog API docs at http://localhost:8000/docs in your web browser or API testing tool.

The Book Catalog project provides a simple CRUD (Create, Read, Update, Delete) interface for managing books. Below are the available endpoints:

- **GET /books:** Retrieves a list of all books in the catalog.
- **GET /books/{isbn}:** Retrieves a specific book by its ISBN.
- **POST /books:** Adds a new book to the catalog.
- **PUT /books/{book_id}:** Updates an existing book.
- **DELETE /books/{book_id}:** Deletes a book from the catalog.

To interact with these endpoints, you can use tools like CURL, Postman, or any HTTP client library in your preferred programming language.

# Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/1. AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

# License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

# Contact

If you have any questions, feedback, or suggestions, feel free to reach out to us:

- **Mateo Velásquez:** mateo10velasquez@hotmail.com
- **Project Link:** https://github.com/MateoVelasquez/book_catalog

We appreciate your interest and value your input!

# Acknowledgments
We would like to express our gratitude to the following resources and individuals whose insights, documentation, and tutorials greatly contributed to the development of this project.

- https://github.com/serfer2/flask-hexagonal-architecture-api/tree/main/src
- The [FastAPI](https://fastapi.tiangolo.com/) documentation and community for providing comprehensive guidance and support in building robust APIs.
- [MongoDB Developer](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/) which provided valuable knowledge on MongoDB database management with fastapi.
- [Hexagonal Architecture in Python](https://douwevandermeij.medium.com/hexagonal-architecture-in-python-7468c2606b63) article wrote by Douwe van der Meij
- [Hexagonal architecture in Python](https://blog.szymonmiks.pl/p/hexagonal-architecture-in-python/) article wrote by Szymon Miks in his personal blog.
- [ES] [Aprende Arquitectura Hexagonal en 10 minutos](https://www.youtube.com/watch?v=eNFAJbWCSww&ab_channel=CodelyTV-Redescubrelaprogramaci%C3%B3n). Video explaining Hex Architecture concepts by "CodelyTV - Redescubre la programación"
- Stack Overflow and various online forums for their wealth of information and solutions to common programming challenges.


We extend our heartfelt appreciation to these resources and individuals for their invaluable contributions to this project. Without their guidance and support, this endeavor would not have been possible. Thank you!