import psutil

def check_load():
    """
    Get loads with psutil
    """
    loads = list(psutil.getloadavg())
    num_logical_cpu = psutil.cpu_count(logical=True)
    for i, _ in enumerate(loads):
        loads[i] /= num_logical_cpu
    return loads

if __name__ == "__main__":
    load_1, load_5, load_15 = check_load()
    print(f"{load_1}, {load_5}, {load_15}")
