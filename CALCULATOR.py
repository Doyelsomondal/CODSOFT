import tkinter as tk


class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("calculator")

        self.entry =tk.Entry(root,width =30 ,borderwidth =5)
        self.entry.grid(row =0, column =0,columnspan =4)


        self.create_buttons()
    def create_buttons(self):
             buttons =[
                 ('7',1,0),('8',1,1),('9',1,2),
                 ('4',2,0),('5',2,1),('6',2,2),
                 ('1',3,0),('2',3,1),('3',3,2),
                 ('0',4,1)

             ]
             for button_text, row, col in buttons:
                 tk.Button(self.root, text=button_text, padx=20, pady=20, command=lambda b=button_text: self.button_click(b)).grid(row=row, column=col)
        
                 
             operation_buttons =[
                 ('+',1,3),('-',2,3),('*',3,3),('/',4,3),
                  ('C',4,0),('=',4,2)
             ]

             for button_text,row,col in operation_buttons:
                 if button_text == "C":
                     tk.Button(self.root,text=button_text,padx =20, pady =20, command= self.button_clear).grid(row =row,column =col)
                 elif button_text == "=":
                     tk.Button(self.root,text=button_text,padx =20, pady =20, command= self.button_equal).grid(row =row,column =col)
                 else:
                     tk.Button(self.root, text=button_text, padx=20, pady=20, command=lambda b=button_text: self.button_click(b)).grid(row=row, column=col)
        
    def button_click(self,number):
          current = self.entry.get()
          self.entry.delete(0,tk.END)
          self.entry.insert(0,current + str(number))

    def button_clear(self):
        self.entry.delete(0,tk.End)


    def button_equal(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0,tk.END)
            self.entry.insert(0,result)

        except Exception:
            self.entry.delete(0,tk.END)
            self.entry.insert(0,"Error")




if __name__ == "__main__":
    root =tk.Tk()
    app = Calculator(root)
    root.mainloop()
            
    





          
