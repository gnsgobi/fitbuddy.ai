def generate_workout(user_input):
    return {
        "type": "workout",
        "message": f"Workout plan for: {user_input}"
    }


def generate_nutrition_tip(user_input):
    return {
        "type": "nutrition",
        "message": f"Nutrition plan for: {user_input}"      
    }
def update_workout_plan(user_input, current_plan, feedback):
    return 