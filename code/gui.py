#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Wed Sep  2 14:02:16 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import rootcode
# end wxGlade


class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyFrame.__init__
		kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((400, 180))
		
		# Menu Bar
		self.MenuBar = wx.MenuBar()
		wxglade_tmp_menu = wx.Menu()
		item = wxglade_tmp_menu.Append(wx.ID_ANY, "Create Mod File from INT", "Create a mod file from INT files.")
		self.Bind(wx.EVT_MENU, self.create_mod_file, id=item.GetId())
		item = wxglade_tmp_menu.Append(wx.ID_ANY, "View Mod Info", "View a mod file's info.")
		self.Bind(wx.EVT_MENU, self.view_mod_info, id=item.GetId())
		item = wxglade_tmp_menu.Append(wx.ID_ANY, "About", "Info about this program")
		self.Bind(wx.EVT_MENU, self.about_menu, id=item.GetId())
		self.MenuBar.Append(wxglade_tmp_menu, "File")
		wxglade_tmp_menu = wx.Menu()
		item = wxglade_tmp_menu.Append(wx.ID_ANY, "Ignore ISO/Mod Region", "Automatically, this program detects when mods are incompatible with the ISO you give them, based on region.", wx.ITEM_CHECK)
		self.Bind(wx.EVT_MENU, self.ignore_mod_region, id=item.GetId())
		self.MenuBar.Append(wxglade_tmp_menu, "Settings")
		self.SetMenuBar(self.MenuBar)
		# Menu Bar end
		self.ChooseImage = wx.Button(self, wx.ID_ANY, "Choose ISO")
		self.ChooseFile = wx.Button(self, wx.ID_ANY, "Choose File")
		self.Start = wx.Button(self, wx.ID_ANY, "Start")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.choose_image_event, self.ChooseImage)
		self.Bind(wx.EVT_BUTTON, self.choose_file_event, self.ChooseFile)
		self.Bind(wx.EVT_BUTTON, self.start_event, self.Start)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("ptr2inject")
		self.ChooseImage.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
		self.ChooseImage.SetToolTip("This button chooses your Parappa The Rapper 2 ISO image.")
		self.ChooseFile.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
		self.ChooseFile.SetToolTip("This button selects the .PTR2MOD file you want to inject.")
		self.Start.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
		self.Start.SetToolTip("This button begins the ISO injection. Once you click this, you will be asked where to save the newly created ISO.")
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		RootSizer = wx.BoxSizer(wx.HORIZONTAL)
		RootSizer.Add(self.ChooseImage, 1, wx.ALL | wx.EXPAND, 8)
		RootSizer.Add(self.ChooseFile, 1, wx.ALL | wx.EXPAND, 8)
		RootSizer.Add(self.Start, 2, wx.ALL | wx.EXPAND, 8)
		self.SetSizer(RootSizer)
		self.Layout()
		# end wxGlade

	def create_mod_file(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'create_mod_file' not implemented!")
		event.Skip()

	def view_mod_info(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'view_mod_info' not implemented!")
		event.Skip()

	def about_menu(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'about_menu' not implemented!")
		event.Skip()

	def ignore_mod_region(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'ignore_mod_region' not implemented!")
		event.Skip()

	def choose_image_event(self, event):  # wxGlade: MyFrame.<event_handler>
		print("hello")
        
	def choose_file_event(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'choose_file_event' not implemented!")
		event.Skip()
	def start_event(self, event):  # wxGlade: MyFrame.<event_handler>
		print("Event handler 'start_event' not implemented!")
		event.Skip()
# end of class MyFrame

class MyDialog(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: MyDialog.__init__
		kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLOSE_BOX
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetSize((320, 220))

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: MyDialog.__set_properties
		self.SetTitle("About ptr2inject")
		self.SetSize((320, 220))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyDialog.__do_layout
		AboutRootSizer = wx.BoxSizer(wx.VERTICAL)
		AboutText = wx.StaticText(self, wx.ID_ANY, "Program created by JMK\n\nThis program is free.\nHow to use: \n1. Choose your Parappa The Rapper 2 ISO\n2. Choose your mod file\n3. Click \"Start\" \n4. Profit", style=wx.ALIGN_CENTER)
		AboutText.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
		AboutRootSizer.Add(AboutText, 1, wx.ALL | wx.EXPAND, 20)
		self.SetSizer(AboutRootSizer)
		self.Layout()
		# end wxGlade

# end of class MyDialog

class MyApp(wx.App):
	def OnInit(self):
		self.RootFrame = MyFrame(None, wx.ID_ANY, "")
		self.SetTopWindow(self.RootFrame)
		self.RootFrame.Show()
		return True

# end of class MyApp

if __name__ == "__main__":
	app = MyApp(0)
	app.MainLoop()
