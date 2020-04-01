class Person():

    def __init__(self, first_name, last_name):

        self.first_name = first_name

        self.last_name = last_name



    def First_name(self):

        return self.first_name



    def Last_name(self):

        return self.last_name



    def __str__(self):

        return "%s        %s     " % (self.first_name, self.last_name)





class Student(Person):

    def __init__(self, first_name, last_name, sub_area):

        Person.__init__(self, first_name, last_name)

        self.sub_area = sub_area



    def Sub_area(self):

        return self.sub_area



    def print_name_sub(self):

        print(Person.__str__(self), self.sub_area)