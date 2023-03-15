from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# we can declare schema here or in the settings.py
# from posts.schema import schema

urlpatterns = [
    # we only need this URL to access graphql
    # This view will serve as GraphQL endpoint with 'graphiql=True'.
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]