from controllers.menu import MenuController
from models.model_entry_menu import ModelEntry, ModelUpdate
from views.manager import ManagerView


class Controller:
    def __init__(self, model_entry: ModelEntry,model_update: ModelUpdate, managerView: ManagerView):
        self.model_entry = model_entry
        self.model_update = model_update
        self.managerView = managerView
        self.menu_controller = MenuController(model_entry, model_update, managerView)

    def start(self):
        self.managerView.start_mainloop()