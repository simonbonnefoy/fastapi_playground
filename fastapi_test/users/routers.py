from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/users")
def get_all_users():
    # users = database.get_all_users()
    # users_list = [u.as_dict() for u in users]
    # return users_list
    return fake_items_db



@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    """
    Retrieve a user based on their id
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """
    # user = database.get_user_by_id(user_id)
    # return user.as_dict()
    print(user_id)
    return fake_items_db



@router.post("/user/")
async def add(username: str, password: str, email: str):
    """
    Retrieve a user based on their id
    :param email:
    :param password:
    :param username:
    :return: a dict containing the user info
    """
    user = User(username, password, email)
    database.add_user(user)
    return user.as_dict()

@router.put("/{user_id}")
async def add(user_id: int, username: Optional[str] = None,
              password: Optional[str] = None,
              email: Optional[str] = None):
    """
    Retrieve a user based on their id
    :param username:
    :param email:
    :param password:
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """

    user = database.get_user_by_id(user_id)
    user.username = username if username else user.username
    user.password = password if password else user.password
    user.email = email if email else user.email
    database.add_user(user)
    return user.as_dict()

@router.delete("/user/{user_id}")
async def add(user_id: int):
    """
    Retrieve a user based on their id
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """
    database.delete_user_by_id(user_id)
    return {'deleted': f'user_id {user_id}'}
