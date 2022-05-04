def get_event_date(event):  # its a simple function to sort the list
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = {
    Event("2022-01-21 12:38:16", "login", "thispc", "sunny"),
    Event("2022-04-15 10:22:15", "login", "office-machine", "kamal"),
    Event("2022-01-01 00:00:00", "logout", "sunny-pc", "poojitha"),
}

users = current_users(events)
print(users)

generate_report(users)
