from classes import *

user = [User(1, "Randy", [1, 3]),
        User(2, "Axel", [4, 5]),
        User(3, "Julio", [2, 7])
        ]

bengkel = [Bengkel(1, "Yamaha", [3, 4]),
           Bengkel(2, "Suzuki", [1, 1]),
           Bengkel(3, "Honda", [0, 6])
           ]

order = [Order(1, 1, 1), Order(2,2,2)]

detail = [Detail(order[0], "ban", 10000, 1), Detail(order[1], "dashboard", 100000, 2)]