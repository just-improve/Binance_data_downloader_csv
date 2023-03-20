from models.model_entry_menu import ModelEntry, ModelUpdate
from views.manager import ManagerView
from controllers.manager import Controller

def main():
    manager_view = ManagerView()
    model_entry = ModelEntry()
    model_update = ModelUpdate()
    controller = Controller(model_entry, model_update, manager_view)
    controller.start()

if __name__ == "__main__":
    main()
