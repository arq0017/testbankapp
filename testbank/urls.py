from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# importBranchDetail view for populating BankBranchModel (bank_id field is foreign key)
from api.views import importBranchDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    # use this url only to add .csv data to BankBranch Model
    path('addData', importBranchDetail, name='add-data'),
    # for querying graphQL queries 
    path('gql', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
