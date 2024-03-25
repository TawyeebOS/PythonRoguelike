class Map:
    def __init__(self):
        """
        creates the home room
        """
        home_room = Room("Start")

    def display_map(self):
        pass




class Room:
    def __init__(self, room_type):
        """
        Assumes room_type is an integer
        """
        self.room_type = room_type
        self.adjecent_rooms = {}

    def add_adjacent_room(self, room, pos):
        """
        Assumes room is a Room object and pos is a string representing a 
            direction
        Adds the room to self.adjacent rooms
        """
        self.adjecent_rooms[pos] = room
    
S