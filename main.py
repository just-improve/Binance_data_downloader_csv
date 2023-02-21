from models.model_entry_menu import ModelEntry
from views.manager import ManagerView
from controllers.manager import Controller

def main():
    manager_view = ManagerView()
    model_entry = ModelEntry()
    controller = Controller(model_entry, manager_view)
    controller.start()

if __name__ == "__main__":
    main()
