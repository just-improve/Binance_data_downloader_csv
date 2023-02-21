class MenuController:
    def __init__(self, model_entry, manager_view):
        self.model = model_entry
        self.manager_view = manager_view
        self.frame = self.manager_view.frames["menu"]
        self._bind()


    def _bind(self):
        self.frame.test_btn.config(command=self.printer)

    def printer(self):
        print('fsdf')
    # def go_to_sing_out(self):
    #     self.manager_view.switch('signup')
