import psutil

def get_top_processes(limit=10):
    processes = []
    
    psutil.cpu_percent(interval=None)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info

            cpu = info['cpu_percent'] if info['cpu_percent'] is not None else 0.0
            mem = info['memory_percent'] if info['memory_percent'] is not None else 0.0

            processes.append({
                'pid': info['pid'],
                'name': info['name'],
                'cpu_percent': cpu,
                'memory_percent': mem
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    return processes[:limit]