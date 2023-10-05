import logging as log
from datetime import datetime
import re

logger = log.getLogger(__name__)

def check_participant(name: str):
  """
    Arguments:
      name: str

    Returns:
      score: int

    Examples:
      participant("Anika")
  """
  if not isinstance(name, str):
    log.debug("Participant data type not valid (0/10p)")
    return 0

  # Remove spaces
  name = name.replace(' ', '')

  # Remove emojis
  # print(name.encode())
  regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
  "]+", flags = re.UNICODE)
  name = regrex_pattern.sub(r'',name)
  # print(name.encode())

  if not name or not str(name).replace(" ", "").isalpha() or str(name) in ["deinenNamen", "Ichscheissaufdie10punkte"]:
    log.debug("Participant \"%s\" not valid (0/10p)", name)
    return 0

  log.debug("Participant \"%s\" valid (10/10p)", name)
  return 10




def check_gender(gender_value: str, gender_result: str):
  """
    Arguments:
      gender_value: str
      gender_result: str

    Returns:
      score: int

    Examples:
      gender("Männlich", "Männlich")
  """
  if not isinstance(gender_value, str):
    log.debug("Gender data type not valid (0/30p)")
    return 0

  # Remove spaces
  gender_value = gender_value.replace(' ', '')

  if gender_value.upper() == gender_result.upper():
    log.debug("Gender \"%s\" correct (30/30p)", gender_value)
    return 30

  log.debug("Gender \"%s\" not correct (0/30p)", gender_value)
  return 0






def check_birthdate(birthdate_value: str, birthdate_result: str):
  """
    Arguments:
      birthdate_value: str
      birthdate_result: str

    Returns:
      score: int

    Examples:
      birthdate("2023-08-25", "2023-08-21")
  """

  if not isinstance(birthdate_value, str):
    log.debug("Birthdate data type not valid (0/70p)")
    return 0

  max_score = 70
  score = 0

  value_date = datetime.strptime(birthdate_value, '%Y-%m-%d')
  result_date = datetime.strptime(birthdate_result, '%Y-%m-%d')

  diff_days=(value_date-result_date).days

  # pro abweichender Tag 10 minus
  score = max_score - (abs(diff_days) * 10)

  if score <= 0:
    log.debug("Birthdate \"%s\" not correct (0/70p)", str(value_date).split(' ', 1)[0])
    return 0

  log.debug("Birthdate \"%s\" correct (%i/70p)", str(value_date).split(' ', 1)[0], score)
  return score




def check_firstname(firstname_value: str, firstname_result: str):
  """
    Arguments:
      firstname_value: str
      firstname_result: str

    Returns:
      score: int

    Examples:
      firstname("Anika", "Horsti")
  """
  if not isinstance(firstname_value, str):
    log.debug("Firstname data type not valid (0/100p)")
    return 0

  values = firstname_value.split()
  results = firstname_result.split()
  return_score = 0

  for res_name in results:
    score = 0

    for val_name in values:
      if not val_name or not str(val_name).isalpha():
        log.debug("Firstname \"%s\" not correct (0/100p)", val_name)
        score = 0

      if val_name.upper() == res_name.upper():
        log.debug("Firstname \"%s\" correct (100/100p)", val_name)
        return 100

      if len(val_name) == len(res_name):
        log.debug("Firstname \"%s\" has equal number of characters (+25p)", val_name)
        score += 25

      if val_name[0].upper() == res_name[0].upper():
        log.debug("Firstname \"%s\" has the same initial letter (+25p)", val_name)
        score += 25

      return_score = max(score, return_score)

  log.debug("Firstname \"%s\" correct (summary %i/100p)", firstname_value, return_score)
  return return_score




def check_surname(surname_value: str, surname_result: str):
  """
    Arguments:
      surname_value: str
      surname_result: str

    Returns:
      score: int

    Examples:
      surname("Jandt", "Jandt")
  """
  if not isinstance(surname_value, str):
    log.debug("Surname data type not valid (0/40p)")
    return 0

  score = 0

  if not surname_value or not str(surname_value).isalpha():
    log.debug("Surname \"%s\" not correct (0/40p)", surname_value)
    return 0

  if surname_value.upper() == surname_result.upper():
    log.debug("Surname \"%s\" correct (40/40p)", surname_value)
    return 40

  log.debug("Surname \"%s\" not correct (%i/40p)", surname_value, score)
  return score




