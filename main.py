from tkinter import *
from planner import generate_schedule
from progress_tracker import save_progress

root = Tk()
root.title("Smart Study Planner")
root.geometry("600x500")

Label(root, text="Smart Study Planner",
      font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Subject Name").pack()
subject_entry = Entry(root, width=30)
subject_entry.pack()

Label(root, text="Study Hours").pack()
hours_entry = Entry(root, width=30)
hours_entry.pack()

schedule_box = Text(root, height=10, width=50)
schedule_box.pack(pady=10)

def create_schedule():
    subject = subject_entry.get()
    hours = hours_entry.get()

    result = generate_schedule(subject, hours)

    schedule_box.delete(1.0, END)
    schedule_box.insert(END, result)

def save_task():
    task = schedule_box.get(1.0, END)
    save_progress(task)

Button(root,
       text="Generate Schedule",
       command=create_schedule,
       bg="lightblue").pack(pady=5)

Button(root,
       text="Save Progress",
       command=save_task,
       bg="lightgreen").pack(pady=5)

root.mainloop()
