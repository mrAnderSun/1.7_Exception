
#  Функции арифметических операций
def addition(operand1, operand2):
    return print(f'{operand1 + operand2} \n')


def subtraction(operand1, operand2):
    return print(f'{operand1 - operand2} \n')


def implementation(operand1, operand2):
    return print(f'{operand1 * operand2} \n')


def division(operand1, operand2):
    #  проверка деления на ноль
    try:
        local_division = operand1 / operand2
    except ZeroDivisionError:
        print("You cannot do it again ( ZeroDivision )! Remember that!!!")
    else:
      return print(f'{local_division} \n')


#  ВВод данных, глоб. переменных, проверка на первый символ
def data():
  global operation
  global operand1
  global operand2
  operation_base = ("*", "+", "/", "-")

  data = input("Enter Notation: ")
  data_list = data.split()
  operation = data_list[0]
  operand1 = data_list[1]
  operand2 = data_list[2]

  assert operation in operation_base, f'Wrong operation! Need only {operation_base}'

  try:
      if isinstance(int(operand1), int):
          operand1 = int(operand1)
      if isinstance(int(operand2), int):
          operand2 = int(operand2)
  except ValueError:
      print("Wrong operand's Value. Check your data!")
  except TypeError:
      print("Wrong operand's Type. Check your data!")
  else:
    print(f'{operation} {operand1} {operand2}')
    return arithmetic_operation(operation, operand1, operand2)


#####  Сравнение и выполнение функции
def arithmetic_operation(operation, operand1, operand2):

  if operation == "+":
      addition(operand1, operand2)
  elif operation == "-":
      subtraction(operand1, operand2)
  elif operation == "*":
      implementation(operand1, operand2)
  elif operation == "/":
      division(operand1, operand2)


###### MAin
print("Notation from Poland! \n"
      "For example: + 3 4\n")
while True:
  data()