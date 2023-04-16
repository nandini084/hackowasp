# Create a dictionary with state/union territory names as keys and their respective food delicacies as values
,
#1
indian_food = {
 "Andhra Pradesh": ["Biryani", "Mirchi Bajji", "Gongura Pickle"],
 "Arunachal Pradesh": ["Momos", "Thukpa", "Bamboo Shoot Fry"],
 "Assam": ["Masor Tenga", "Khaar", "Pitha","Papaya Khar"],
 "Andaman & Nicobar":["Fish Curry","Macher Jhol","Chilly Curry","Grilled Lobsters"],
 "Bihar": ["Litti Chokha", "Sattu Paratha", "Chana Ghugni"],
 "Chhattisgarh": ["Poha", "Chila", "Bafauri"],
 "Delhi":["Chole Bhature","Butter Chicken","Lassi","Chaat","Nihari"],
 "Goa": ["Fish Curry", "Vindaloo", "Sorpotel"],
 "Gujarat": ["Dhokla", "Khandvi", "Undhiyu"],
 "Haryana": ["Kachri ki Sabzi", "Kadhi Pakora", "Bajra Khichdi"],
 "Himachal Pradesh": ["Siddu", "Thenthuk", "Bhey","Dham"],
 "Jammu & Kashmir": ["Rogan Josh","Aloo Dum","Kashmiri Rajma","Phirni"],
 "Jharkhand": ["Dhuska", "Chilka Roti", "Pittha"],
 "Karnataka": ["Bisi Bele Bath", "Mysore Masala Dosa", "Ragi Mudde"],
 "Kerala": ["Appam", "Puttu", "Fish Molly"],
 "Ladakh" :["Butter Tea","Chang","Thukpa","Skyu","Chutagi"],
 "Lakshadweep":["Mus Kavaab","Batla Appam","Maas Podichathu","Fish Fry"],
 "Madhya Pradesh": ["Poha Jalebi", "Bhutte Ka Kees", "Dal Bafla"],
 "Maharashtra": ["Vada Pav", "Misal Pav", "Pav Bhaji"],
 "Manipur": ["Iromba", "Singju", "Chak-hao kheer","Kangshoi"],
 "Meghalaya": ["Jadoh", "Doh Khlieh", "Tung-rymbai"],
 "Mizoram": ["Bai", "Zu", "Vawksa Rep","Misa Maach Poora"],
 "Nagaland": ["Axone", "Smoked Pork Curry", "Bamboo Shoot Fry"],
 "Odisha": ["Dalma", "Chhena Poda", "Rasagola"],
 "Punjab": ["Sarson Da Saag", "Makki Ki Roti", "Butter Chicken"],
 "Pondicherry":["Mutton Rolls","Quiche","Spinach Crepe","Idli Sambhar","Bondas"],
 "Rajasthan": ["Dal Baati Churma", "Ghevar", "Laal Maas"],
 "Sikkim": ["Gundruk", "Sael Roti", "Thenthuk"],
 "Tamil Nadu": ["Idli", "Dosa", "Pongal"],
 "Telangana": ["Hyderabadi Biryani", "Mirchi ka Salan", "Khubani ka Meetha"],
 "Tripura": ["Bhangui", "Muya Awandru", "Panch Phoron Tarkari","Chakhwi"],
 "Uttar Pradesh": ["Tunde ke Kebab", "Galouti Kebab", "Aloo Tikki"],
 "Uttarakhand": ["Kafuli", "Chainsoo", "Bal Mithai"],
 "West Bengal": ["Rosogolla", "Mishti Doi", "Shukto","Kosha Mangsho"]
}

# Take input from the user
state = input("Enter an Indian state or union territory: ")

# Check if the input state is present in the dictionary
if state in indian_food:
 print("Some popular delicacies of", state, "are:")
 for delicacy in indian_food[state]:
 print("- " + delicacy)
else:
 print("Sorry, we do not have information about the delicacies of that state.")



