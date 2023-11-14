from typing import List

import strawberry


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, id: strawberry.ID) -> User:
        return User(id=id, name="John", email="john@abc.com")

    @strawberry.field
    def users(self, info) -> List[User]:
        return [
            User(id=strawberry.ID("1"), name="John", email="john@abc.com")
        ]
