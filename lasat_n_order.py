orders = []

def record(order_id):
    orders.append(order_id)

def get_last(i):
    return orders[-i]

if __name__ == "__main__":
    record(1)
    record(2)
    record(3)
    record(4)
    record(5)
    print(get_last(4))