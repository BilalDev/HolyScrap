# coding: utf-8 

import sys
import hsdb, hshelper, hsrun
import Tkinter as tk

labels = []

class MainApplication(tk.Tk):
	"""Main user interface"""
	def __init__(self):
		tk.Tk.__init__(self)
		# Window maximized
		self.winfo_toplevel().wm_state('zoomed')

		self.MenuBar()
		self.config(menu=self.menuBar)

	def MenuBar(self):
		self.menuBar = tk.Menu(master=self)

		self.fileMenu = tk.Menu(self.menuBar, tearoff=False)
		self.fileMenu.add_command(label='Ajouter anime', underline=0, command=self.quit)
		self.fileMenu.add_command(label='Lister les animés', underline=0, command=self.list_anime)
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label='Quitter', underline=0, command=self.quit)

		self.menuBar.add_cascade(label='Fichier', menu=self.fileMenu)


	def list_anime(self):
		for label in labels:
			label.destroy()

		del labels[:]

		mangas = hsdb.get_animes()

		index = 0
		for manga in mangas:
			labels.append(tk.Label(self, text=manga[0]))
			labels[index].pack()
			index = index + 1


	def quit(self):
		sys.exit(0)
