import strawberry
from strawberry.tools import merge_types

from . import user


auth_queries = (
    user.Query,
)


auth_schema = strawberry.Schema(
    query=merge_types("AuthQuery",  auth_queries),
    # mutation=AuthMutation,
    # subscription=AuthSubscription,
)
