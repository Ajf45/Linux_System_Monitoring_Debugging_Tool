import psutil

def inspect_process(pid):
    try:
        proc = psutil.Process(pid)

        info = {
            "PID": proc.pid,
            "Name": proc.name(),
            "Status": proc.status(),
            "CPU %": proc.cpu_percent(interval=0.5),
            "Memory %": proc.memory_percent(),
            "Threads": proc.num_threads(),
            "Executable": proc.exe(),
        }

        try:
            files = proc.open_files()
            file_list = [f.path for f in files]
        except Exception:
            file_list = ["Access Denied"]

        info["Open Files"] = file_list

        return info
    except psutil.NoSuchProcess:
        return {"Error": "Process not found"}
    except psutil.AccessDenied:
        return {"Error": "Access denied to process information"}
    
    