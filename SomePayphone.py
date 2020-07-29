from datetime import datetime
import os


class Dude:

    def __init__(self, n, s, t, w):
        self.Name = n
        self.Surname = s
        self.Telephone = t
        self.Born = w

    def __str__(self):
        return '\n{0}|{1}|{2}|{3}|'.format(self.Name, self.Surname, self.Telephone, self.Born)

    def get_name(self):
        return self.Name

    def get_surname(self):
        return self.Surname


def CheckName(testing):
    if ord(testing[0][0]) < 65 or ord(testing[0][0]) > 90:
        return False
    return True


def Destruction(People, SomeString):
    name = SomeString.split(' ')[0]
    surname = SomeString.split(' ')[1]
    for people in People:
        if people.Name == name and people.Surname == surname or people.Name == surname and people.Surname == name:
            People.remove(people)
    open('data.txt', 'w').close()
    with open('data.txt', 'w') as writeAgain:
        for dude in People:
            writeAgain.write(dude.__str__())


def InputChecking(testing):
    s = ""
    try:
        #if len(testing) == 3:
        #    testing.append('NO:TG:IVEN')
        if ord(testing[0][0]) < 65 or ord(testing[0][0]) > 90:
            #s += 'Error of name input\n'
            testing[0] = testing[0].capitalize()
        if ord(testing[1][0]) < 65 or ord(testing[1][0]) > 90:
            #s += 'Error of surname input\n'
            testing[1] = testing[1].capitalize()
        if len(testing[2]) == 12 and testing[2][0] + testing[2][1] == '+7':
            testing[2] = testing[2].replace('+', '')
            testing[2] = testing[2].replace(testing[2][0], '8', 1)
        if len(testing[2]) != 11 or testing[2][0] != '8':
            s += 'Error of phone number input\n'
        now = datetime.now()
        if len(testing) == 4 and (int(testing[3].split(':')[0]) > 30 or int(testing[3].split(':')[1]) > 12 or \
                len(testing[3].split(':')[2]) != 4 or int(testing[3].split(':')[2]) > int(now.year)):
            s += 'Error of data input'
        if len(testing) == 3:
            testing.append(None)
        return s
    except Exception:
        return s + 'Exception happens '


def NumberChecking(People,testing):
    for OBJ in People:
        if testing[2] == OBJ.Telephone:
            return False
    return True


def NameAndSurnameChecking(People, testing):
    for OBJ in People:
        if testing[0] == OBJ.Name and testing[1] == OBJ.Surname or testing[0] == OBJ.Surname and testing[1] == OBJ.Name:
            return False
    return True


def Sep():
    return '\n=================================================================================='


if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as Try:
        Try.write('')
    print('The file "data.txt" was created')

AllPerson = list()
with open('data.txt', 'r') as recordingsBeforeUs:
    SomePeople = recordingsBeforeUs.readlines()
for lines in SomePeople:
    if lines != '\n':
        test = lines.split('|')
        AllPerson.append(Dude(test[0], test[1], test[2], test[3]))

print('Here are all the entries')
for people in AllPerson:
    print(Sep()+people.__str__())
print(Sep())
print('Please choice some operation :\n1 - Add person in table\n2 - Change data about person\n'
          '3 - Delete all information about person\n'
          '4 - Find entry by name,surname,number or date of birth\n'
          '5 - Display information about all entries\n'
          '6 - To find out how old the person by name and surname\n'
          '7 - Show information about peoples birthdays which earlier than 30 days\n8 - EXIT')
