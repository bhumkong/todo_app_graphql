from src.data import get_data, save_data
from src.models import Todo
from src.types import TodoType, TodoCreate, TodoUpdate


def get_todo_list(user_id: int | None = None) -> list[TodoType]:
    all_todos = get_data().todos
    if user_id is not None:
        all_todos = [todo for todo in all_todos if todo.user_id == user_id]
    return all_todos


def mark_done(todo_id: int, done: bool) -> TodoType:
    data = get_data()
    try:
        todo = next(todo for todo in data.todos if todo.id == todo_id)
    except StopIteration:
        raise ValueError(f"Todo with id {todo_id} not found")
    todo.done = done
    save_data()
    return todo


def create_todo(todo: TodoCreate) -> TodoType:
    data = get_data()
    next_id = max(todo.id for todo in data.todos) + 1
    new_todo = Todo(**todo.__dict__, id=next_id, done=False)
    data.todos.append(new_todo)
    save_data()
    return new_todo


def update_todo(todo_id: int, todo_fields: TodoUpdate) -> TodoType:
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
