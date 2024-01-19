from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str


class PostCreate(PostBase):
    user_id: int
    pass


class Post(PostBase):
    id: int
    user_id: int


    class Config:
        orm_mode = True


# Celui qui rentre sur la methode POST
class PostPrecursor(BaseModel):
    title: str
    text: str


# Prepare par le service (sauf id) pour la date
class PostEntity(PostPrecursor):
    id: int
    user_id: int
    date: int

# Celui qui sort du controller (retour à l'UI)
class PostDTO(PostPrecursor):
    date: int

# Service precusor -> entity ou entity -> DTO

