import psutil

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent, memory_info.used, memory_info.total