from agents.task_agent import create_task
from agents.calendar_agent import schedule_event
from agents.notes_agent import save_note

def handle_request(user_input):
    text = user_input.lower()
    response = []

    if "task" in text:
        response.append(create_task(user_input))

    if "schedule" in text or "meeting" in text:
        response.append(schedule_event(user_input))

    if "note" in text:
        response.append(save_note(user_input))

    if not response:
        return "❌ Could not understand request"

    return "\n".join(response)