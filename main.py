from controllers.mainFrame import mainFrame
from dao.conn_factory import criar_tab

if __name__ == "__main__":
    criar_tab()
    app = mainFrame()
    app.mainloop()