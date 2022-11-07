from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from api.models import Bank, BankBranch

'''
     class -> BankType and BankBranchType model:
     details -> We are creating GraphQL types for our model. GraphQL types fields correspond to Django model field.
'''


class BankNode(DjangoObjectType):

    class Meta:
        model = Bank
        fields = ['name', 'branches']
        interfaces = (relay.Node, )
        filter_fields = []


class BankBranchNode(DjangoObjectType):

    class Meta:
        model = BankBranch
        fields = ['ifsc', 'branch', 'bank_id', 'bank_id__name']
        interfaces = (relay.Node, )
        filter_fields = []


'''
     class -> Query
     details -> Rooty type for accessing queries
'''


class Query(ObjectType, ifsc=None):
     # for fetching all the branches
    all_branches = DjangoFilterConnectionField(BankBranchNode)
    # for fetching specific branch (filter by id generated by graphene)
    branch = relay.Node.Field(BankBranchNode)

     # for fetching all the banks
    all_banks = DjangoFilterConnectionField(BankNode)
    # for fetching specific bank (filter by id generated by graphene)
    bank = relay.Node.Field(BankNode)
