class Animal():
    def __init__(self, num="", name="", weight=int(), foot=int(), count=int()):
        self.__num = num.zfill(8)
        self.__name = name
        self.__weight = weight
        self.__foot = foot
        self.__count = count
    
    @property
    def num(self):
        return self.__num
    # def get_num(self):
    #     return self.__num
    @num.setter
    def num(self, num):
        assert type(num) == str, "Please input string !"
        self.__num = num

    @num.deleter
    def num(self):
        del self.__num

    def show_info(self):
        print("Animal num: ", self.__num)
        print("Animal name: ", self.__name)
        print("Animal weight: ", self.__weight)
        print("Animal foot: ", self.__foot)

    def set_speed(self, speed):
        self.__speed = speed
        print("Animal-{} speed: {}km/h".format(self.__name, self.__speed))

    def __show_count(self):
        print("Animal-%s count: %d" % (self.__name, self.__count))

if __name__ == "__main__":
    Animal()
    cat = Animal("1", "cat", 60, 4, 10)
    cat.show_info()

    # 存取私有方法__show_count()
    cat._Animal__show_count()

    # cat.set_num('20')
    print(cat.num)
    cat.num = "100"
    print(cat.num)
    del cat.num
    print(cat.num)
    