# Create a dictionary with Indian state names as keys and their respective famous tourist spots as values
indian_tourism = {
 "Andhra Pradesh": ["Tirupati", "Visakhapatnam", "Amaravati"],
 "Andaman & Nicobar":["Port Blair","Radhanagar Beach","Cellular Jail","Ross Island","Elephant Beach","Chidiya tapu"],
 "Arunachal Pradesh": ["Tawang", "Ziro", "Bomdila"],
 "Assam": ["Kaziranga National Park", "Manas National Park", "Sualkuchi"],
 "Bihar": ["Bodh Gaya", "Nalanda", "Rajgir"],
 "Chhattisgarh": ["Bastar", "Chitrakote Falls", "Sirpur"],
 "Delhi":["Red fort","India Gate","Agrasen Ki Baori","Lotus Temple","Qutub Minar","Akshardham"],
 "Goa": ["Baga Beach", "Calangute Beach", "Dudhsagar Falls"],
 "Gujarat": ["Somnath Temple", "Rann of Kutch", "Sabarmati Ashram"],
 "Haryana": ["Kurukshetra", "Sultanpur National Park", "Pinjore Gardens"],
 "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala"],
 "Jammu & Kashmir":["Gulmarg","Pahalgam","Vaishno Devi","Patnitop","Sonmarg"],
 "Jharkhand": ["Hazaribagh National Park", "Jonha Falls", "Netarhat"],
 "Karnataka": ["Bangalore", "Mysore", "Hampi"],
 "Kerala": ["Munnar", "Alleppey", "Kochi"],
 "Ladakh":["Pangong Lake","Khardung La","Zanskar Valley","Magnetic Hill"],
 "Madhya Pradesh": ["Khajuraho", "Sanchi", "Bhopal"],
 "Maharashtra": ["Mumbai", "Pune", "Ajanta and Ellora Caves"],
 "Manipur": ["Loktak Lake", "Imphal", "Keibul Lamjao National Park"],
 "Meghalaya": ["Shillong", "Cherrapunji", "Dawki"],
 "Mizoram": ["Aizawl", "Phawngpui", "Durtlang Hills"],
 "Nagaland": ["Kohima", "Dimapur", "Dzukou Valley"],
 "Odisha": ["Puri", "Bhubaneswar", "Konark Sun Temple"],
 "Punjab": ["Golden Temple", "Jallianwala Bagh", "Wagah Border"],
 "Rajasthan": ["Jaipur", "Udaipur", "Jaisalmer"],
 "Sikkim": ["Gangtok", "Tsomgo Lake", "Nathu La"],
 "Tamil Nadu": ["Chennai", "Madurai", "Mahabalipuram"],
 "Telangana": ["Hyderabad", "Warangal", "Charminar"],
 "Tripura": ["Agartala", "Unakoti", "Ujjayanta Palace"],
 "Uttar Pradesh": ["Taj Mahal", "Varanasi", "Lucknow"],
 "Uttarakhand": ["Mussoorie", "Nainital", "Haridwar"],
 "West Bengal": ["Kolkata", "Darjeeling", "Sunderbans National Park"]
}

# Loop through the dictionary and print the state and its famous tourist spots
for state, tourist_spots in indian_tourism.items():
 print(state + ":")
 for spot in tourist_spots:
 print("- " + spot)
 print() # Add an extra line for spacing
#2 (itinerary generator)
  import pandas as pd

# Read the tourist spots dataset into a Pandas dataframe
df = pd.read_csv("tourist_spots.csv")

# Get a list of all the states in the dataset
states = df["State"].unique()

# Ask the user which state they want to visit
while True:
    state = input("Which state do you want to visit? (choose from " + ", ".join(states) + ") ")
    if state in states:
        break
    else:
        print("Invalid state, please try again.")

# Ask the user how many days they have for the trip
while True:
    days = input("How many days do you have for the trip? ")
    if days.isdigit() and int(days) > 0:
        break
    else:
        print("Invalid number of days, please try again.")

# Get all the tourist spots in the chosen state
spots_in_state = df[df["State"] == state]["Tourist Spot"].tolist()

# Shuffle the list of spots to randomize the itinerary
import random
random.shuffle(spots_in_state)

# Calculate how many spots to visit each day, rounding up if necessary
spots_per_day = (len(spots_in_state) + int(days) - 1) // int(days)

# Create an itinerary for each day of the trip
itinerary = []
for i in range(int(days)):
    start = i * spots_per_day
    end = min((i + 1) * spots_per_day, len(spots_in_state))
    day_spots = spots_in_state[start:end]
    itinerary.append(f"Day {i+1}: " + ", ".join(day_spots))

# Print the itinerary
print(f"Here's your {days}-day itinerary for {state}:")
print("\n".join(itinerary))

#3 (API integration for google maps)
html:
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>

<div id="map"></div>

javascript:
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: YOUR_LATITUDE, lng: YOUR_LONGITUDE },
    zoom: ZOOM_LEVEL,
  });
}

#to add markers:
const marker = new google.maps.Marker({
  position: { lat: MARKER_LATITUDE, lng: MARKER_LONGITUDE },
  map: map,
  title: "Marker Title",
});

#to add an info window:
const infowindow = new google.maps.InfoWindow({
  content: "Info window content",
});

marker.addListener("click", () => {
  infowindow.open(map, marker);
});

#recommendation of places
import pandas as pd

# Read the dataset into a Pandas dataframe
df = pd.read_csv("C:\\Users\\nandinir\\Downloads\\City.csv")

# Count the number of occurrences of each tourist spot
spot_counts = df["City"].value_counts()

# Choose the most popular spot
most_popular_spot = spot_counts.index[0]
sec_most_popular_spot = spot_counts.index[1]

# Print the most popular spot
print(f"Most popular spot is {most_popular_spot}.")
print(f"Second best spot according to its popularity is {sec_most_popular_spot}.")
