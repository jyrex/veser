

class User:

    def __init__(self, kode, nama, lokasi):
        self.kode = kode
        self.nama = nama
        self.lokasi = lokasi

class Kendaraan:

    def __init__(self, owner, noPolisi, jenis, warna):
        self.owner = owner
        self.noPolisi = noPolisi
        self.jenis = jenis
        self.warna = warna


class Bengkel:

    def __init__(self, kode, nama, lokasi):
        self.kode = kode
        self.nama = nama
        self.lokasi = lokasi


class Order:

    def __init__(self, kode, User, Bengkel):
        self.kode = kode
        self.user = User
        self.bengkel = Bengkel


class Detail:

    def __init__(self, kode, Order, namaService, unitPrice, quantity):
        self.kode = kode
        self.order = Order
        self.namaServis = namaService
        self.unitPrice = unitPrice
        self.quantity = quantity