from data.users import sample_user
from models.user_model import User

db: list[User] = [User(**sample_user)]
