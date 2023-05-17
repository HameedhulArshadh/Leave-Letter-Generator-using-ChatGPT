import os
import datetime
import openai

class LeaveLetterGPT():

    def __init__(self):
        # please make sure that you enter your API-KEY here before running
        openai.api_key = "Enter your API-KEY here"


    def getChatGPTReply(self, message):
        messages = [{"role": "user", "content":message}]
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        return reply

    def verticalSpace(self, lines):
        for i in range(lines):
            print('\n')

    def horizontalLine(self):
        for i in range(70):
            print('-', end="")
        print('\n')

    def greetings(self):
        self.horizontalLine()
        print("\t\t\tWelcome to Leave Letter application!\n")
        self.horizontalLine()

    def options(self):
        print("Please select the type of leave you want to take:")
        print("\t1. Sick leave")
        print("\t2. Festive leave")
        print("\t3. Casual leave")
        print("\t4. Planned vacation leave")
        print("\t5. Compensatory leave")
        print("\t6. others")
        print("\t7. exit")
        while True:
            option = input("Your option: ")
            if option.isdigit():
                option = int(option)
                if option == 7:
                    option = -1
                    break
                elif 1 <= option <= 6:
                    break
                else:
                    print("Please enter a valid number between 1 to 6!")
            else:
                print("Please enter a valid option from the list!")
        return option

    def getName(self):
        while True:
            name = input("Please enter the name: ")
            if len(name) > 0:
                name = name.strip().lower().title()
                break
            else:
                print("Name cannot be empty!")
        return name

    def getDesignation(self):
        while True:
            designation = input("Please enter the designation: ")
            if len(designation) > 0:
                designation = designation.strip().lower().title()
                break
            else:
                print("Designation cannot be empty!")
        return designation

    def getOrganisation(self):
        while True:
            organisation = input("Please enter the organisation: ")
            if len(organisation) > 0:
                organisation = organisation.strip().lower().title()
                break
            else:
                print("Organisation cannot be empty!")
        return organisation

    def getCity(self):
        while True:
            city = input("Please enter the city: ")
            if len(city) > 0:
                city = city.strip().lower().title()
                break
            else:
                print("City cannot be empty!")
        return city

    def getReason(self):
        while True:
            reason = input("Please enter the reason: ")
            if len(reason) > 0:
                reason = reason.strip().lower().title()
                break
            else:
                print("Reason cannot be empty!")
        return reason

    def getDays(self):
        while True:
            days = input("Please enter the number of days: ")
            if len(days) > 0 and days.isdigit() and int(days.isdigit()) >= 0:
                days = int(days)
                if days > 1:
                    days = str(days) + " days"
                    break
                else:
                    days = str(days) + " day"
                    break
            else:
                print("Please enter a valid number of days!")
        return days

    def getFestival(self):
        while True:
            festival = input("Please enter the festival you are going to celebrate: ")
            if len(festival) > 0:
                festival = festival.strip().lower().title()
                break
            else:
                print("festival name cannot be empty!")
        return festival

    def getFromDate(self):
        wrongDate = True
        while True:
            fromDate = input("Please enter the date from which you are taking the leave (dd/mm/yyyy): ")
            if len(fromDate) > 0:
                fromDate = fromDate.strip().lower()
                dataList = fromDate.split('/')

                if str(dataList[0]).isdigit() and str(dataList[1]).isdigit() and str(dataList[2]).isdigit():
                    day = int(dataList[0])
                    month = int(dataList[1])
                    year = int(dataList[2])
                    try:
                        newDate = datetime.datetime(year, month, day)
                        wrongDate = False
                        break
                    except ValueError:
                        wrongDate = True
                        print("Please enter a valid date in (dd/mm/yyyy) format.")
                else:
                    print("Please enter a valid date in (dd/mm/yyyy) format.")
            else:
                print("Date cannot be empty!")
        return fromDate

    def getToDate(self):
        wrongDate = True
        while True:
            toDate = input("Please enter the date from which you are taking the leave (dd/mm/yyyy): ")
            if len(toDate) > 0:
                toDate = toDate.strip().lower()
                dataList = toDate.split('/')

                if str(dataList[0]).isdigit() and str(dataList[1]).isdigit() and str(dataList[2]).isdigit():
                    day = int(dataList[0])
                    month = int(dataList[1])
                    year = int(dataList[2])
                    try:
                        newDate = datetime.datetime(year, month, day)
                        wrongDate = False
                        break
                    except ValueError:
                        wrongDate = True
                        print("Please enter a valid date in (dd/mm/yyyy) format.")
                else:
                    print("Please enter a valid date in (dd/mm/yyyy) format.")
            else:
                print("Date cannot be empty!")
        return toDate

    def getFromDetails(self):
        print("Enter the details of the person who is writing the letter")
        self.horizontalLine()
        FromDetails = {}
        FromDetails["Name"] = self.getName()
        FromDetails["Designation"] = self.getDesignation()
        FromDetails["Organisation"] = self.getOrganisation()
        FromDetails["City"] = self.getCity()
        self.horizontalLine()
        return FromDetails

    def getToDetails(self):
        print("Enter the details of the person to whom the letter is addressed")
        self.horizontalLine()
        ToDetails = {}
        ToDetails["Name"] = self.getName()
        ToDetails["Designation"] = self.getDesignation()
        ToDetails["Organisation"] = self.getOrganisation()
        ToDetails["City"] = self.getCity()
        self.horizontalLine()
        return ToDetails

    def buildFrom(self, FromDetails):
        From = "From:"
        for detail, i in zip(FromDetails.values(), range(len(FromDetails))):
            if i == len(FromDetails) - 1:
                From += ("    " + detail + ".")
            else:
                From += ("    " + detail + ",")
        return From

    def buildTo(self, ToDetails):
        To = "To:"
        for detail, i in zip(ToDetails.values(), range(len(ToDetails))):
            if i == len(ToDetails) - 1:
                To += ("    " + detail + ".")
            else:
                To += ("    " + detail + ",")
        return To

    def letterCreater(self, option, isFile=True):
        if option == -1:
            print("Exiting...")
            exit()

        FromDetails = self.getFromDetails()
        ToDetails = self.getToDetails()
        if option != 5:
            days = self.getDays()

        letter = ""

        if option == 1:
            # call Sick leave
            reason = self.getReason()
            fromDate = self.getFromDate()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a sick or medical leave letter with the subject as "
            letter += f"Requesting sick leave for {days} from {fromDate}."
            letter += f"I am suffering from {reason}. So, I would like to take sick leave {days}."
            letter += "write a leave letter considering this scenario"

        elif option == 2:
            # call Festive leave
            fromDate = self.getFromDate()
            festival = self.getFestival()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a festive leave letter with subject as "
            letter += f"Requesting leave for {days}, to celebrate {festival} from {fromDate}."
            letter += f"I am going to celebrate {festival}. So, I will be taking leave for {days}.I humbly request you to grant me leave for {days}."
            letter += "write a leave letter considering this scenario"

        elif option == 3:
            # call Casual leave
            fromDate = self.getFromDate()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a casual leave letter with subject as "
            letter += f"Sub: Requesting casual leave for {days} from {fromDate}."
            letter += f"I am planning to take casual leave from {fromDate} for {days}. So, I will not be available for {days}. I humbly request you to grant me leave for {days}."
            letter += "write a leave letter considering this scenario"

        elif option == 4:
            # call Planned vacation leave
            fromDate = self.getFromDate()
            toDate = self.getToDate()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a planned vacation leave letter with subject as "
            letter += f"Sub: Requesting planned vacation leave for {days}."
            letter += f"I am going on a planned vacation for {days} from {fromDate} to {toDate}. So, I will not be available duing these {days}. I humbly request you to grant me leave for {days}."
            letter += "write a leave letter considering this scenario"

        elif option == 5:
            # call Compensatory leave
            date = self.getFromDate()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a compensatory leave letter with subject as "
            letter += f"Sub: Requesting compensatory day off on {date}."
            letter += f"I will be taking my compensatory leave on {date}. So, I will not be available on {date}. I humbly request you to apporve my leave."
            letter += "write a leave letter considering this scenario"

        elif option == 6:
            # call generic leave
            reason = self.getReason()
            date = self.getFromDate()
            letter += "The letter is sent by"
            letter += self.buildFrom(FromDetails)
            letter += ". the letter is addressed to"
            letter += self.buildTo(ToDetails)
            letter += "."
            letter += "Hi, write a generic leave letter with subject as "
            letter += f"    Sub: Requesting leave for {days} due to {reason} from {date}."
            letter += f"    I would like to take leave for {reason}. So, I will not be available for {days}. I humbly request you to grant me leave for {days}."
            letter += "write a leave letter considering this scenario"

        else:
            # Just return saying invalid option selected
            print("Please select a valid option and try again!")

        if isFile:
            reply = self.getChatGPTReply(letter)
            with open('LeaveLetter.txt', 'w') as file:
                file.writelines(reply)

            # to open the file in notepad
            os.system(f"notepad.exe LeaveLetter.txt")

            # to open the file in the default text editor
            # webbrowser.open('LeaveLetter.txt')
        else:
            # if writing to file is not desired, just print the result
            reply = self.getChatGPTReply(letter)
            print(reply)





