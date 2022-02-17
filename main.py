from helpers import (
   spanish_fruits,
   brazilian_fruits,
   japanese_fruits,
   popular_fruits,
   emails
)

def spanish_and_brazilian_fruits(spanish_fruits: set, brazilian_fruits: set) -> list:
    return(list(spanish_fruits & brazilian_fruits))


def spanish_and_japan_fruits(spanish_fruits: set, japanese_fruits: set) -> list:
    return(list(spanish_fruits & japanese_fruits))


def brazilian_and_japan_fruits(brazilian_fruits: set, japanese_fruits: set) -> list:
    return(list(brazilian_fruits & japanese_fruits))


def popular_spanish_or_brazilian_fruits(
    popular_fruits: set, spanish_fruits: set, brazilian_fruits: set
    ) -> list:
    return(list(popular_fruits & spanish_fruits | brazilian_fruits))


def popular_only_spanish_fruits(
    popular_fruits: set, spanish_fruits: set, japanese_fruits, brazilian_fruits: set
    ) -> list:
    return(list(popular_fruits & spanish_fruits - japanese_fruits | brazilian_fruits))


def only_yahoo_emails(emails_list: list) -> set:
    return(set(filter(lambda word: 'yahoo' in word.lower() ,emails_list)))


def only_hotmail_emails(emails_list: list) -> set:
    return(set(filter(lambda word: 'hotmail' in word.lower() ,emails_list)))


def only_br_emails(emails_list: list) -> set:
    return(set(filter(lambda word: 'br' in word[-2::].lower() ,emails_list)))
