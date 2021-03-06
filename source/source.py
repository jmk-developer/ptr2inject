#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

ptr2inject
by JMK

GitHub: https://github.com/jmk-developer/ptr2inject

'''

import wx
import shutil 
import os
import time
import math
import json

import modmanager

CurrentImage        = None
CurrentModFile      = None

CurrentImagePackage = None
CurrentModPackage   = None

ImageReady          = False
ModFileReady        = False

temp_directory      = None
temp_directory_name = ".temporary"
temp_directory_path = "\\" + temp_directory_name + "\\"
temp_directory_fullpath = os.getcwd() + temp_directory_path

if not os.path.isdir(temp_directory_fullpath):
    os.makedirs(temp_directory_fullpath)

modmanager.set_temporary_directory(temp_directory_fullpath)


def check_start_enabled(thisobject):
    print("Image Ready: " + str(ImageReady))
    print("ModFile Ready: " + str(ModFileReady))
    
    startbutton = thisobject.GetParent().Start
    if ImageReady == True and ModFileReady == True:
        startbutton.Enable()
    else:
        startbutton.Disable()

def not_yet_implemented(self):
    mod_data_dialog = wx.MessageDialog(self,
                                       "This feature is not yet implemented.",
                                       "Info",
                                       wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
    mod_data_dialog.ShowModal()
    mod_data_dialog.Destroy()

def show_package_data(self, mod_package):
    mod_data_dialog = wx.MessageDialog(self,
                                       "Mod Name: " + mod_package['mod_data_json']['name'] +
                                       "\nMod Description: " + mod_package['mod_data_json']['description'] +
                                       "\nMod Version: " + str(mod_package['mod_data_json']['version']),

                                       "Mod Info",
                                       wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
    mod_data_dialog.ShowModal()
    mod_data_dialog.Destroy()

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

        item = wxglade_tmp_menu.Append(wx.ID_ANY, "View ISO Info", "View an ISO file's info.")
        self.Bind(wx.EVT_MENU, self.view_iso_info, id=item.GetId())

        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Clear Temporary Files", "Clear all temporary files.")
        self.Bind(wx.EVT_MENU, self.clear_temporary_files, id=item.GetId())

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
        self.Start.Disable()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("ptr2inject")
        self.ChooseImage.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.ChooseImage.SetToolTip("This button chooses your Parappa The Rapper 2 ISO image.")
        self.ChooseFile.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.ChooseFile.SetToolTip("This button selects the .p2m file you want to inject.")
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
        not_yet_implemented(self)

    def view_mod_info(self, event):  # wxGlade: MyFrame.<event_handler>
        if ModFileReady == False:
            view_mod_error_dialog = wx.MessageDialog(self,
                                                        "Please select a mod file before using this option.",
                                                        "Info",
                                                        wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
            view_mod_error_dialog.ShowModal()
            view_mod_error_dialog.Destroy()
        else:
            show_package_data(self, CurrentModPackage)

    def view_iso_info(self, event):
        not_yet_implemented(self)
        '''
        if ImageReady == False:
            view_iso_error_dialog = wx.MessageDialog(self,
                                                     "Please select an ISO file before using this option.",
                                                     "Info",
                                                     wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
            view_iso_error_dialog.ShowModal()
            view_iso_error_dialog.Destroy()
        else:
            show_image_data(self, CurrentModPackage)
        '''

    def clear_temporary_files(self, event):
        begin_time = time.perf_counter()
        modmanager.clear_temporary_directory()
        end_time = time.perf_counter()
        clear_temporary_files_dialog = wx.MessageDialog(self,
                                           "Finished in " + str(math.ceil(end_time - begin_time)) +
                                           " seconds. Thank you!",
                                           "Done",
                                           wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
        clear_temporary_files_dialog.ShowModal()
        clear_temporary_files_dialog.Destroy()


    def about_menu(self, event):  # wxGlade: MyFrame.<event_handler>
        not_yet_implemented(self)

    def ignore_mod_region(self, event):  # wxGlade: MyFrame.<event_handler>
        not_yet_implemented(self)

    def choose_image_event(self, event):  # wxGlade: MyFrame.<event_handler>
        global CurrentImage
        global ImageReady
        
        iso_dialog = wx.FileDialog(self, "Open", "", "", "PS2 ISO images (*.iso)|*.iso", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        iso_dialog.ShowModal()
        CurrentImage = iso_dialog.GetPath()
        if not CurrentImage or CurrentImage == "":
            CurrentImage = None
            return
        myobject = event.GetEventObject()
        myobject.Disable()
        myobject.SetLabel("Completed")
        ImageReady = True
        check_start_enabled(myobject)

    def choose_file_event(self, event):  # wxGlade: MyFrame.<event_handler>
        global CurrentModFile
        global CurrentModPackage
        global ModFileReady
        
        file_dialog = wx.FileDialog(self, "Open", "", "", "PTR2 mod files (*.p2m)|*.p2m", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        file_dialog.ShowModal()
        CurrentModFile = file_dialog.GetPath()

        if not CurrentModFile or CurrentModFile == "":
            CurrentModFile = None
            return
        CurrentModPackage = modmanager.unpackage_mod_file(CurrentModFile, "ptr2mod")

        myobject = event.GetEventObject()
        myobject.Disable()
        myobject.SetLabel("Completed")
        ModFileReady = True
        check_start_enabled(myobject)

    def start_event(self, event):  # wxGlade: MyFrame.<event_handler>
        global CurrentModFile
        global CurrentModPackage
        global CurrentImage

        start_button = event.GetEventObject()
        start_button.Disable()
        start_button.SetLabel("Starting...")
        wx.BeginBusyCursor()
        show_package_data(self, CurrentModPackage)
        begin_time = time.perf_counter()
        start_button.SetLabel("Cleaning up...")
        modmanager.clear_temporary_directory()

        start_button.SetLabel("Extracting ISO...")
        unpackaged_iso = modmanager.unpackage_iso(CurrentImage, "ptr2iso")
        start_button.SetLabel("Moving files...")
        start_button.SetLabel("Patching ISO...")
        modmanager.package_iso(unpackaged_iso, CurrentImage)

        end_time = time.perf_counter()
        wx.EndBusyCursor()
        finished_dialog = wx.MessageDialog(self,
                                            "Finished in " + str(math.ceil(end_time - begin_time)) +
                                            " seconds. Thank you!",
                                            "Done",
                                            wx.OK | wx.STAY_ON_TOP | wx.CENTRE)
        finished_dialog.ShowModal()
        finished_dialog.Destroy()
# end of class MyFrame

class AboutDialog(wx.Dialog):
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
