import logging
logging.basicConfig(level=logging.INFO)

def calculator(action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "), num1 = float(input("Podaj składnik 1: ")), num2 = float(input("Podaj składnik 2: "))):
    if action == "1":
        numbers = []
        res = num1+num2
        res = float(res)
        nums_text = input("Proszę podać więcej liczb do działania, rozdzielając je przecinkiem: ")
        if nums_text != "":
            nums = nums_text.split(',')
            for num in nums:
                num = float(num)
                res+=num
                numbers.append(num)
            logging.info(f"Dodaję {num1} i {num2} i {numbers}")
            print(f"Wynik: {res}")
        else:
            logging.info(f"Dodaję {num1} i {num2}")
            print(f"Wynik: {num1 + num2}")
    elif action == "2":
        logging.info(f"Odejmuję {num1} i {num2}")
        print(num1-num2)
    elif action == "3":
        numbers = []
        res = num1 + num2
        res = float(res)
        nums_text = input("Proszę podać więcej liczb do działania, rozdzielając je przecinkiem: ")
        if nums_text != "":
            nums = nums_text.split(',')
            for num in nums:
                num = float(num)
                res = res * num
                numbers.append(num)
            logging.info(f"Mnożę {num1} i {num2} i {numbers}")
            print(f"Wynik: {res}")
        else:
            logging.info(f"Mnożę {num1} i {num2}")
            print(f"Wynik: {num1 * num2}")
    elif action == "4":
        logging.info(f"Dzielę {num1} i {num2}")
        print(num1/num2)


calculator()