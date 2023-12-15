import strawberry

from src.models import User, Todo


@strawberry.experimental.pydantic.type(model=User, all_fields=True)
class UserType:
    pass


@strawberry.experimental.pydantic.type(model=Todo, all_fields=True)
class TodoType:
    pass


@strawberry.experimental.pydantic.input(model=Todo)
class TodoCreate:
    title: strawberry.auto
    description: strawberry.auto
    user_id: strawberry.auto


@strawberry.input
class TodoUpdate:
    title: str | None = None
    description: str | None = None
    user_id: int | None = None


@strawberry.experimental.pydantic.type(model=User, all_fields=True)
class UserWithTodosType:
    todos: list[TodoType] | None = None
