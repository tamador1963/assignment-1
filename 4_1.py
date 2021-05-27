class hous:
    def __init__(self,area=0,num_of_room=0):
        self._area=area
        self._num_of_room=num_of_room
    def getarea(self):
        return self._area
    def getnum_of_room(self):
        return self._num_of_room
    def setarea(self,area):
        self._area=area
    def setnum_of_room(self,num_of_room):
        self._num_of_room=num_of_room
    def __str__(self):
        return "The Hous area: "+str(self._area) +"\n\
"+"The num_of_room: "+str(self._num_of_room)

class Building(hous):
    def __init__(self,area=0,num_of_room=0,num_of_hous=0):
        super().__init__(area,num_of_room)
        self._num_of_hous=num_of_hous
    def total(self):
        t_h =(self._num_of_room*self._num_of_hous)
        return t_h

class Building_a(hous):
    def __init__(self,area=0,num_of_room=0,num_of_hous=0):
        super().__init__(area,num_of_room)
        self._num_of_hous=num_of_hous
    def total(self):
        t_a =(self._num_of_hous*self._area)
        return t_a
