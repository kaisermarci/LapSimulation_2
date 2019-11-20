import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from shutil import copyfile
import shutil
from PIL import Image,ImageTk
from parameterStudy import ParamStudy as parameter_study
import os








class menu():

    next_step = "main_menu"
    last_step = "main_menu"
    exit = False
    elements= []
    red_rgb ='#%02x%02x%02x' % (215 ,59 ,60)
    loaded_cars = ["temp"]
    loaded_tracks = ["temp"]
    parameters = ['C_F','C_R','m','CoG_X','mu','alpha','CoP_X','C_la','rho','gearRatio','tireRadius','fr','Lift2Drag']
    tracks = ['Endurance_FSA15_Curvature', 'AutoX_FSA15_Curvature', 'Skidpad', 'Acceleration', 'Efficiency_FSA15_Curvature']


    window_height = 800
    window_width = 1200

    def __init__(self,icon_path,top_background_path,bottom_background_path):

        self.gui_window = tk.Tk()
        self.gui_window.resizable(width=False,height=False)
        self.gui_window.title("LapSim")
        self.gui_window.iconbitmap(icon_path)
        self.gui_canvas = tk.Canvas(self.gui_window,width=self.window_width,height=self.window_height,bg="white")
        self.validate_input_value = self.gui_canvas.register(self.validate_input)


        self.import_top_background = Image.open(top_background_path)
        temp=self.import_top_background.resize((self.window_width+10,self.window_height-(self.window_height-120)),Image.ANTIALIAS)
        top_background=ImageTk.PhotoImage(temp)
        self.gui_canvas.create_image(self.window_width/2,0,image=top_background,anchor="n")

        self.import_bottom_background = Image.open(bottom_background_path)
        temp=self.import_bottom_background.resize((self.window_width+10,self.window_height-(self.window_height-120)),Image.ANTIALIAS)
        bottom_background= ImageTk.PhotoImage(temp)
        self.gui_canvas.create_image(self.window_width/2,self.window_height,image=bottom_background,anchor="s")

        self.head_text_id = self.gui_canvas.create_text(self.window_width/2, 115, text="Lap Simulation", font="Arial 40 bold", fill="black", anchor="center")


        self.last_step = "main_menu"
        self.load_car_modells()
        self.gui_engine()

        self.gui_canvas.pack(fill="both", expand=False)
        self.gui_window.mainloop()
    def gui_engine(self):
        self.clear_window()

        def event_button_back():
            self.next_step=self.last_step
            self.last_step = "main_menu"
            self.clear_window()
            print(self.next_step)
            self.gui_engine()

        if (self.next_step != "main_menu"):
            print("back button da")
            button_next = tk.Button(self.gui_canvas, text="Back", command=event_button_back, font="Arial 14 bold", bd=1,background=self.red_rgb, fg="Black", width=10,height=1)
            self.elements.append(self.gui_canvas.create_window(self.window_width - (self.window_width - 114),self.window_height -22, window=button_next,anchor="center"))



        if (self.next_step == "main_menu"):
            self.main_menu()

        if (self.next_step == "simulation_menu"):
            self.study_menu()

        if (self.next_step == "import_car"):
           self.import_car_menu()

        if (self.next_step == "import_track"):
            self.import_track_menu()

        if (self.next_step == "parameter_study"):
            self.parameter_study_menu()

        if (self.next_step == "single_simulation"):
            self.single_simulation()

        if (self.next_step == "comparison_simulation"):
             self.comparison_study_menu()

        if (self.next_step == "generate_plot"):
            self.generate_plot_menu()

        if (self.next_step == " load_study"):
            self.load_study_menu()

        if (self.next_step == "generate_car"):
            self.generate_car_menu()

        if (self.next_step == "exit"):
            self.gui_window.destroy()
            return

    def main_menu(self):

        def start_simulation():
            self.next_step = "simulation_menu"
            self.last_step = "main_menu"
            self.gui_engine()


        button_simulation = tk.Button(self.gui_canvas, text="Simulation", command=start_simulation, font="Arial 24 bold",bd=1, background=self.red_rgb, fg="black", width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2, 280, window=button_simulation, anchor="center"))

        def start_import_car():
            self.next_step = "import_car"
            self.last_step = "main_menu"
            self.gui_engine()


        button_import_car = tk.Button(self.gui_window, text="Import Car", command=start_import_car, font="Arial 24 bold",bd=1, background=self.red_rgb, fg="black", width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2, 400, window=button_import_car, anchor="center"))

        def start_create_car():
            self.next_step = "generate_car"
            self.last_step = "main_menu"
            self.gui_engine()

        button_create_car = tk.Button(self.gui_window,text="Create Car",command=start_create_car, font="Arial 24 bold",bd=1,background=self.red_rgb,fg="black",width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,520,window=button_create_car,anchor="center"))


        def start_create_track():
            self.next_step = "import_track"
            self.last_step = "main_menu"
            self.gui_engine()


        button_create_track = tk.Button(self.gui_window, text="Import Track", command=start_create_track,font="Arial 24 bold", bd=1, background=self.red_rgb, fg="black", width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2, 640, window=button_create_track, anchor="center"))








    def study_menu(self):


        def event_button_parameter():
            self.next_step="parameter_study"
            self.last_step = "simulation_menu"
            self.gui_engine()

        button_parameter = tk.Button(self.gui_window, text="Start Parameter Study",command=event_button_parameter,font="Arial 24 bold", bd=1, background=self.red_rgb,fg="black",width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,280,window=button_parameter,anchor="center"))

        def event_button_single():
            self.next_step = "single_simulation"
            self.last_step = "simulation_menu"
            self.gui_engine()

        button_single = tk.Button(self.gui_window, text="Start Single Simulation",command=event_button_single,font="Arial 24 bold",bd=1,background=self.red_rgb,fg="black",width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,380,window=button_single,anchor="center"))

        def event_button_compare():
            self.next_step = "comparison_simulation"
            self.last_step = "simulation_menu"
            self.gui_engine()

        button_compare = tk.Button(self.gui_window, text="Start Compare  Simulation",command=event_button_compare,font="Arial 24 bold",bd=1,background=self.red_rgb,fg="black",width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,480,window=button_compare,anchor="center"))

        def event_button_plot():
            self.next_step = "generate_plot"
            self.last_step = "simulation_menu"
            self.gui_engine()

        button_plot = tk.Button(self.gui_window, text="Generate Plots",command=event_button_plot,bd=1,background=self.red_rgb,font="Arial 24 bold",fg="black",width=30)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,580,window=button_plot,anchor="center"))


    def parameter_study_menu(self):
        self.load_car_modells()
        self.load_tracks()

        self.elements.append(self.gui_canvas.create_text(100,170,text="Simulationname",font="Arial 16 bold",anchor="w"))
        self.simulationname_selection = tk.StringVar()
        self.simulationname = tk.Entry(self.gui_canvas,textvariable=self.simulationname_selection,width="18",bd=2,font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(100,200,window=self.simulationname,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100,260,text="Car Model",font="Arial 16 bold",anchor="w"))
        self.car_type_combobox = ttk.Combobox(self.gui_window,values=self.loaded_car_modells,font="Arial 12 bold",state="readonly")
        self.car_type_combobox.set("Choose a Car Model")
        self.elements.append(self.gui_canvas.create_window(100,290,window=self.car_type_combobox,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100,350,text="Track",font="Arial 16 bold",anchor="w"))
        self. track_type_combobox = ttk.Combobox(self.gui_window,values=self.loaded_tracks,font="Arial 12 bold",state="readonly")
        self.track_type_combobox.set("Choose a Track")
        self.elements.append(self.gui_canvas.create_window(100,380,window=self.track_type_combobox,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100,440,text="Parameter",font="Arial 16 bold",anchor="w"))
        self.parameter_type_combobox = ttk.Combobox(self.gui_window,values=self.parameters, font="Arial 12 bold",state="readonly")
        self.parameter_type_combobox.set("Choose the Parameter")
        self.elements.append(self.gui_canvas.create_window(100,470,window=self.parameter_type_combobox,anchor="w"))


        self.start_value_selection = tk.StringVar()
        self.start_value = tk.Entry(self.gui_canvas,textvariable=self.start_value_selection,width="17",validate='key',validatecommand=(self.validate_input_value,'%P'),bd=2,font="Arial 14 italic")
        self.elements.append(self.gui_canvas.create_window(100,580,window=self.start_value,anchor="w"))
        self.elements.append(self.gui_canvas.create_text(100,550,text="Start Value",font="Arial 16 bold",anchor="w"))

        self.min_value_selection = tk.StringVar()
        self.min_value = tk.Entry(self.gui_canvas,textvariable=self.min_value_selection,width="17",validate="key",validatecommand=(self.validate_input_value,'%P'),bd=2,font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(340,580,window=self.min_value,anchor="w"))
        self.elements.append(self.gui_canvas.create_text(340,550,text="Min. Value",font="Arial 16 bold",anchor="w"))

        self.step_value_selection = tk.StringVar()
        self.step_value = tk.Entry(self.gui_canvas,textvariable=self.step_value_selection,width="17",validate="key",validatecommand=(self.validate_input_value,'%P'),bd=2,font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(580,580,window=self.step_value,anchor="w"))
        self.elements.append(self.gui_canvas.create_text(580,550,text="Step Width",font="Arial 16 bold", anchor="w"))

        self.max_value_selection = tk.StringVar()
        self.max_value = tk.Entry(self.gui_canvas,textvariable=self.max_value_selection,width="17",validate="key",validatecommand=(self.validate_input_value,'%P'),bd=2,font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(820,580,window=self.max_value,anchor="w"))
        self.elements.append(self.gui_canvas.create_text(820,550,text="Max. Value",font="Arial 16 bold", anchor="w"))

        def event_start_button():



            self.parameter_study = parameter_study('FSA', 2015, self.parameter_type_combobox.get(), int(self.step_value_selection.get()), int(self.min_value_selection.get()), int(self.max_value_selection.get()),self.car_type_combobox.get(),self.track_type_combobox.get(),self.simulationname_selection.get())
            self.parameter_study.SimulateParamStudy()
            self.next_step = "parameter_study"
            self.gui_engine()

        self.start_button = tk.Button(self.gui_window,text="Start Simulation",command=event_start_button,bd=1,background=self.red_rgb,font="Arial 14 bold",fg="black",width=15)
        self.elements.append(self.gui_canvas.create_window(820,650,window=self.start_button,anchor="w"))






    def comparison_study_menu(self):
        print("temp")

    def single_simulation(self):

        self.elements.append(self.gui_canvas.create_text(100, 170, text="Simulationname", font="Arial 16 bold", anchor="w"))
        self.simulationname_selection = tk.StringVar()
        self.simulationname = tk.Entry(self.gui_canvas, textvariable=self.simulationname_selection, width="18", bd=2,font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(100, 200, window=self.simulationname, anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100, 260, text="Car Model", font="Arial 16 bold", anchor="w"))
        self.car_type_combobox = ttk.Combobox(self.gui_window, values=self.loaded_cars, font="Arial 12 bold",state="readonly")
        self.car_type_combobox.set("Choose a Car Model")
        self.elements.append(self.gui_canvas.create_window(100, 290, window=self.car_type_combobox, anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100, 350, text="Track", font="Arial 16 bold", anchor="w"))
        self.track_type_combobox = ttk.Combobox(self.gui_window, values=self.loaded_tracks, font="Arial 12 bold",state="readonly")
        self.track_type_combobox.set("Choose a Track")
        self.elements.append(self.gui_canvas.create_window(100, 380, window=self.track_type_combobox, anchor="w"))

        self.elements.append(self.gui_canvas.create_text(100, 440, text="Parameter", font="Arial 16 bold", anchor="w"))
        self.parameter_type_combobox = ttk.Combobox(self.gui_window, values=self.parameters, font="Arial 12 bold",state="readonly")
        self.parameter_type_combobox.set("Choose the Parameter")
        self.elements.append(self.gui_canvas.create_window(100, 470, window=self.parameter_type_combobox, anchor="w"))

        def event_start_button():

            self.single_simulation_parameters = self.simulationname.get(),self.car_type_combobox.get(),self.track_type_combobox.get(),self.parameter_type_combobox
            self.gui_engine()

        self.start_button = tk.Button(self.gui_window,text="Start Simulation",command=event_start_button,bd=1,background=self.red_rgb,font="Arial 14 bold",fg="black",width=15)
        self.elements.append(self.gui_canvas.create_window(900,800,window=self.start_button,anchor="w"))


    def generate_plot_menu(self):
        print("temp")
    def load_study_menu(self):
        print("temp")

    def import_car_menu(self):
        self.file_path=""
        def event_browse_button():
            self.file_path = filedialog.askopenfilename()
            self.path_selection.set(str(self.file_path))



        browse_button = tk.Button(self.gui_canvas,text="...",command=event_browse_button,font="Arial 10 bold",bd=1,width=2,height=1,background="white")
        self.elements.append(self.gui_canvas.create_window(self.window_width/2+108,380,window=browse_button,anchor="center"))
        def event_import_button():

            print(self.file_path)
            shutil.copy(self.file_path,os.getcwd()+"/car_modells")

        import_button = tk.Button(self.gui_canvas,text="Import",command=event_import_button,font="Arial 16 bold",bd=1,width=15,background=self.red_rgb)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,420,window=import_button,anchor="center"))

        self.path_selection = tk.StringVar()
        self.path_entry = tk.Entry(self.gui_canvas, textvariable=self.path_selection, width="17", bd=2, font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(self.window_width/2, 380, window=self.path_entry, anchor="center"))
        self.elements.append(self.gui_canvas.create_text(self.window_width/2, 350, text="Choose the file Path", font="Arial 16 bold", anchor="center"))


    def import_track_menu(self):
        self.file_path=""
        def event_browse_button():
            self.file_path = filedialog.askopenfilename()
            self.path_selection.set(str(self.file_path))



        browse_button = tk.Button(self.gui_canvas,text="...",command=event_browse_button,font="Arial 10 bold",bd=1,width=2,height=1,background="white")
        self.elements.append(self.gui_canvas.create_window(self.window_width/2+108,380,window=browse_button,anchor="center"))
        def event_import_button():

            print(self.file_path)
            shutil.copy(self.file_path,os.getcwd()+"/tracks")

        import_button = tk.Button(self.gui_canvas,text="Import",command=event_import_button,font="Arial 16 bold",bd=1,width=15,background=self.red_rgb)
        self.elements.append(self.gui_canvas.create_window(self.window_width/2,420,window=import_button,anchor="center"))

        self.path_selection = tk.StringVar()
        self.path_entry = tk.Entry(self.gui_canvas, textvariable=self.path_selection, width="17", bd=2, font="Arial 14 italic ")
        self.elements.append(self.gui_canvas.create_window(self.window_width/2, 380, window=self.path_entry, anchor="center"))
        self.elements.append(self.gui_canvas.create_text(self.window_width/2, 350, text="Choose the file Path", font="Arial 16 bold", anchor="center"))

    def generate_car_menu(self):
        self.elements.append(self.gui_canvas.create_text(150,170,text="Oblique Stiffness:",font="Arial 16 bold",anchor="w"))
        self.C_F_selection = tk.StringVar()
        self.C_F_input = tk.Entry(self.gui_canvas, textvariable=self.C_F_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(150,200,window=self.C_F_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(150,270,text="C_R:",font="Arial 16 bold",anchor="w"))
        self.C_R_selection = tk.StringVar()
        self.C_R_input = tk.Entry(self.gui_canvas, textvariable=self.C_R_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(150,300,window=self.C_R_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(150,370,text="Mass:",font="Arial 16 bold",anchor="w"))
        self.m_selection = tk.StringVar()
        self.m_input = tk.Entry(self.gui_canvas, textvariable=self.m_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(150,400,window=self.m_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(150,470,text="Center of Gravity in X:",font="Arial 16 bold",anchor="w"))
        self.CoG_X_selection = tk.StringVar()
        self.CoG_X_input = tk.Entry(self.gui_canvas, textvariable=self.CoG_X_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(150,500,window=self.CoG_X_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(150,570,text="Tire Friction:",font="Arial 16 bold",anchor="w"))
        self.mu_selection = tk.StringVar()
        self.mu_input = tk.Entry(self.gui_canvas, textvariable=self.mu_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(150,600,window=self.mu_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(350,170,text="alpha:",font="Arial 16 bold",anchor="w"))
        self.alpha_selection = tk.StringVar()
        self.alpha_input = tk.Entry(self.gui_canvas, textvariable=self.alpha_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(350,200,window=self.alpha_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(350,270,text="CoP_X:",font="Arial 16 bold",anchor="w"))
        self.CoP_X_selection = tk.StringVar()
        self.CoP_X_input = tk.Entry(self.gui_canvas, textvariable=self.CoP_X_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(350,300,window=self.CoP_X_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(350,370,text="Downforce Coefficient:",font="Arial 16 bold",anchor="w"))
        self.C_la_selection = tk.StringVar()
        self.C_la_input = tk.Entry(self.gui_canvas, textvariable=self.C_la_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(350,400,window=self.C_la_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(350,570,text="Drive-Type:",font="Arial 16 bold",anchor="w"))
        self.drive_type_values = ["a","b"]
        self.drive_type_combobox = ttk.Combobox(self.gui_canvas, values=self.drive_type_values,font="Arial 14 italic",state="readonly")
        self.elements.append(self.gui_canvas.create_window(350,600,window=self.drive_type_combobox,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(550,170,text="Gear Ratio:",font="Arial 16 bold",anchor="w"))
        self.Gear_ratio_selection = tk.StringVar()
        self.Gear_ratio_input = tk.Entry(self.gui_canvas, textvariable=self.Gear_ratio_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(550,200,window=self.Gear_ratio_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(550,270,text="Tire Radius:",font="Arial 16 bold",anchor="w"))
        self.tire_radius_selection = tk.StringVar()
        self.tire_radius_input = tk.Entry(self.gui_canvas, textvariable=self.tire_radius_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(550,300,window=self.tire_radius_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(550,370,text="Rolling Resistance:",font="Arial 16 bold",anchor="w"))
        self.fr_selection = tk.StringVar()
        self.fr_input = tk.Entry(self.gui_canvas, textvariable=self.fr_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(550,400,window=self.fr_input,anchor="w"))

        self.elements.append(self.gui_canvas.create_text(550,470,text="Lift2Drag:",font="Arial 16 bold",anchor="w"))
        self.lift_2_drag_selection = tk.StringVar()
        self.lift_2_drag_input = tk.Entry(self.gui_canvas, textvariable=self.lift_2_drag_selection,width="10",font="Arial 14 italic",bd=2)
        self.elements.append(self.gui_canvas.create_window(550,500,window=self.lift_2_drag_input,anchor="w"))




    def clear_window(self):
        for a in range(len(self.elements)):
            self.gui_canvas.delete(self.elements[a])

    def validate_input(self,input):
        if input.isdigit() or input == "":
            return True
        else:
            return False

    def load_car_modells(self):
        self.loaded_car_modells = os.listdir(os.getcwd()+"/car_modells/")


    def load_tracks(self):
        self.loaded_tracks = os.listdir(os.getcwd()+"/tracks/")

