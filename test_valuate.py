import unittest
from module_valuate import (
  participant,
  gender,
  birthdate,
  firstname,
  surname,
  weight,
)
from evaluate import resultset

class TestValuation(unittest.TestCase):
  """
  Unit class
  """

  def test_participant(self):
    """
    Unit test participant
    """
    self.assertEqual( participant("test"), 10 )
    self.assertEqual( participant("Max Mustermann"), 10 )
    self.assertEqual( participant(""), 0 )
    self.assertEqual( participant("test01"), 0 )
    self.assertEqual( participant("Diana und Patrick"), 10 )
    self.assertEqual( participant("deinen Namen"), 0 )




  def test_gender(self):
    """
    Unit test gender
    """
    self.assertEqual( gender("Männlich", resultset['gender']), 30 )
    self.assertEqual( gender("Weiblich", resultset['gender']), 0 )
    self.assertEqual( gender("Divers", resultset['gender']), 0 )




  def test_birthdate(self):
    """
    Unit test birthdate
    """
    self.assertEqual( birthdate("2023-08-21", resultset['birthdate']), 70 )
    self.assertEqual( birthdate("2023-08-20", resultset['birthdate']), 60 )
    self.assertEqual( birthdate("2023-08-22", resultset['birthdate']), 60 )
    self.assertEqual( birthdate("2023-08-15", resultset['birthdate']), 10 )
    self.assertEqual( birthdate("2023-06-21", resultset['birthdate']), 0 )
    self.assertEqual( birthdate("2023-10-21", resultset['birthdate']), 0 )




  def test_firstname(self):
    """
    Unit test firstname
    """
    self.assertEqual( firstname("Horsti", resultset['firstname']), 100 )
    self.assertEqual( firstname("Hans", resultset['firstname']), 25 )
    self.assertEqual( firstname("iiiiii", resultset['firstname']), 25 )
    self.assertEqual( firstname("Helmut", resultset['firstname']), 50 )
    self.assertEqual( firstname("", resultset['firstname']), 0 )
    self.assertEqual( firstname("Horsti122", resultset['firstname']), 0 )




  def test_surname(self):
    """
    Unit test surname
    """
    self.assertEqual( surname("Jandt", resultset['surname']), 40 )
    self.assertEqual( surname("Hild", resultset['surname']), 0 )
    self.assertEqual( surname("Hindt", resultset['surname']), 0 )
    self.assertEqual( surname("Jald", resultset['surname']), 0 )
    self.assertEqual( surname("", resultset['surname']), 0 )
    self.assertEqual( surname("Jald123", resultset['surname']), 0 )




  def test_weight(self):
    """
    Unit test weight
    max. 50p
    pro 50g Abweichung gerundet 5p weniger
    """
    self.assertEqual( weight("3150", resultset['weight']), 50 )
    self.assertEqual( weight("3150g", resultset['weight']), 50 )
    self.assertEqual( weight("3.15", resultset['weight']), 50 )
    self.assertEqual( weight("3200g", resultset['weight']), 45 )
    self.assertEqual( weight("3.13", resultset['weight']), 50 )
    self.assertEqual( weight("03.13", resultset['weight']), 50 )
    self.assertEqual( weight("03120", resultset['weight']), 50 )
    self.assertEqual( weight("100,6", resultset['weight']), 0 )
    self.assertEqual( weight("3,6123", resultset['weight']), 5 )



if __name__ == '__main__':
  unittest.main(verbosity=2)
