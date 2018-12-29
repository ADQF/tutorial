class People():
    def __init__(self, name, race, country, height, bodyweight):
        self.name = name
        self.race = race
        self.country = country
        self.height = height
        self.BodyWeight = bodyweight
        self.BMI = (bodyweight/2)/(height/100*2)

    def print_race(self):
        print('{}的人种是{}'.format(self.name, self.race))

    def print_country(self):
        print('{}的国家是{}'.format(self.name, self.country))

    def print_height(self):
        print('{}的身高是{}'.format(self.name, self.height))

    def print_BodyWeight(self):
        print('{}的体重是{}'.format(self.name, self.BodyWeight))
    def print_BMI(self):
        print('{}的BMI是{}'.format(self.name, int(self.BMI)))
stu1 = People('小明','黄种人','中国', 180, 70)
stu2 = People('爱丽丝', '白种人', '英国', 150, 110)

stu2.print_BMI()