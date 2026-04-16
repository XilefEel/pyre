from result import Err, Ok

from errors import AppError, find_user
from models import Config


def main() -> None:
    print("Hello from {project_name}!\n")

    match find_user(42):
        case Ok(user):
            print(f"Found: {user}")
        case Err(AppError.INVALID_INPUT):
            print("Invalid user id")
        case Err(AppError.NOT_FOUND):
            print("User not found")
        case Err(e):
            print(f"Error: {e}")

    config = Config(host="localhost", port=8080)
    print(f"Running on {config.host}:{config.port}")


if __name__ == "__main__":
    main()
