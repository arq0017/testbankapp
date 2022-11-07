import requests


# for testing specific branch
def test_branch():
    query = '''
     {
          branch(id:"QmFua0JyYW5jaE5vZGU6QUJIWTAwNjUwMDE="){
               ifsc
          }
     }
     '''
    response = requests.post("http://127.0.0.1:8000/gql",
                             json={'query': query})
    response_body = response.json()
    assert response_body['data']['branch']['ifsc'] == "ABHY0065001"


# for testing all branches
def test_all_branches():
    query = '''
     {
          allBranches {
               edges {
                    node {
                         bankId {
                              name
                         }
                    }
               }
          }
     }
     '''
    response = requests.post("http://127.0.0.1:8000/gql",
                             json={'query': query})
    response_body = response.json()
    assert response_body['data']['allBranches']['edges'][0]['node']['bankId']['name'] == "ABHYUDAYA COOPERATIVE BANK LIMITED"


# for testing specific bank
def test_bank():
    query = '''
     {
          bank(id:"QmFua05vZGU6MQ=="){
               name
          }
     }
     '''
    response = requests.post("http://127.0.0.1:8000/gql",
                             json={'query': query})
    response_body = response.json()
    assert response_body['data']['bank']['name'] == "STATE BANK OF INDIA"


# for testing all banks
def test_all_banks():
    query = '''
     {
          allBanks {
               edges {
                    node {
                         name
                    }
               }
          }
     }
     '''
    response = requests.post("http://127.0.0.1:8000/gql",
                             json={'query': query})
    response_body = response.json()
    assert response_body['data']['allBanks']['edges'][0]['node']['name'] == "STATE BANK OF INDIA"
