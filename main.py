import tkinter as tk
from ui import BattleUI

def main():
    root = tk.Tk()
    app = BattleUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

