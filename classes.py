class User:
    'menampung atribut dan method untuk user'
    userCount = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        User.userCount += 1

    def dispCount(self):
        print("jumlah user : ", User.userCount)

    def dispUser(self):
        print("nama user : ", User.name, "\nlokasi : ", User.location)

class Bengkel:
    'class untuk menampung bengkel'
    countBengkel = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Bengkel.countBengkel += 1

    def dispCount(self):
        print("jumlah bengkel : ", Bengkel.userCount)

    def dispUser(self):
        print("nama bengkel : ", Bengkel.name, "\nlokasi : ", Bengkel.location)