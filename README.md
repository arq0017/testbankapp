# testbankapp

Assignment: 

## Configure project
1. create an environment and install all required packages using
    * ```pip install -r requirements.txt```
  
2. Run the following commands inside the root directory:
    * ```python manage.py makemigrations```
    * ```python manage.py migrate```

3. Once all models have been migrated, now dump data into models using fixtures
    * First load Bank model data
      * ```python manage.py loaddata bank.json```
    * Now load Bankbranch.json . it may take some time 
      * ```python manage.py loaddata bankbranch.json```

<img width="423" alt="Screenshot 2022-11-08 at 12 18 04 AM" src="https://user-images.githubusercontent.com/70997750/200396723-4d5304f2-6681-4581-aa43-db90e4b2a1a4.png">


4. After dumping data into models, create superuser
    * ```python manage.py createsuperuser```
5. Now run the server
    * ```python manage.py runserver```
  
  
Using superuser credentials, login to ```http://127.0.0.1:8000/admin``` and now you will see two tables - **Branch** and **BankBranch**.  
Note: BankBranch has a foreign key bank_id to the Branch table

<img width="485" alt="Screenshot 2022-11-08 at 12 09 43 AM" src="https://user-images.githubusercontent.com/70997750/200396106-291e6b61-70a5-4277-809d-6d3e85072024.png">

## Encountering error while dumping data </h1>
Note: you may get the error while dumping data to Bankbranch. Hence I am providing a CSV file. 
Therefore, go to ```http://127.0.0.1::8000/addData``` and you will get a page dictating whether data has been added or not. 

### Query API 
Go to ```http://localhost:8000/gql``` in order to perform GraphQL queries : 

1. Get all branches with subclasses 
<img width="972" alt="Screenshot 2022-11-08 at 12 23 45 AM" src="https://user-images.githubusercontent.com/70997750/200396350-a34e178e-2756-40a2-9817-c434bf1902b2.png">

2. Get a specific branch
<img width="877" alt="Screenshot 2022-11-08 at 12 27 45 AM" src="https://user-images.githubusercontent.com/70997750/200396407-d6909a82-e767-4b7b-9019-6f2b751603d7.png">

3. Get all banks 
4. Get a specific bank

## Added Test for all GraphQL queries

<img width="762" alt="Screenshot 2022-11-08 at 12 36 42 AM" src="https://user-images.githubusercontent.com/70997750/200396577-7a1550b4-d69b-4405-bd8a-87aad4886d2e.png">



