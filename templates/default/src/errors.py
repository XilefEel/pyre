from enum import StrEnum, auto

from result import Err, Ok, Result


# Error Variants
# (Rust: enum AppError { NotFound, InvalidInput, Unexpected })
class AppError(StrEnum):
    NOT_FOUND = auto()
    INVALID_INPUT = auto()
    UNEXPECTED = auto()


# Example usage
# (Rust: fn find_user(id: u32) -> Result<User, AppError>)
def find_user(user_id: int) -> Result[str, AppError]:
    if user_id <= 0:
        return Err(AppError.INVALID_INPUT)
    if user_id > 100:
        return Err(AppError.NOT_FOUND)
    return Ok(f"user_{user_id}")


# Example match
if __name__ == "__main__":
    match find_user(0):
        case Ok(user):
            print(f"Found: {user}")
        case Err(AppError.INVALID_INPUT):
            print("Invalid user id")
        case Err(AppError.NOT_FOUND):
            print("User not found")
        case Err(e):
            print(f"Unexpected error: {e}")
