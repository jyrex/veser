

class User:

    def __init__(self, id, nama, lokasi):
        self.id = id
        self.nama = nama
        self.lokasi = lokasi

class Kendaraan:

    def __init__(self, owner, noPolisi, jenis, warna):
        self.owner = owner
        self.noPolisi = noPolisi
        self.jenis = jenis
        self.warna = warna


class Bengkel:

    def __init__(self, id, nama, lokasi):
        self.id = id
        self.nama = nama
        self.lokasi = lokasi


class Order:

    def __init__(self, id, User, Bengkel):
        self.id = id
        self.user = User
        self.bengkel = Bengkel


class Detail:

    def __init__(self, id, Order, namaService, unitPrice, quantity):
        self.id = id
        self.order = Order
        self.namaServis = namaService
        self.unitPrice = unitPrice
        self.quantity = quantity