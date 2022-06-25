import tkinter as tk
from tkinter import ttk
import tyre_calculator as t_calc
import database


class Model:
    def __init__(self, widthValue, profileValue, diameterValue):
        self.widthValue = widthValue
        self.profileValue = profileValue
        self.diameterValue = diameterValue

    @property
    def width(self):
        return self._width

    @property
    def profile(self):
        return self._profile

    @property
    def diameter(self):
        return self._diameter


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # title
        self.titleLabel = ttk.Label(
            self, text="Find Alternative Tyre Sizes", font=('Arial', 14, 'bold'))
        self.titleLabel.grid(column=0, row=0, columnspan=2, pady=(0, 10))

        # size labels
        self.widthLabel = ttk.Label(self, text="Tyre Width:")
        self.widthLabel.grid(column=0, row=1, sticky=tk.W, padx=(0, 10))

        self.profileLabel = ttk.Label(self, text="Tyre Profile:")
        self.profileLabel.grid(column=0, row=2, sticky=tk.W, padx=(0, 10))

        self.diameterLabel = ttk.Label(self, text="Tyre Diameter:")
        self.diameterLabel.grid(column=0, row=3, sticky=tk.W, padx=(0, 10))

        # size comboboxes
        self.widthOptions = [145, 155, 165, 175, 185, 195, 205, 215,
                             225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335]
        self.profileOptions = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
        self.diameterOptions = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

        self.widthVar = tk.IntVar(value=205)
        self.widthCombo = ttk.Combobox(
            self, textvariable=self.widthVar, values=self.widthOptions, state='readonly')
        self.widthCombo.grid(column=1, row=1)

        self.profileVar = tk.IntVar(value=55)
        self.profileCombo = ttk.Combobox(
            self, textvariable=self.profileVar, values=self.profileOptions, state='readonly')
        self.profileCombo.grid(column=1, row=2)

        self.diameterVar = tk.IntVar(value=16)
        self.diameterCombo = ttk.Combobox(
            self, textvariable=self.diameterVar, values=self.diameterOptions, state='readonly')
        self.diameterCombo.grid(column=1, row=3)

        # search button
        self.searchButton = ttk.Button(
            self, text='Search', command=self.search_button_clicked)
        self.searchButton.grid(column=1, row=4, sticky='we')

        # size label
        self.sizeLabel = ttk.Label(self, text="Alternative \nSizes")
        self.sizeLabel.grid(column=0, row=5, sticky='w', padx=(0, 10))

        # size listbox
        self.sizesVar = tk.StringVar()
        self.sizeListbox = tk.Listbox(self, listvariable=self.sizesVar)
        self.sizeListbox.grid(column=1,
                              row=5, sticky='nwes', pady=(10, 0))

        # set controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def search_button_clicked(self):
        if self.controller:
            # Return tuple of alternative sizes
            alt_sizes = self.controller.searchSizes(
                self.widthVar.get(), self.profileVar.get(), self.diameterVar.get())
            self.sizesVar.set(alt_sizes)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def searchSizes(self, tyreWidth, tyreProfile, tyreDiameter):
        """
        Search database for alternative tyre sizes
        :param tyre size:
        :return array:
        """
        try:
            # do something
            print("I am searching for a tyre size")
            rolling_radius = t_calc.calc_rolling_radius(
                tyreWidth, tyreProfile, tyreDiameter)
            alt_sizes = database.find_similar_sizes(rolling_radius)
            return tuple(alt_sizes)
        except:
            # print error
            print("Couldn't find an alternative size.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tyre Size Calculator")

        # create a model
        model = Model(205, 55, 16)

        # create view
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create controler
        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
