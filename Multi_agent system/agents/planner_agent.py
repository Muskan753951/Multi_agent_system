

def plan_steps(user_goal: str) -> list:
    """
    Naive planner that returns an ordered list of steps based on keywords.
    """
    goal = user_goal.lower()
    steps = []

    if "launch" in goal:
        steps.append("find_next_launch")
    if "weather" in goal:
        steps.append("check_weather")
    if "delay" in goal or "summarize" in goal:
        steps.append("summarize_risk")

    return steps
