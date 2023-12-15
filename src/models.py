from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str
    done: bool
    user_id: int


class User(BaseModel):
    id: int
    name: str


class Data(BaseModel):
    todos: list[Todo]
    users: list[User]


class UserWithTodos(User):
    todos: list[Todo] | None = None
