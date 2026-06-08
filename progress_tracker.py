def save_progress(task):
    with open("progress.txt", "a") as file:
        file.write(task)
        file.write("\n----------------------\n")
