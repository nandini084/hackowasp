# Create a dictionary with state/union territory names as keys and their respective food delicacies as values
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
    print()  # Add an extra line for spacing
