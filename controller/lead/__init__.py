class Lead:
    def __init__(self):
        print("Lead class constructor..!")

    def create(self):
        print("Lead created!")

    def update(self):
        print("Lead updated!")

    def view(self):
        print("View lead!")

# Example usage
lead_instance = Lead()  # Calls the constructor
lead_instance.create()  # Calls the create method
lead_instance.update()  # Calls the update method
lead_instance.view()    # Calls the view method

