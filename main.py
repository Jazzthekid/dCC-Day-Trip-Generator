import random


destinations = ['New York City', 'San Antonio', 'Atlanta', 'Cancun', 'San Jaun', 'Tokyo', 'Detroit', 'San Fransisco', 'Paris', 'Napal', 'Las Vegas', 'New Orleans', 'Chicago' ]
restaurants = ['Katz Deli', 'The Barbecue Station', 'Bones Restaurant', 'Vagon Santurce', 'Shake Shack', 'Five Guys', ' Chipolte','Tempura Fukamachi' 'A Casa de Porco', 'Old Nola Cookery', 'PF Changs']
transportation = ['Car', 'Plane', 'Train', 'Bike', 'Klingon Transporter','Hover Bike', 'Millenium Falcon','DeLorean', 'Tardis', 'Dragon', 'The Enterprise', 'Stargate' ]
entertainment = ['Mos Eisley Cantina', 'Comedy Club', 'Comic Convention', 'Concert', 'Circus', 'Science Fair', 'Drive-In Movie', 'Bowling', 'Roller Skating', 'Axe Throwing', 'Escape Room','Paintball']





def item_picker(list):
    random_item = random.choice(list)
    return random_item

def destination_picker():
    user_picked = False
    while user_picked == False:
        random_item = item_picker(destinations)
        print(f'Destination: {random_item}')
        user_picked = True
        return random_item

def restaurant_picker():
    user_picked = False
    while user_picked == False:
        random_item = item_picker(restaurants)
        print(f'Restaurant: {random_item}')
        user_picked = True
        return random_item
def transport_picker():
    user_picked = False
    while user_picked == False:
        random_item =item_picker(transportation)
        print(f'Transportation: {random_item}')
        user_picked = True
        return random_item

def entertainment_picker():
    user_picked = False
    while user_picked == False:
        random_item = item_picker(entertainment)
        print(f'Entertainment: {random_item}')
        user_picked = True
        return random_item


def day_trip_selections():
    all_decisions = destination_picker(), transport_picker(),restaurant_picker(),entertainment_picker()
   
    return all_decisions




def accepting_day_trip():
    user_picked = False
    while user_picked == False:
        random_selections = day_trip_selections()
        print("")
        print(f'We have selected these choices for your day trip. Would you like to finalize your trip?' )
        print("")
        user_choice = input('Type "Yes" to accept this trip or "No" to decline ')
    
        if user_choice == "Yes":
             print("")
             print(f'Great! Here is your day trip itinerary. {random_selections}')
             user_picked = True
             
        elif user_choice == "No":
            print("")
            print(f'Im Sorry, How about these selections?')
            print("")
        else:
            print("Invalid Input")
            user_picked = True

accepting_day_trip()