from controllers.mainFrame import mainFrame
from dao.connFactory import dao

if __name__ == "__main__":
    banco = dao()
    app = mainFrame()
    app.mainloop()