import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import math

def my_sign(x):
  return (x > 0) - (x < 0)

# Function to update the graph
def update_graph(E, psi_initial):
    psi = psi_initial[:]
    potential = []
    x = []

    for i in range(0, 4001):
        x_value = (i) * deltax
        x.append(x_value)
        potential.append(2.5*my_sign(i*deltax - 2) + 2.5)

    for i in range(2, 4001):
        psi.append((2.0 * psi[i-1] - psi[i-2] + 2.0 * deltax * deltax * psi[i-1] * (potential[i-1] - E))) ## Pg 178 from packet

    ax.clear()
    ax.plot(x, psi, label='Wavefunction ψ(x)')
    ax.plot(x, potential, label='Potential V(x)', linestyle='--')
    ax.set_xlabel('Position x')
    ax.set_ylabel('ψ(x) and U(x)')
    ax.set_title('Wavefunction and Potential for a Half-Infinite Well')
    plt.suptitle('*Note, this is held together with tape at best, only applies to odd functions', fontsize =10)
    ax.legend()
    ax.grid(True)
    canvas.draw()

# Function to handle button clicks for updating E
def adjust_E(delta):
    global E
    E = round(E + delta, 4)
    e_label.config(text=f'E = {E}')
    update_graph(E, psi)
    
#def adjust_E(delta):
   # global E
   # target_E = E + delta
    #step_size = delta / 10  # Number of steps for smooth transition
    #update_E_step_by_step(target_E, step_size)

#def update_E_step_by_step(target, step):
    #global E
    #if (step > 0 and E < target) or (step < 0 and E > target):
       # E = round(E + step, 3)
       # e_label.config(text=f'E = {E}')
       # update_graph(E, psi)
       #root.after(1, update_E_step_by_step, target, step)  # Update every 5 ms

# Function to handle radio button selection for function type
def set_function_type():
    global psi
    psi = [0, 1] if function_type.get() == "Even" else [1, 1]
    update_graph(E, psi)

# Parameters
k = 1
deltax = 0.001
E = 0.5
psi = [0, 1]

# Setting up the main Tkinter window
root = Tk()
root.title("Quantum Harmonic Oscillator Simulator")

# Creating a frame for the plot
frame = Frame(root)
frame.pack(fill=BOTH, expand=1)

# Creating a matplotlib figure and axis
fig, ax = plt.subplots(figsize=(10,6))
canvas = FigureCanvasTkAgg(fig, master=frame)
widget = canvas.get_tk_widget()
widget.pack(fill=BOTH, expand=1)

# Creating the GUI elements for adjusting E
control_frame = Frame(root)
control_frame.pack()

e_label = Label(control_frame, text=f'E = {E}', font=('Arial', 14))
e_label.pack(side=LEFT, padx=10)

# Arrow buttons
decimal_places = [1, 0.1, 0.01, 0.001, 0.0001]
for delta in decimal_places:
    arrow_frame = Frame(control_frame)
    arrow_frame.pack(side=LEFT)
    Button(arrow_frame, text='↑', command=lambda d=delta: adjust_E(d)).pack(side=TOP)
    Button(arrow_frame, text='↓', command=lambda d=delta: adjust_E(-d)).pack(side=BOTTOM)

# Radio buttons for function type selection
function_frame = Frame(root)
function_frame.pack()
function_type = StringVar(value="Even")
Label(function_frame, text="Function Type:").pack(side=LEFT)
Radiobutton(function_frame, text="Even", variable=function_type, value="Even", command=set_function_type).pack(side=LEFT)
Radiobutton(function_frame, text="Odd", variable=function_type, value="Odd", command=set_function_type).pack(side=LEFT)

# Listbox for valid energy configurations
config_frame = Frame(root)
config_frame.pack()
Label(config_frame, text="Valid Energy Configurations:").pack()
listbox = Listbox(config_frame)
listbox.pack()
valid_configs = ["E = 0.4541, n = 0 odd", "E = 1.765, n = 1 even", "E = 5.5, n = 2 odd"]
for item in valid_configs:
    listbox.insert(END, item)

# Initial graph plot
update_graph(E, psi)

# Start the Tkinter event loop
root.mainloop()