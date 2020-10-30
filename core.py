import random
from datetime import datetime
def start_custom_training(amount,operators,difficulty):
    avgseconds = 0
    for i in range(amount):
        right = False
        operation = random.randint(0,len(operators)-1)
        normalgen = False
        first = 0
        second = 0
        result = 0
        answer = 0

        while normalgen == False:
            if (difficulty == 1):
                first = random.randint(1,9)
                second = random.randint(1,9)

            if (difficulty == 2):
                first = random.randint(1,99)
                second = random.randint(1,99)

            if (difficulty == 3):
                first = random.randint(1,999)
                second = random.randint(1,999)

            if (first%second==0):
                normalgen = True    

        start = datetime.now()

        while right == False:
            if (operators[operation] == "+"):
                result = first+second
                answer = int(input(str(first)+"+"+str(second)+"="))

            if (operators[operation] == "-"):
                result = first-second
                answer = int(input(str(first)+"-"+str(second)+"="))

            if (operators[operation] == "*"):
                result = first*second
                answer = int(input(str(first)+"*"+str(second)+"="))

            if (operators[operation] == "/"):
                result = first/second
                answer = int(input(str(first)+"/"+str(second)+"="))

            if (answer == result):
                right = True
                end = datetime.now()
                delta = end - start
                print("Right answer!")
                print("It took:",delta.seconds,"s")
                avgseconds+=delta.seconds
            else:
                print("Wrong answer!")
    avgseconds/=amount
    print("AVG:",avgseconds,"s")