import graphene
import graphql_jwt
from graphql_auth import mutations
# UserQuery to query users with some useful filters.
# MeQuery to retrieve data for the currently authenticated user.
from graphql_auth.schema import UserQuery, MeQuery

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    delete_account = mutations.DeleteAccount.Field()

class Mutation(AuthMutation, graphene.ObjectType):
   pass

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)