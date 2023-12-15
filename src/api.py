from src import resolvers
from src.types import TodoType
from strawberry import type, field, Schema


@type
class Query:
    todo_list: list[TodoType] = field(resolver=resolvers.get_todo_list)


@type
class Mutation:
    mark_done: TodoType = field(resolver=resolvers.mark_done)
    create_todo: TodoType = field(resolver=resolvers.create_todo)
    update_todo: TodoType = field(resolver=resolvers.update_todo)


schema = Schema(Query, Mutation)
