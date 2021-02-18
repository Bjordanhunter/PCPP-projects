import tkinter as tk

"""each tuple in 'phases' is a pattern for all the lights, each true or false is an individual light.
More patterns and lights can be added, right now it's 6 patterns of UP TO 5 lights.
"""
phases = ((True,  False, False, False,True),
          (True,  True,  False, True, False),
          (False, False, True , False,True),
          (False, True,  False, True, False),
          (False, False, False, False,True),
          (True,  True,  True , True, False))

phaseI=0
def next_phase():
    """cycles through each phase (pattern of lights)."""
    global phaseI
    phase = phases[phaseI]
    offColour = "grey"

    for i in range(len(phase)):
        try:
            light = lights[i]
        except IndexError:
            print(f"Lights index error: not enough lights for on/off phases: {phaseI}:{i}")
            break

        if phase[i]:
            canvas.itemconfig(light[0], fill=light[1])
        else:
            canvas.itemconfig(light[0], fill=offColour)

    phaseI = (phaseI+1) % len(phases)

lights = []
def make_lights(numOfLights:int, colours:list):
    """makes specified number of lights on canvas with each default colour supplied by the colours list."""
    global lights
    canvas.config(height=numOfLights*200+10)
    for i in range(numOfLights):
        lights.append((canvas.create_oval(10,(i*200)+10, 200,(i*200)+200, width=4, outline="black"),colours[i]))


#gui setup and layout
window = tk.Tk()
window.title("Traffic Lights")
canvas = tk.Canvas(window, width=210, height=810, bg="gray30")

# makes 3 lights with default colours listed **will print ignorable error as phases are five items long** you can set it to UP TO 5 without also changing ‘phases’ but that doesn't fit my screen.
make_lights(3,["red","yellow","green","blue","pink"])
next_phase()

canvas.grid(row=1)

nextButton = tk.Button(window, text="Next", command=next_phase)
nextButton.grid(row=2)
quitButton = tk.Button(window, text="Quit", command=window.destroy)
quitButton.grid(row=3)

window.mainloop()
