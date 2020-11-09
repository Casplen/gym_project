class Member:
    def __init__(self, first_name, last_name, type, start_date, active_status = True, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.start_date = start_date
        self.active_status = True
        self.id = id

    def deactivate(self):
        self.active_status = False

    def activate(self):
        self.active_status = True