from src import resolvers
from src.types import TodoType, UserWithTodosType
from strawberry import type, field, mutation, Schema


@type
class Query:
    users: list[UserWithTodosType] = field(resolver=resolvers.get_users_with_todos)
    todo_list: list[TodoType] = field(resolver=resolvers.get_todo_list)


@type
class Mutation:
    mark_done: TodoType = mutation(resolver=resolvers.mark_done)
    create_todo: TodoType = mutation(resolver=resolvers.create_todo)
    update_todo: TodoType = mutation(resolver=resolvers.update_todo)


schema = Schema(Query, Mutation)
