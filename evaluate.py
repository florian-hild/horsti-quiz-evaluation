#!/usr/bin/env python3

"""
-------------------------------------------------------------------------------
Author        : Florian Hild
Created       : 2023-07-09
Python version: 3.x
Description   :
-------------------------------------------------------------------------------
"""

__VERSION__ = '1.0.0'

import logging as log
import argparse
import sys

import pandas
from prettytable import PrettyTable

from module_valuate import (
  participant,
  gender,
  birthdate,
  firstname,
  surname,
  weight,
)

resultset = {
  'gender': "Divers",
  'birthdate': '2023-08-21',
  'firstname': 'Test01',
  'surname': 'Hindt',
  'weight': '3333',
  'height': '333',
}
cvs_cols = ["Teilnehmer", "Geschlecht", "Geburtstermin", "Name", "Nachname", "Geburtsgewicht in g", "Körpergröße in mm"]


def main():
  log.basicConfig(
    format='[%(levelname)8s] %(message)s',
  )

  parser = argparse.ArgumentParser(
    description='Evaluate cvs file from Horsie Quiz.',
    prog='evaluate.py',
    usage='%(prog)s [options]',
    add_help=False,
  )

  parser.add_argument(
    '-V', '--version',
    help="Print version number and exit.",
    action='version',
    version=f"%(prog)s version {__VERSION__}",
  )

  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument(
    '-h', '--help',
    help='Print a short help page describing the options available and exit.',
    action='help',
  )

  parser.add_argument(
    '-v', '--verbose',
    help='Verbose mode. Print debugg messages. Multiple -v options increase the verbosity. The maximum is 3.',
    action='count',
    default=0,
  )

  parser.add_argument(
    "-c", "--cvs",
    action="store",
    metavar="file",
    type=str,
  )

  args = parser.parse_args()

  if args.verbose == 0:
    log.getLogger().setLevel(log.WARN)
  elif args.verbose == 1:
    log.getLogger().setLevel(log.INFO)
  else:
    log.getLogger().setLevel(log.DEBUG)

  if not args.cvs:
    log.error("No cvs-file provided.")
    parser.print_help()
    sys.exit(1)

  log.info("Read cvs data from %s", args.cvs)
  log.info("Using columns: {}".format(', '.join(map(str, cvs_cols))))
  cvs_data = pandas.read_csv(
    args.cvs,
    usecols=cvs_cols,
  )

  result_table = PrettyTable()
  result_table.header = True
  result_table.field_names = [
    "Participant",
    "Res1",
    "Gender",
    "Res2",
    "Birthdate",
    "Res3",
    "Firstname",
    "Res4",
    "Surname",
    "Res5",
    "Weight",
    "Res6",
    "Height",
    "Res7",
    "Total res",
  ]

  # Iterate through each row and select columns
  cvs_data = cvs_data.reset_index()  # make sure indexes pair with number of rows
  for index, row in cvs_data.iterrows():
    log.debug("----------------------------------------")
    log.debug("Evaluation for \"%s\"", row["Teilnehmer"])
    participant_result = participant(row["Teilnehmer"])
    gender_result = gender(row["Geschlecht"], resultset["gender"])
    birthdate_result = birthdate(row["Geburtstermin"], resultset["birthdate"])
    firstname_result = firstname(row["Name"], resultset["firstname"])
    surname_result = surname(row["Nachname"], resultset["surname"])
    weight_result = weight(row["Geburtsgewicht in g"], resultset["weight"])
    # height_result = height(row["Körpergröße in mm"], resultset["height"])
    height_result = 0

    result_table.add_row([
      row["Teilnehmer"],
      participant_result,
      row["Geschlecht"],
      gender_result,
      row["Geburtstermin"],
      birthdate_result,
      row["Name"],
      firstname_result,
      row["Nachname"],
      surname_result,
      row["Geburtsgewicht in g"],
      weight_result,
      row["Körpergröße in mm"],
      height_result,
      participant_result + gender_result + birthdate_result + firstname_result + surname_result + weight_result + height_result
    ])

  result_table.sortby = "Total res"
  result_table.align = "l"
  print(result_table)

if __name__ == '__main__':
  main()
