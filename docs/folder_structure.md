# Folder Structure

The folder structure of the Book Catalog project reflects a typical organization following the principles of hexagonal architecture. At its core lies the app directory, housing the main project components. Within app, the books module takes center stage, orchestrating the management of books through distinct layers.

Under books, the application directory encapsulates the application logic, featuring the books_service.py module responsible for book management operations. Additionally, the dtos.py file defines Data Transfer Objects (DTOs) used for transferring data between layers.

In the domain directory, essential domain logic resides, including definitions for entities related to books (entity.py), domain exceptions (exceptions.py), and the book repository interface (repository.py).

Complementing the application and domain layers, the infrastructure directory houses infrastructure-related code. This includes adapters for data persistence (adapters), such as the in-memory adapter (in_memory_adapter.py) and the MongoDB adapter (mongo_adapter.py). The api directory within infrastructure contains API-related code, with api_routers.py defining API routers for book management.

Outside the books module, other critical project files include database.py for database configuration, error_handlers.py for application error handling, and main.py serving as the primary entry point for the application.

Finally, the run.py script provides a convenient way to execute the application. This structured organization ensures a clear separation of concerns and facilitates the maintenance and scalability of the project.