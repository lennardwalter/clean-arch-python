class UserNotFoundError:
    pass


type UserGetByIdError = UserNotFoundError
type UserGetByEmailError = UserNotFoundError
