import turtle
import pandas as pd

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# Load data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Writer turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Function to find the nearest state
def find_nearest_state(x, y):
    """Finds the closest state based on click coordinates."""
    data["distance"] = abs(data["x"] - x) + abs(data["y"] - y)  # Manhattan Distance
    nearest_state = data.loc[data["distance"].idxmin()]
    return nearest_state if nearest_state["distance"] < 20 else None  # Allow small tolerance

# Function to handle mouse clicks
def on_click(x, y):
    nearest_state = find_nearest_state(x, y)
    
    if nearest_state is not None and nearest_state["state"] not in guessed_states:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)}/50 States Correct",
            prompt="What's the state name? Type 'Exit' to quit."
        )

        if answer_state is None or answer_state.title() == "Exit":
            save_missing_states()
            screen.bye()

        elif answer_state.title() == nearest_state["state"]:
            guessed_states.append(nearest_state["state"])
            writer.goto(nearest_state["x"], nearest_state["y"])
            writer.write(nearest_state["state"], align="center", font=("Arial", 10, "bold"))

# Function to save missing states
def save_missing_states():
    missing_states = [state for state in all_states if state not in guessed_states]
    pd.DataFrame(missing_states).to_csv("states_to_learn.csv")

# Detect mouse clicks
turtle.onscreenclick(on_click)

turtle.mainloop()
