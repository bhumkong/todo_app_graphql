
from src.data import get_data, save_data
from src.models import Todo
from src.types import TodoType, TodoCreate, TodoUpdate
from strawberry import type, field, Schema, mutation


@type
class Query:
    @field
    def hello(self, name: str) -> str:
        return f"Hello {name}!"

    @field
    def todo_list(self, user_id: int | None = None) -> list[TodoType]:
        all_todos = get_data().todos
        if user_id is not None:
            all_todos = [todo for todo in all_todos if todo.user_id == user_id]
        return all_todos


@type
class Mutation:
    @mutation
    def mark_done(self, todo_id: int, done: bool) -> TodoType:
        data = get_data()
        try:
            todo = next(todo for todo in data.todos if todo.id == todo_id)
        except StopIteration:
            raise ValueError(f"Todo with id {todo_id} not found")
        todo.done = done
        save_data()
        return todo

    @mutation
    def create_todo(self, todo: TodoCreate) -> TodoType:
        data = get_data()
        next_id = max(todo.id for todo in data.todos) + 1
        new_todo = Todo(**todo.__dict__, id=next_id, done=False)
        data.todos.append(new_todo)
        save_data()
        return new_todo

    @mutation
    def update_todo(self, todo_id: int, todo_fields: TodoUpdate) -> TodoType:
        data = get_data()
        try:
            todo = next(todo for todo in data.todos if todo.id == todo_id)
        except StopIteration:
            raise ValueError(f"Todo with id {todo_id} not found")
        for key, value in todo_fields.__dict__.items():
            if value is not None:
                setattr(todo, key, value)
        save_data()
        return todo


schema = Schema(Query, Mutation)
