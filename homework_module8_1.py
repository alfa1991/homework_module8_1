def add_everything_up(a, b):
  """Складывает числа и строки.

  Args:
    a: Число или строка.
    b: Число или строка.

  Returns:
    Результат сложения или конкатенации.
  """

  if type(a) != type(b):
    return str(a) + str(b)
  else:
    return a + b

# Примеры использования:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))