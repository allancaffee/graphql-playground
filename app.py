from ariadne import ObjectType, QueryType, gql, snake_case_fallback_resolvers, make_executable_schema
from ariadne.asgi import GraphQL

from models.person import Person

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql("""
    type Query {
        people: [Person!]!
    }

    type Person {
        firstName: String
        lastName: String
        age: Int
        fullName: String
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("people")
def resolve_people(*_):
    return [
        Person(first_name="John", last_name="Doe", age=21),
        Person(first_name="Bob", last_name="Boberson", age=24),
    ]


# Map resolver functions to custom type fields using ObjectType
person = ObjectType("Person")

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, person, snake_case_fallback_resolvers)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)
