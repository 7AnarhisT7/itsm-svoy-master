tickets = []

def create_ticket(title, client):
    ticket = {
        "id" : len(tickets) + 1,
        "title" : title,
        "client" : client,
        "status" : "Открыта"
    }
    tickets.append(ticket)
    return ticket

def change_status(ticket_id, new_status):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = new_status
            return ticket
    return None

def show_tickets():
    for ticket in tickets:
        print(f"#{ticket['id']} | {ticket['client']} | {ticket['title']} | {ticket['status']}")

create_ticket("Течет труба", "Ресторан Мираж")
create_ticket("Не работает интернет", "Кафе Вкусняшка")
change_status(1, "В работе")
show_tickets()
result = change_status(99, "закрыта")
print(result)