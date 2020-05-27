class Animal():
    def __init__(self, ID="", name="", weight=int(), foot=int(), count=int()):
        self.id = ID.zfill(8)
        self.name = name
        self.weight = weight
        self.foot = foot
        self.__count = count
    
    def show_info(self):
        print("Animal ID: ", self.id)
        print("Animal name: ", self.name)
        print("Animal weight: ", self.weight)
        print("Animal foot: ", self.foot)

    def set_speed(self, speed):
        self.speed = speed
        print("Animal-{} speed: {}km/h".format(self.name, self.speed))

    def __show_count(self):
        print("Animal-%s count: %d" % (self.name, self.__count))

if __name__ == "__main__":
    cat = Animal("1", "cat", 60, 4, 10)
    cat.show_info()

    # 存取私有方法__show_count()
    cat._Animal__show_count()

    cat.set_speed(50)
    cat.name = "dog"
    cat.show_info()
    print(Animal.foot)