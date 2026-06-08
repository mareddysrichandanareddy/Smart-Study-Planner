def generate_schedule(subject, hours):
    try:
        hours = int(hours)

        schedule = f"\nStudy Schedule\n"
        schedule += f"\nSubject: {subject}\n"
        schedule += f"Study Time: {hours} Hours\n"

        for i in range(1, hours + 1):
            schedule += f"Hour {i}: Study {subject}\n"

        return schedule

    except:
        return "Please enter valid study hours."
