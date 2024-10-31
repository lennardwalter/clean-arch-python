from typing import Never


class TodoNotFoundError:
    pass


type TodoCreateError = Never
type TodoUpdateError = TodoNotFoundError
type TodoDeleteError = TodoNotFoundError
type TodoGetByIdError = TodoNotFoundError
type TodoGetCountByUserIdError = Never
type TodoGetAllByUserIdError = Never