def check_weight(weight_value: str, weight_result: str):
  """
    Arguments:
      weight_value: str
      weight_result: str

    Returns:
      score: int

    Examples:
      weight("3000g", "3200")
  """
  if not isinstance(weight_value, str):
    log.debug("Weight data type not valid (0/50p)")
    return 0

  # Remove leading zeros
  weight_value = weight_value.lstrip("0")

  if re.match(r"^[0-9\,\.]*\s*(g|[gG]ramm|[gG]r)\b", weight_value) or \
     re.match(r"^[0-9]{3,5}([\.|\,][0-9]*)?$", weight_value):
    # Gramm
    log.debug("Weight in g: \"%s\"", weight_value)
    weight_value = float(re.sub("[^0-9\. ]", "", weight_value.replace(',', '.')))
  elif re.match(r"^[0-9\,\.]*\s*(kg|[kK]ilo|[kK]ilogramm)\b", weight_value) or \
       re.match(r"^[0-9]{1,3}([\.|\,][0-9]*)?$", weight_value):
    # Kilogramm
    log.debug("Weight: Converting \"%s\"kg to \"%s\"g", weight_value, weight_value * 1000)
    weight_value = float(re.sub("[^0-9\. ]", "", weight_value.replace(',', '.'))) * 1000
  else:
    # Unknowen
    log.debug("Weight \"%s\" not valid (0/50p)", weight_value)
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
    log.debug("Weight \"%s\" not correct (0/50p)", weight_value)
    return 0

  log.debug("Weight \"%s\" correct (%i/50p)", weight_value, score)
  return score




def check_height(height_value: str, height_result: str):
  """
    Arguments:
      height_value: str
      height_result: str

    Returns:
      score: int

    Examples:
      height("330mm", "300")
  """
  if not isinstance(height_value, str):
    log.debug("Height data type not valid (0/50p)")
    return 0

  # Remove leading zeros
  height_value = height_value.lstrip("0")

  if re.match(r"^[0-9]{4}([\.|\,][0-9]*)?$", height_value):
    log.debug("Weight: Converting \"%s\"m to \"%s\"mm", height_value, float(height_value.replace(',', '.')) / 10)
    height_value = float(height_value.replace(',', '.')) / 10
  elif re.match(r"^[0-9\,\.]*\s*(mm|[mM]illimeter)\b", height_value) or \
       re.match(r"^[0-9]{3}([\.|\,][0-9]*)?$", height_value):
    # Millimeter
    log.debug("Height in mm: \"%s\"", height_value)
    height_value = float(re.sub("[^0-9\. ]", "", height_value.replace(',', '.')))
  elif re.match(r"^[0-9\,\.]*\s*([cC]m|[zZ]entimeter|[cC]entimeter)\b", height_value) or \
       re.match(r"^[0-9]{2}([\.|\,][0-9]*)?$", height_value):
    # Zentimeter
    log.debug("Weight: Converting \"%s\"cm to \"%s\"mm", height_value, height_value * 10)
    height_value = float(re.sub("[^0-9\. ]", "", height_value.replace(',', '.'))) * 10
  else:
    # Unknowen
    log.debug("Height \"%s\" not valid (0/50p)", height_value)
    return 0

  # Round and convert to integer
  height_value = int(round(height_value))
  height_result = int(round(float(height_result)))

  diff_height = height_value - height_result
  # print(f"{height_result} - {height_value} Differenz: {abs(diff_height)}")

  max_score = 50
  # pro 5mm (gerundet) Abweichung 5 Punkte weniger
  score = max_score - (int(abs(diff_height / 5)) * 5)

  if score <= 0:
    log.debug("Height \"%s\" not correct (0/50p)", height_value)
    return 0

  log.debug("Height \"%s\" correct (%i/50p)", height_value, score)
  return score
