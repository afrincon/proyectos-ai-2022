import string
import random
from typing import List, Callable


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportBank:

    def __init__(self, client, dni, transaction, status):
        self.id = generate_id()
        self.client = client
        self.dni = dni
        self.transaction = transaction
        self.status = status

def fifoOrdering(list: List[SupportBank]) -> List[SupportBank]:
    return list.copy()


def filoOrdering(list: List[SupportBank]) -> List[SupportBank]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def randomOrdering(list: List[SupportBank]) -> List[SupportBank]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def blackHoleOrdering(list: List[SupportBank]) -> List[SupportBank]:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets = []

    def create_service(self, client, dni, transaction, status):
        self.tickets.append(SupportBank(client, dni, transaction, status))

    def process_tickets(self, ordering: Callable[[List[SupportBank]], List[SupportBank]]):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportBank):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.dni}")
        print(f"Issue: {ticket.client}")
        print(f"Issue: {ticket.transaction}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_service("John Smith", "999999999", "Credit card expedition", "In progress")
app.create_service("Linus Sebastian", "1111111", "Account open", "Finished")

# process the tickets
app.process_tickets(filoOrdering)