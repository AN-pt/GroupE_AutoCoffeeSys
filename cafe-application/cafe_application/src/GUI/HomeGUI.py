from tkinter import *
from BLL.DecentralizationBLL import DecentralizationBLL
from BLL.BaristaBLL import BaristaBLL
from GUI.AccountGUI import AccountGUI
from GUI.BillGUI import BillGUI
from GUI.CategoryGUI import CategoryGUI
from GUI.CustomerGUI import CustomerGUI
from GUI.DecentralizationGUI import DecentralizationGUI
from GUI.IngredientGUI import IngredientGUI
from GUI.ProductGUI import ProductGUI
from GUI.ReceiptGUI import ReceiptGUI
from GUI.RecipeGUI import RecipeGUI
from GUI.SaleGUI import SaleGUI
from GUI.BaristaGUI import BaristaGUI
from GUI.SupplierGUI import SupplierGUI
from PIL import Image, ImageTk


class HomeGUI(Frame):
    def __init__(self, account):
        self.__account = account
        self.__barista = BaristaBLL().searchBaristas("BARISTA_ID = '" + self.__account.getBaristaID() + "'")[0]
        self.__decentralization = DecentralizationBLL().searchDecentralizations("DECENTRALIZATION_ID = '" + self.__account.getDecentralizationID() + "'")[0]
        self.__arr = []
        self.__arr.append(0)
        self.__arr.append(self.__decentralization.getIsSale())
        self.__arr.append(self.__decentralization.getIsProduct())
        self.__arr.append(self.__decentralization.getIsCategory())
        self.__arr.append(self.__decentralization.getIsRecipe())
        self.__arr.append(self.__decentralization.getIsImport())
        self.__arr.append(self.__decentralization.getIsBill())
        self.__arr.append(self.__decentralization.getIsWarehouses())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(self.__decentralization.getIsAccount())
        self.__arr.append(self.__decentralization.getIsBarista())
        self.__arr.append(self.__decentralization.getIsCustomer())
        self.__arr.append(self.__decentralization.getIsDiscount())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(1)

        self.__master = Tk()
        self.init_components()


    def init_components(self):
        self.__master.configure(bg="#673c16")
        self.__master.title("Home")
        self.__master.resizable(False, False)
        x_cordinate = int((self.__master.winfo_screenwidth()/2) - (1350/2))
        y_cordinate = int((self.__master.winfo_screenheight()/2) - (760/2))
        self.__master.geometry("{}x{}+{}+{}".format(1350, 760, x_cordinate, y_cordinate))

        self.contentPane = Frame( bg="#ffffff", width=1350, height=760)
        self.contentPane.master = self.__master
        self.contentPane.pack(fill="both", expand=True)

        self.west = Frame(self.contentPane, bg="#673c16", width=300, height=760)
        self.west.pack(side="left")
        self.west.pack(fill="both", expand=True)

        self.info = Frame(self.west, bg="#b27800", width=280, height=80)
        self.info.place(x=10, y=10)

        self.imgAvartar = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/bell-boy.png").resize((60, 60)))

        self.avatar = Label(self.info, image=self.imgAvartar, bg="#b27800")
        self.avatar.place(x=10, y=10)

        self.name = Label(self.info, text="Username: " + self.__barista.getName(), font=("Tahoma", 10), fg="#ffffff", bg="#b27800")
        self.name.place(x=80, y=15)
        self.rule = Label(self.info, text="Role: " + self.__decentralization.getDecentralizationName(), font=("Tahoma", 10), fg="#ffffff", bg="#b27800")
        self.rule.place(x=80, y=40)

        self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/sun.png").resize((30, 30)))
        self.mode = Label(self.info, image=self.imgMode, bg="#b27800")
        self.mode.bind('<Button-1>', self.changeMode)
        self.mode.place(x=230, y=40)
        self.darkMode = True

        self.fram_cate = Frame(self.west, bg="#b27800", width=280, height=650)
        self.fram_cate.place(x=10, y=100)

        self.cate = Frame(self.fram_cate, bg="#b27800", width=260, height=630)
        self.cate.place(x=10, y=10)

        self.panel = []
        self.panel.append(None)
        for i in range(1, 15):
            self.panel.append(Frame(self.cate, bg="#b27800", width=250, height=40))
            self.panel[i].bind('<Button-1>', self.on_panel_click)

        self.label = []
        self.label.append(None)
        self.label.append(Label(self.panel[1], text="Items", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[2], text="Products", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[3], text="Category", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[4], text="Formula", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[5], text="Reciepts", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[6], text="Order Record", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[7], text="Inventory", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[8], text="Statistics", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[9], text="Account", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[10], text="Baristas", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[11], text="Customers", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[12], text="Discounts", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[13], text="Decentralization", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))
        self.label.append(Label(self.panel[14], text="Suppliers", font=("Calibri", 15), fg="#ffffff", bg="#b27800"))

        self.icon = []
        self.image = []
        self.icon.append(None)
        self.image.append(None)
        for i in range(1, 14):
            url = fr"cafe_application/img/icons/{i:02}.png"
            self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30))))
            self.image.append(Label(self.panel[i], image=self.icon[i], bg="#b27800"))
        self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30))))
        self.image.append(Label(self.panel[len(self.label)-1], image=self.icon[len(self.icon)-1], bg="#b27800"))
        self.x = 5
        self.y = 5
        for i in range(1, 15):
            if self.__arr[i] != 0:
                self.panel[i].place(x=self.x, y=self.y)
                self.image[i].place(x=20, y=4)
                self.label[i].place(x=70, y=5)
                self.y = self.y + 45

        for i in range(1, 15):
            for child in self.panel[i].winfo_children():
                child.bind('<Button-1>', self.on_childPanel_click)

        self.east = Frame(self.contentPane, bg="#b27800", width=1040, height=740)
        self.east.place(x=300, y=10)

        self.function = Frame(self.east, bg="#b27800", width=1040, height=740)
        self.function.pack()


        self.__master.mainloop()

    def changeMode(self, event):
        if self.darkMode:
            self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/moon.png").resize((30, 30)))
            self.mode.configure(image=self.imgMode, bg="#d4b37f")

            self.__master.configure(bg="#ffffff")
            self.west.configure(bg="#ffffff")

            self.info.configure(bg="#d4b37f")
            self.avatar.configure(bg="#d4b37f")
            self.name.configure(bg="#d4b37f")
            self.rule.configure(bg="#d4b37f")
            self.fram_cate.configure(bg="#d4b37f")
            self.cate.configure(bg="#d4b37f")

            for i in range(1, 15):
                self.panel[i].configure(bg="#f0f0f0")
                self.image[i].configure(bg="#f0f0f0")
                self.label[i].configure(bg="#f0f0f0", fg="#000000")

            self.darkMode = False
        else:
            self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/sun.png").resize((30, 30)))
            self.mode.configure(image=self.imgMode, bg="#b27800")

            self.__master.configure(bg="#673c16")
            self.west.configure(bg="#673c16")

            self.info.configure(bg="#b27800")
            self.avatar.configure(bg="#b27800")
            self.name.configure(bg="#b27800")
            self.rule.configure(bg="#b27800")
            self.fram_cate.configure(bg="#b27800")
            self.cate.configure(bg="#b27800")

            for i in range(1, 15):
                self.panel[i].configure(bg="#b27800")
                self.image[i].configure(bg="#b27800")
                self.label[i].configure(bg="#b27800", fg="#FFFFFF")

            self.darkMode = True

    def on_panel_click(self, event):
        self.disable()
        for child in event.widget.winfo_children():
            child.configure(background='#673c16')
        event.widget.configure(background='#673c16')
        self.callChildFrom(event.widget)

    def on_childPanel_click(self, event):
        self.disable()
        if self.darkMode:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#673c16')
            parent_frame.configure(background='#673c16')
            self.callChildFrom(parent_frame)
        else:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#44963C')
            parent_frame.configure(background='#44963C')
            self.callChildFrom(parent_frame)

    def disable(self):
        frame = self.cate
        if self.darkMode:
            for child1 in frame.winfo_children():
                child1.configure(background='#b27800')
                for child2 in child1.winfo_children():
                    child2.configure(background='#b27800')
        else:
            for child1 in frame.winfo_children():
                child1.configure(background='#f0f0f0')
                for child2 in child1.winfo_children():
                    child2.configure(background='#f0f0f0')

    def callChildFrom(self, frame):
        if frame == self.panel[1]:
            self.openChildForm(SaleGUI(self.function))
        elif frame == self.panel[2]:
            self.openChildForm(ProductGUI(self.function))
        elif frame == self.panel[3]:
            self.openChildForm(CategoryGUI(self.function))
        elif frame == self.panel[4]:
            self.openChildForm(RecipeGUI(self.function))
        elif frame == self.panel[5]:
            self.openChildForm(ReceiptGUI(self.function))
        elif frame == self.panel[6]:
            self.openChildForm(BillGUI(self.function))
        elif frame == self.panel[7]:
            self.openChildForm(IngredientGUI(self.function))
        elif frame == self.panel[8]:
            pass
        elif frame == self.panel[9]:
            self.openChildForm(AccountGUI(self.function))
        elif frame == self.panel[10]:
            self.openChildForm(BaristaGUI(self.function))
        elif frame == self.panel[11]:
            self.openChildForm(CustomerGUI(self.function))
        elif frame == self.panel[12]:
            pass
        elif frame == self.panel[13]:
            self.openChildForm(DecentralizationGUI(self.function))
        elif frame == self.panel[14]:
            self.openChildForm(SupplierGUI(self.function))


    def openChildForm(self, frame):
        for child in self.function.winfo_children():
            if child != frame:
                child.destroy()
        frame.pack()
        self.function.update()
