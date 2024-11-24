import random

class Room:
    """
    A class that defines a room and its inhabitants
    """

    DIRECTIONS = ("north", "east", "south", "west", "north-east", "north-west", "south-east", "south-west")
    ADJ_DIRECTIONS = ("north", "east", "south", "west")

    def __init__(self, name: str, description: str):
        """
        Assumes name and description are strings
        Creates a new Room object
        """

        self.name = name
        self.description = description
        
        # a dictionary containing a pointer to 8 adjacent rooms, initially empty
        self.adjacent_rooms = {
                "north": None,
                "east": None,
                "south": None,
                "west": None,
                "north-east": None,
                "north-west": None,
                "south-east": None,
                "south-west": None
                }

        # Holds any entities that may be inside the room
        inhabitants: Entity = None

        # True if the current room has been searched
        searched = False

    @staticmethod
    def get_random_direction():
        """ returns a tuple of the exit directions for a room """
        return random.choice(Room.ADJ_DIRECTIONS)
    
    @staticmethod
    def get_opposite_direction(direction: str):
        """ 
        Assumes direction is a string representing a cardinal direction
        Returns a string represnting the opposite cardinal direction 

        e.g. north -> south, east -> west

        if a unexpected direction is given, returns the original direction

        e.g. up -> up, northbound -> northbound
        """

        if direction == "north":
            return "south"
        elif direction == "south":
            return "north"
        elif direction == "east":
            return "west"
        elif direction == "west":
            return "east"

        return direction

    @staticmethod
    def get_diagonal_directions(direction: str):
        """
        Assumes direction is a string representing a cardinal direction
        Returns a tuple containing the 2 directions as strings 45 degrees 
            of the given direction

        e.g. north -> (north-east, north-west), west -> (north-west, south-west)
        """

        if direction == "east" or direction == "west":
            return ("north-"+direction, "south-"+direction)
        
        if direction == "north" or direction == "south":
            return (direction+"-east", direction+"-west")

        return direction


    @staticmethod
    def get_side_directions(direction: str):
        """
        Assumes direction is a string representing a cardinal direction
        Returns a tuple containing the 2 directions as strings 90 degrees 
            of the given direction

        e.g. north -> (east, west), west -> (north, south)
        """

        if direction == "north" or direction == "south":
            return ("east", "west")

        if direction == "east" or direction == "west":
            return ("north", "south")

        return direction

    def can_add_neighbour(self):
        """ Returns True if the room has a free neighbour """
        for pos in Room.ADJ_DIRECTIONS:
            # if one of the adjacent rooms = None
            if not(self.adjacent_rooms[pos]):
                return True

        return False

    def set_neighbour(self, room, direction: str):
        """
        Assumes room is a Room object and direction is a string representing a 
            direction
        Adds the room to self.adjacent rooms dictionary
        """
        self.adjacent_rooms[direction] = room

    def get_adjacent_rooms(self):
        """ Returns the dictionary of adjacent room """
        return self.adjacent_rooms
    
    def has_neighbour(self, direction: str):
        """ 
        Assumes direction is a string representing a cardinal direction
        Returns true if room has a neighbour in that direction
        """

        if self.adjacent_rooms[direction]:
            return True
        return False

    def get_Neighbour(self, direction:str):
        """
        Assumes direction is a string representing a cardinal direction
        Returns the room object in that direction, returns None if no room exist
            in that direction
        """

        return self.adjacent_rooms[direction] 

    def get_name(self):
        """ Returns the name of the room """
        return self.name
    
    def __str__(self):
        return self.name
    
class Map:
    """
    A class that holds all the rooms in an array data structure
    """
    def __init__(self, size:int):
        """
        Assumes size is an integer representing the number of rooms
            in the map
        """

        self.size = size
        self.start_room = None
        self.rooms = []
    
    def get_map(self):
        """
        Returns the map array
        """
        return self.rooms;

    def get_start_room(self):
        """ Returns the start room of this map """
        return self.start_room
    
    def __get_random_room(self):
        rand_num = random.randint(0, len(self.rooms)-1)
        return self.rooms[rand_num]

    def __is_map_correct_size(self) -> bool:
        """ Returns True if the number of rooms is equal to the size of the map """

        return len(self.rooms) == self.size

    def add_room(self, room: Room):
        """
        Assumes room is a Room object
        Adds room to the map, if only room in map then 
            this room is also the start room
        """

        # if there isn't a start room
        if not(self.start_room):
            self.start_room = room
            self.rooms.append(room)
            return;

        
        rand_room = None
        # find a random room that can add a new neighbour
        while True:
            rand_room = self.__get_random_room()
            
            # if room cannot add a new neighbour
            if rand_room.can_add_neighbour():
                break


        # add the room to a random avaiable direction
        while True:
            rand_direction = Room.get_random_direction()
            
            # if room can add neighbour in this direction
            if rand_room.get_adjacent_rooms()[rand_direction]:
                # add room to the map
                self.rooms.append(room)
                 
                # update relevant dictionaries
                rand_room.set_adjacent_room(room, rand_direction)
                room.set_adjacent_room(rand_room, Room.get_opposite_direction(rand_direction))
                diag_directions = Room.get_diagonal_directions(rand_direction)
                side_directions = Room.get_side_directions(rand_direction)
                
                for (diag, side) in zip(diag_directions, side_directions):

                    # check if randomly selected room has diagonal neighbours
                    if rand_room.has_neighbour(diag):
                        diag_neighbour = rand_room.getNeighbour(diag)
                        opp_direction = Room.get_opposite_direction(side)
                        
                        # setting diagonal neighbour as side neighbour for new room
                        diag_neigbour.set_neighbour(room, opp_direction)
                        room.set_neighbour(diag_neigbour, side)

                break


if __name__ == "__main__":
    new_map = Map(10)

    for i in range(10):
        room = Room("Room " + str(i), "This is Room " + str(i))
        new_map.add_room(room)
        

    print(new_map.get_map())
    print(new_map.get_start_room())



