class User:
    id = 1

    def __init__(self, nama, lokasi):
        self.id = id
        self.nama = nama
        self.lokasi = lokasi
        User.id += 1


class Kendaraan:
    owner = User.id
    noPolisi = ""
    jenis = ""
    warna = ""
    def __init__(self, owner, noPolisi, jenis, warna):
        self.owner = owner
        self.noPolisi = noPolisi
        self.jenis = jenis
        self.warna = warna


class Bengkel:
    id = 1

    def __init__(self, nama, lokasi):
        self.id = id
        self.nama = nama
        self.lokasi = lokasi
        Bengkel.id += 1


class Order:
    id = 1
    user = User.id
    bengkel = Bengkel.id
    total_harga = 0

    def __init__(self, User, Bengkel):
        self.id = id
        self.user = User.id
        self.bengkel = Bengkel.id
        Order.id += 1


class Detail:
    id = 1
    order = Order.id
    unitPrice = 0
    namaServis = ""
    quantity = 0
    status = ""

    def __init__(self, Order, namaService, unitPrice, quantity):
        self.id = id
        self.order = Order.id
        self.namaServis = namaService
        self.unitPrice = unitPrice
        self.quantity = quantity
        Detail.id += 1