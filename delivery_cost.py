def delivery_cost(km, sur, size, frag):
    # catch errors
    if km < 1:
        return "Invalid 'km' value!"
    elif km > 30 and frag:
        return "Can't deliver fragile orders more than 30 km"

    # cost calculation
    cost = distance_cost(km) + size_cost(size) + fragility(frag)
    cost = surge(sur, cost)
    return cost if cost > 400 else 400


def distance_cost(km):
    cost = 0
    if km <= 2:
        cost += 50
    elif km <= 10:
        cost += 100
    elif km <= 30:
        cost += 200
    elif km > 30:
        cost += 300
    return cost


def size_cost(size):
    cost = 0
    if size == "Big":
        cost += 200
    elif size == "Small":
        cost += 100
    return cost


def fragility(frag):
    cost = 0
    if frag is True:
        cost += 300
    return cost


def surge(sur, cost):
    if sur == 1.6:
        cost *= 1.6
    elif sur == 1.4:
        cost *= 1.4
    elif sur == 1.2:
        cost *= 1.2
    else:
        cost *= 1
    return int(cost)
