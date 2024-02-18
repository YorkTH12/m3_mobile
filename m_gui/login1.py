import tkinter
import mysql.connector
from tkinter import messagebox

cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="db_library")

class Form(tkinter.Frame):

    def __init__(self,parent):
        tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("Login")
        self.parent.config(background="#FF5733")
        self.parent.geometry("350x150")
        self.parent.resizable(False,False)

        global username
        global password

        username = tkinter.StringVar()
        password = tkinter.StringVar()

        self.labelUser = tkinter.Label(self.parent,text="Username: ", background = "#4682B4", foreground = "White", font="Arial 8 bold")
        self.labelUser.place(x=25,y=25)

        self.entryUser = tkinter.Entry(self.parent,textvariable=username)
        self.entryUser.place(x=100,y=25)

        self.labelPass = tkinter.Label(self.parent,text="Password: ", background = "#4682B4", foreground = "White", font="Arial 8 bold")
        self.labelPass.place(x=25,y=50)

        self.entryPass = tkinter.Entry(self.parent,textvariable=password)
        self.entryPass.place(x=100,y=50)

        self.buttonLogin = tkinter.Button(self.parent,text="LOGIN", font=('Open Sans',16,'bold'),bd=0,bg='#87CEEB',fg='white',activebackground='#87CEEB',activeforeground='white',width=17,command=self.logs)

        self.buttonLogin.place(height=45,width=100 ,x=100,y=75)

    def logs(self):
        from subprocess import call
        mycursor = cnx.cursor()
        sql = "SELECT * FROM tb_member WHERE BINARY m_user = '%s' AND BINARY m_pass = '%s'" % (username.get(),password.get())

        mycursor.execute(sql)

        if mycursor.fetchone():
            messagebox.showinfo('Success', 'Login successful!')
            call(["python","user.py"])
            # กรณีเข้าสู่ระบบสำเร็จ ทำอะไรต่อไปก็เช่นกัน
        else:
            messagebox.showerror('Error', 'Username or password incorrect')

def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()

if __name__ == "__main__":
    main()
