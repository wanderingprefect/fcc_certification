class Category:
    #creates a name and empty ledger for new object
    def __init__(self, name):
        self.name = name
        self.ledger = []
    #adds an amount and an optional description to the ledger
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':float(amount), 'description':description})
    #retrieves sum of ledger
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return(balance)
    #checks if funds exceed number in balance
    def check_funds(self, amount):
        if amount > self.get_balance():
            return(False)
        else:
            return(True)
    #withdraws money from ledger if amount does not exceed balance
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(float(-amount), description)
            return(True)
        else:
            return(False)
    #transfers funds from one ledger to another if amount does not exceed balance
    #adds a description of transfer to both ledgers
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return(True)
        else:
            return(False)
    #returns a nicely ordered check of expenses
    def __str__(self):
        balancedCheck = str(self.name)
        balancedCheck = balancedCheck.center(30, '*')
        for i in self.ledger:
            desc = i['description'][:23]
            fl = format(i['amount'], '.2f')[:7]
            addlength = ' ' *(30 - (len(str(fl)) + len(str(desc))))
            balancedCheck += f'\n{desc}{addlength}{fl}'
        balancedCheck += f'\nTotal: {self.get_balance()}'
        return(balancedCheck)

#makes a barchart of all withdrawals
def create_spend_chart(categories):
    chart = 'Percentage spent by category'
    catnames = []
    order = []
    absTotal = 0
    total = {}
    percentage = {}
    #retrieves total amount of withdrawals made and withdrawals made per ledger
    for cat in categories:
        for i in cat.ledger:
            if i['amount'] < 0:
                catnames.append(cat.name)
                total[cat.name] = i['amount']
                absTotal += i['amount']
    for p in total:
        percentage[p] = (total[p]/absTotal)*100
        percentage[p] = (int(percentage[p]) - (int(percentage[p])%10))/10
    #code below is incredibly messy because I asummed it had to be sorted by size of percentage
    #sorts dict by percentage size and adds it to a list
    for p in dict(sorted(percentage.items(), key=lambda item: item[1], reverse=True)):
        order += [p]
    longestname = max(catnames, key=len)
    #start layout of the barchart
    chartcolumns = ['1           ', '0987654321  ','00000000000 ','||||||||||| ']
    #adds apropriate amount of whitespace to the length so it matches the longest name
    for n, i in enumerate(chartcolumns):
        chartcolumns[n] = i + (' '*(len(longestname)))
    #places where the bar chart should be displayed
    places = [1,4,7]
    c = 2
    for i in range(10):
        #adds whitespace if no bar
        if i not in places:
            barchart = '           -'
            barchart += ' '*(len(longestname))
            chartcolumns.append(barchart)
        #adds bar
        else:
            barchart = ' '
            barchart += (' '*(int(9-percentage[order[c]])))
            barchart += ('o'*int(percentage[order[c]]+1))
            barchart += '-'
            barchart += order[c]
            if order[c] != longestname:
                barchart += ' '*(len(longestname)-len(order[c]))
            chartcolumns.append(barchart)
            #more messy code to make the program in order of creation instead of size
            if c == 2:
              c = 0
            elif c == 0:
              c = 1
    #converts the list to a string that's properly formatted
    for i in range(len(chartcolumns[0])):
        chart += '\n'
        for j in chartcolumns:
            chart += j[i]
    return(chart)