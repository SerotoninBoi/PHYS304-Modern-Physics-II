import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

# Function to update the graph
def update_graph(E, psi_initial):
    psi = psi_initial[:]
    potential = []
    x = []

    for i in range(0, 4001):
        x_value = (i - 2000) * deltax
        x.append(x_value)
        potential.append(0.5 * k * (x_value * x_value))

    for i in range(2, 4001):
        psi.append((2.0 * psi[i-1] - psi[i-2] + 2.0 * deltax * deltax * psi[i-1] * (potential[i-1] - E))) ## Pg 178 from packet

    ax.clear()
    ax.plot(x, psi, label='Wavefunction ψ(x)')
    ax.plot(x, potential, label='Potential V(x)', linestyle='--')
    ax.set_xlabel('Position x')
    ax.set_ylabel('ψ(x) and V(x)')
    ax.set_title('Wavefunction and Potential for a Quantum Harmonic Oscillator')
    ax.legend()
    ax.grid(True)
    canvas.draw()

# Function to handle button clicks for updating E
def adjust_E(delta):
    global E
    E = round(E + delta, 3)
    e_label.config(text=f'E = {E}')
    update_graph(E, psi)

# Function to handle radio button selection for function type
def set_function_type():
    global psi
    psi = [0, 1] if function_type.get() == "Even" else [1, 2]
    update_graph(E, psi)

# Parameters
k = 1
deltax = 0.001
E = 1.765
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
decimal_places = [0.1, 0.01, 0.001]
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