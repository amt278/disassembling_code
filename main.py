import dis

def add(x, y, z):
    return x + y + z

# dis.dis('1+2') # byhwl el code el gowa el '' l assembly
dis.dis(add)
