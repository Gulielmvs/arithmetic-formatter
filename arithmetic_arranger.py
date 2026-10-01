def arithmetic_arranger(problems, display=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  row_operands1 = ''
  row_operands2 = ''
  row_dashes = ''
  row_answers = ''

  for item in problems:
    if '+' in item:
      operator = '+'
    elif '-' in item:
      operator = '-'
    else:
      return 'Error: Operator must be \'+\' or \'-\'.'

    operands = item.split(operator)
    operands[0] = operands[0].strip()
    operands[1] = operands[1].strip()

    # Two operands only digits
    if len(operands) != 2 or not operands[0].isdigit() or \
                  not operands[1].isdigit():
      return 'Error: Numbers must only contain digits.'
    # No more than four digits
    if len(operands[0]) > 4 or len(operands[1]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    # addition or subtraction
    if operator == '+':
      answer = int(operands[0]) + int(operands[1])
    elif operator == '-':
      answer = int(operands[0]) - int(operands[1])

    # Spaces
    if len(operands[0]) <= len(operands[1]):
      dashes = '-' * (len(operands[1]) + 2)
      spaces_operand1 = ' ' * (len(dashes) - len(operands[0]))
      spaces_operand2 = ' '
    else:
      dashes = '-' * (len(operands[0]) + 2)
      spaces_operand1 = ' ' * 2
      spaces_operand2 = ' ' * (len(dashes) - len(operands[1]) - 1)
    spaces_answer = ' ' * (len(dashes) - len(str(answer)))
    spaces_problem = ' ' * 4

    # Concatenating
    row_operands1 = row_operands1 + \
                  spaces_operand1 + operands[0] + spaces_problem
    row_operands2 = row_operands2 + operator + \
                  spaces_operand2 + operands[1] + spaces_problem
    row_dashes = row_dashes + dashes + spaces_problem
    row_answers = row_answers + spaces_answer + \
                  str(answer) + spaces_problem

  # Removing all extra spaces from each row
  row_operands1 = row_operands1.rstrip()
  row_operands2 = row_operands2.rstrip()
  row_dashes = row_dashes.rstrip()
  row_answers = row_answers.rstrip()

  # Problems arranged vertically
  if display:
    arranged_problems = row_operands1 + '\n' + row_operands2 + \
                '\n' + row_dashes + '\n' + row_answers
  else:
    arranged_problems = row_operands1 + '\n' + row_operands2 + '\n' + row_dashes
  return arranged_problems
