from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample data for locations, activities, and interests
activities = {
    "New York": {
        "sightseeing": ["Statue of Liberty", "Central Park", "Times Square"],
        "art": ["Metropolitan Museum of Art", "Museum of Modern Art"],
        "food": ["Katz's Delicatessen", "Eataly", "Joe's Pizza"],
        "shopping": ["Fifth Avenue", "Brooklyn Flea Market"],
        "outdoors": ["High Line Park", "Hudson River Park"]
    },
    "Paris": {
        "sightseeing": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "art": ["Musée d'Orsay", "Centre Pompidou"],
        "food": ["Le Jules Verne", "Bistrot Paul Bert", "Pierre Hermé"],
        "shopping": ["Champs-Élysées", "Le Marais"],
        "outdoors": ["Jardin des Tuileries", "Luxembourg Gardens"]
    }
}

def generate_itinerary(location, days, age, interests):
    if location not in activities:
        return f"Sorry, we don't have data for {location} yet."

    daily_itinerary = []
    for day in range(1, days + 1):
        daily_activities = []
        for interest in interests:
            if interest in activities[location]:
                activity = random.choice(activities[location][interest])
                daily_activities.append(activity)
        daily_itinerary.append({"day": day, "activities": daily_activities})
    
    return daily_itinerary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    location = request.form['location']
    days = int(request.form['days'])
    age = int(request.form['age'])
    interests = request.form.getlist('interests')
    
    itinerary = generate_itinerary(location, days, age, interests)
    return render_template('itinerary.html', itinerary=itinerary)

if __name__ == '__main__':
    app.run(debug=True)
