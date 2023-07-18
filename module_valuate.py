from datetime import datetime
import re

def participant(name: str):
  """
    Arguments:
      name: str

    Returns:
      score: int

    Examples:
      participant("Anika")
  """

  if not name or not str(name).replace(" ", "").isalpha() or str(name) in ["deinen Namen",]:
    # print("Teilnehmer not valide. (0p)")
    # print("Teilnehmer: "+name)
    return 0

  # print("Teilnehmer valide. (10p)")
  # print("Teilnehmer: "+name)
  return 10




def gender(gender_value: str, gender_result: str):
  """
    Arguments:
      gender_value: str
      gender_result: str

    Returns:
      score: int

    Examples:
      gender("Männlich", "Männlich")
  """

  if gender_value.upper() == gender_result.upper():
    return 30

  return 0





def birthdate(birthdate_value: str, birthdate_result: str):
  """
    Arguments:
      birthdate_value: str
      birthdate_result: str

    Returns:
      score: int

    Examples:
      birthdate("2023-08-25", "2023-08-21")
  """

  max_score = 70
  score = 0

  value_date = datetime.strptime(birthdate_value, '%Y-%m-%d')
  result_date = datetime.strptime(birthdate_result, '%Y-%m-%d')

  diff_days=(value_date-result_date).days

  # pro abweichender Tag 10 minus
  score = max_score - (abs(diff_days) * 10)

  if score <= 0:
    return 0

  return score




def firstname(firstname_value: str, firstname_result: str):
  """
    Arguments:
      firstname_value: str
      firstname_result: str

    Returns:
      score: int

    Examples:
      firstname("Anika", "Horsti")
  """
  score = 0

  if not firstname_value or not str(firstname_value).isalpha():
    # print("Name not valide. (0p)")
    return 0

  if firstname_value.upper() == firstname_result.upper():
    # print("Name is equal. (100p)")
    return 100

  if len(firstname_value) == len(firstname_result):
    # print("Name has equal number of characters. (25p)")
    score += 25

  if firstname_value[0].upper() == firstname_result[0].upper():
    # print("Name has the same initial letter. (25p)")
    score += 25

  return score




def surname(surname_value: str, surname_result: str):
  """
    Arguments:
      surname_value: str
      surname_result: str

    Returns:
      score: int

    Examples:
      surname("Jandt", "Jandt")
  """
  score = 0

  if not surname_value or not str(surname_value).isalpha():
    # print("Nachname not valide. (0p)")
    return 0

  if surname_value.upper() == surname_result.upper():
    # print("Nachname is equal. (40p)")
    return 40

  return score




def weight(weight_value: str, weight_result: str):
  """
    Arguments:
      weight_value: str
      weight_result: str

    Returns:
      score: int

    Examples:
      weight("3000g", "3200")
  """
  # Remove leading zeros
  weight_value = weight_value.lstrip("0")

  if re.match(r".*(g|gramm|Gramm|Gr)", weight_value):
    # Gramm
    weight_value = float(re.sub("[^0-9\.]", "", weight_value.replace(',', '.')))
  elif re.match(r".*(kg|kilogramm|Kilogramm|Kilo)", weight_value):
    # Kilogramm
    weight_value = float(re.sub("[^0-9\.]", "", weight_value.replace(',', '.'))) * 1000
  else:
    if re.match(r"^[0-9]{3,5}(,\.)?[0-9]*", weight_value):
      # Gramm
      weight_value = float(weight_value.replace(',', '.'))
    elif re.match(r"^[0-9]{1,3}(,\.)?[0-9]*", weight_value):
      # Kilogramm
      weight_value = float(weight_value.replace(',', '.')) * 1000
    else:
      # Unknowen
      return 0

  # Round and convert to integer
  weight_value = int(round(weight_value))
  weight_result = int(round(float(weight_result)))

  diff_weight = weight_value - weight_result
  # print(f"{weight_result} - {weight_value} Differenz: {abs(diff_weight)}")

  max_score = 50
  # pro 50g Abweichung gerundet 5p weniger
  score = max_score - (int(abs(diff_weight / 50)) * 5)

  if score <= 0:
    return 0

  return score
