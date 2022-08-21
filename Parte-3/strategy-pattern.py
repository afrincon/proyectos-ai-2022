import string
import random
from typing import List


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


class CustomerSupport:

    def __init__(self, processing_strategy: str = "fifo"):
        self.supports = []
        self.processing_strategy = processing_strategy

    def create_service(self, client, dni, transaction, status):
        self.supports.append(SupportBank(client, dni, transaction, status))

    def process_tickets(self):
        # if it's empty, don't do anything
        if len(self.supports) == 0:
            print("There are no tickets to process. Well done!")
            return

        if self.processing_strategy == "fifo":
            for ticket in self.supports:
                self.process_ticket(ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.supports):
                self.process_ticket(ticket)
        elif self.processing_strategy == "random":
            list_copy = self.supports.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportBank):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Client DNI: {ticket.dni}")
        print(f"Customer: {ticket.client}")
        print(f"Issue: {ticket.transaction}")
        print(f"Issue: {ticket.status}")
        print("==================================")


# create the application
app = CustomerSupport("filo")

# register a few tickets
app.create_service("John Smith", "999999999", "Credit card expedition", "In progress")
app.create_service("Linus Sebastian", "1111111", "Account open", "Finished")

# process the tickets
app.process_tickets()