ready = input()
try:
    while ready != '8':
        #adding
        if ready == '1':
            print('Input some data\nName;Surname;XXXXXXXXXXX;DD:MM:YYYY')
            someData = list(input().split(';'))
            if InputChecking(someData) == "":
                if not NameAndSurnameChecking(AllPerson, someData) or not NumberChecking(AllPerson, someData):
                    print('This man was previously recorded')
                elif NameAndSurnameChecking(AllPerson, someData):
                    AllPerson.append(Dude(someData[0], someData[1], someData[2], someData[3]))
                    with open("data.txt", 'a') as someFile:
                        someFile.write(AllPerson[len(AllPerson)-1].__str__())
            else:
                print(InputChecking(someData))
        if ready == '2':
            print('What value you want to change?(name,surname,phone number or date of birth)\n'
                  '1 - Input name and surname(in this order) to search for\n'
                  '2 - Input number to search for\n3 - Input date of birth to search for')
            answer = input()

            if answer == '1':
                print('Input name and surname(in this order) through the gap to search for')
                answer = input()

                for dude in AllPerson:

                    if dude.Name == answer.split(' ')[0] and dude.Surname == answer.split(' ')[1] or\
                            dude.Surname == answer.split(' ')[0] and dude.Name == answer.split(' ')[1]:
                        print('There is all information about '+answer)
                        print(dude.__str__())
                        print('Name or name you want to change in this entry?\nEnter N\S (N - name,S - surname)')
                        secondAnswer = input()

                        if secondAnswer == 'N':
                            print('Enter new name')
                            nameAnswer = input()
                            testForUnicF = list()
                            testForUnicF.append(nameAnswer)
                            testForUnicF.append(dude.Surname)

                            if CheckName(nameAnswer) and NameAndSurnameChecking(AllPerson, testForUnicF):#
                                print(nameAnswer + ' ' + dude.Surname)
                                dude.Name = nameAnswer.capitalize()#
                                open('data.txt', 'w').close()#
                                with open('data.txt', 'w') as writeAgain:#
                                    for dud in AllPerson:#
                                        writeAgain.write(dud.__str__())#

                            if not NameAndSurnameChecking(AllPerson, testForUnicF):
                                print('In fact, we have this record!Try again!\n'
                                      'To change the data press the "2" in the main menu.')

                        if secondAnswer == 'S':#
                            print('Enter new surname')#
                            surnameAnswer = input()#
                            testForUnic = list()
                            testForUnic.append(dude.Name)
                            testForUnic.append(surnameAnswer)

                            if CheckName(surnameAnswer)and NameAndSurnameChecking(AllPerson, testForUnic):#
                                dude.Surname = surnameAnswer.capitalize()#
                                open('data.txt', 'w').close()#
                                with open('data.txt', 'w') as writeAgain:#
                                    for dud in AllPerson:#
                                        writeAgain.write(dud.__str__())#

                            if not NameAndSurnameChecking(AllPerson, testForUnic):
                                print('In fact, we have this record!Try again!\n'
                                      'To change the data press the "2" in the main menu.')
                    else:
                        print('Input error.Try again')
            if answer == '2':
                print('Input number through the gap to search for')
                answer = input()

                if len(answer) == 11 or len(answer) == 12 and answer[0]+answer[1] == '+7':
                    answer = answer.replace('+', '')
                    answer = answer.replace(answer[0], '8', 1)
                    for obl in AllPerson:

                        if answer == obl.Telephone:
                            print(obl.__str__())
                            print('Enter new number')
                            answer = input()

                            if len(answer) == 11 or len(answer) == 12 and answer[0] + answer[1] == '+7':
                                answer = answer.replace('+', '')
                                answer = answer.replace(answer[0], '8', 1)
                                count = 0
                                for check in AllPerson:

                                    if check.Telephone == answer:
                                        print('In fact, we have this number!Try again!')
                                        count = 42

                                if count == 0:
                                    obl.Telephone = answer
                                    open('data.txt', 'w').close()
                                    with open('data.txt', 'w') as writeAgain:
                                        for dud in AllPerson:
                                            writeAgain.write(dud.__str__())
                else:
                    print('Error of phone number input\n')
            if answer == '3':
                print('Enter the date of birth you want to change')
                answer = input()
                check = 0
                for tryingToChange in AllPerson:
                    if answer == tryingToChange.Born:
                        print('Enter a new date of birth')
                        answer = input()
                        check = True
                        for sym in answer:
                            if not sym.isdigit() and sym != ':':
                                check = False
                        if not check:
                            print('There is no person with such a birth date or a typing error')
                        now1 = datetime.now()
                        if check and int(answer.split(':')[0]) <= 30 and int(answer.split(':')[1]) <= 12 and len(answer.split(':')[0]) <= 2 and len(answer.split(':')[1]) <= 2 and int(answer.split(':')[2]) <= int(now1.year) and len(answer.split(':')[2]) == 4:
                            tryingToChange.Born = answer
                            print('Birth date successfully changed')
                            print(Sep()+tryingToChange.__str__()+Sep())
                        else:
                            print('There is no person with such a birth date or a typing error')
                #if check == 0:
                 #   print('There is no person with such a birth date or a typing error')
                #if check == 1:
                 #   print('Birth date successfully changed')
                  #  print(Sep()+objC.__str__()+Sep())
        if ready == '3':
            print('Want to delete a record by phone number or by name and surname?'
                  '\n1 - Name and surname(Enter through the gap)\n2 - Phone number')
            answerA = input()
            if answerA == '1':
                print('Enter name and surname(Enter through the gap)')
                namesurname = input()
                spase = False
                for symb in namesurname:
                    if symb == ' ':
                        spase = True
                if not spase:
                    print('Input error')
                if spase:
                    resultSearch = namesurname.split(' ')[0].capitalize()+' '+namesurname.split(' ')[1].capitalize()
                    Destruction(AllPerson, resultSearch)
                    print('The data was successfully removed')
            if answerA == '2':
                print('Enter phone number')
                number = input()
                checkN = True
                for n in number:
                    if not n.isdigit() and n != '+':
                        checkN = False
                if not checkN:
                    print('Input error')
                if checkN and number[0]+number[1] == '+7' and len(number) == 12 or len(number) == 11:
                    number = number.replace('+', '')
                    number = number.replace(number[0], '8', 1)
                    for peopleN in AllPerson:
                        if peopleN.Telephone == number:
                            AllPerson.remove(peopleN)
                    open('data.txt', 'w').close()
                    with open('data.txt', 'w') as writeAgain:
                        for dude in AllPerson:
                            writeAgain.write(dude.__str__())
                    print('The data was successfully removed')
        if ready == '4':
            print('Enter the name,surname,phone number or date of birth')
            answerForFind = input()
            if len(answerForFind) == 12 and answerForFind[0] + answerForFind[1] == '+7':
                answerForFind = answerForFind.replace('+', '')
                answerForFind = answerForFind.replace(answerForFind[0], '8', 1)
            else:
                answerForFind = answerForFind.capitalize()
            for personF in AllPerson:
                if answerForFind == personF.Surname or answerForFind == personF.Name or answerForFind == personF.Telephone\
                        or answerForFind == personF.Born:
                    print(Sep() + personF.__str__())
                    print('Want to know how old is this person?\nN\Y')
                    andAgain = input()
                    if andAgain == 'Y':
                        if not personF.Born:
                            print('No data on date of birth')
                        else:
                            now = datetime.now()
                            wasBorn = datetime(int(personF.Born.split(':')[2]), int(personF.Born.split(':')[1]),
                                               int(personF.Born.split(':')[0]))
                            period = now - wasBorn
                            count = period.days - period.days % 365
                            print('This person is {} years'.format(count // 365))
            print(Sep())

        if ready == '5':
            print('Here are all the entries')
            for somePeople in AllPerson:
                print(Sep()+somePeople.__str__())
            print(Sep())

        if ready == '6':
            print('Enter the name and surname (in that order)')
            finallyQuest = input()
            cherry = False
            for symboll in finallyQuest:
                if symboll == ' ':
                    cherry = True
            if cherry:
                nameWB = finallyQuest.split(' ')[0].capitalize()
                surnameWB = finallyQuest.split(' ')[1].capitalize()
                for manORwoman in AllPerson:
                    if nameWB == manORwoman.Name and surnameWB == manORwoman.Surname:
                        now = datetime.now()
                        wasBorn = datetime(int(manORwoman.Born.split(':')[2]), int(manORwoman.Born.split(':')[1]),
                                           int(manORwoman.Born.split(':')[0]))
                        period = now - wasBorn
                        count = period.days - period.days % 365
                        print(Sep() + manORwoman.__str__() + Sep())
                        print('This person is {} years'.format(count // 365))
            if not cherry:
                print('Input error')
        if ready == '7':
            now = datetime.now()
            checkagain = False
            for finallyA in AllPerson:
                if finallyA.Born and int(finallyA.Born.split(':')[1]) <= int(now.month):

                    wasBorn = datetime(int(finallyA.Born.split(':')[2]), int(finallyA.Born.split(':')[1]),
                                       int(finallyA.Born.split(':')[0]))
                    period = now - wasBorn
                    if period.days % 365 <= 30:
                        checkagain = True
                        print(finallyA.__str__())
        print('Please choice some operation :\n1 - Add person in table\n2 - Change data about person\n'
              '3 - Delete all information about person\n'
              '4 - Find entry by name,surname,number or date of birth\n'
              '5 - Display information about all entries\n'
              '6 - To find out how old the person by name and surname\n'
              '7 - Show information about peoples birthdays which earlier than 30 days\n8 - EXIT')

        ready = input()
except IndexError:
   print('Input error.Try again')
except Exception:
   print('Input error.Try again')