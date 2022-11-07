from django.shortcuts import render
from .models import Bank, BankBranch

'''
    importBranchDetail view is for adding data from .csv file to Djano Models with foreign field bank_id
'''

def importBranchDetail(request):
    # open csv file
    myFile = open('bank_branches_data.csv', 'r')
    # if an error occurs then either data is available or truncate the data from BankBranch Table
    '''
        Steps to add data to model BankBranch
        1. traverse every line of .csv file
        2. use split method to separate fields from .csv file
        3. Create BankBranch object and pass on the values. bank_id expects object of Bank Model, hence fetcht the object from Bank table
        4. Save BankBranch object to BankBranch Model
    '''
    try:
        for line in myFile:
            line = line.split(',')
            temp = BankBranch.objects.create(
                ifsc=line[0], bank_id=Bank.objects.get(id=int(line[1])), branch=line[2], address=line[3], city=line[4], district=line[5], state=line[6])
            temp.save()
        myFile.close()
        context={'data': 'Data added successfully'}
        return render(request, 'index.html', context)
    except:
        context={'data': 'Data is already added. Truncate table in order to add'}
        return render(request, 'index.html', context)
