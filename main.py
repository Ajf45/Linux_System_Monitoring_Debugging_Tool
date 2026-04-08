import time

from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_usage
from monitor.process import get_top_processes
from monitor.debug import inspect_process
from utils.logger import log_event

from rich.console import Console
from rich.table import Table

console = Console()

CPU_THRESHOLD = 80.0  # CPU usage percentage threshold
MEM_THRESHOLD = 80.0  # Memory usage percentage threshold

def display_dashboard():
    while True:
        console.clear()

        cpu = get_cpu_usage()
        mem_percent, mem_used, mem_total = get_memory_usage()
        processes = get_top_processes()

        console.print(f"\n[bold cyan]System Monitor Dashboard[/bold cyan]")
        console.print(f"CPU Usage: {cpu}%")
        console.print(f"Memory Usage: {mem_percent}% ({mem_used // (1024**2)}MB / {mem_total // (1024**2)}MB)")

        if cpu > CPU_THRESHOLD:
            log_event(f"High CPU usage detected: {cpu}%")

        if mem_percent > MEM_THRESHOLD:
            log_event(f"High Memory usage detected: {mem_percent}%")

        table = Table(title="Top Processes")
        table.add_column("PID")
        table.add_column("Name")
        table.add_column("CPU %")
        table.add_column("Memory %")

        for proc in processes:
            table.add_row(
                str(proc['pid']),
                str(proc['name']),
                str(proc['cpu_percent']),
                f"{proc['memory_percent']:.2f}"
            )

        console.print(table)
        console.print("\nPress Ctrl+C to enter Debug mode...")
        
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            debug_mode()

def debug_mode():
    console.clear()
    console.print("[bold yellow]DEBUG MODE[/bold yellow]")

    try:
        pid = int(console.input("Enter PID to inspect: "))
    except ValueError:
        console.print("[red]Invalid PID. Returning to dashboard...[/red]")
        return
    
    info = inspect_process(pid)

    console.print(f"\n[bold green]Process Information for PID [/bold green]")

    for key, value in info.items():
        if key == "Open Files":
            console.print(f"{key}:")
            for f in value:
                console.print(f"  - {f}")
        else:
            console.print(f"{key}: {value}")

    input("\nPress Enter to return to dashboard...")
    display_dashboard()
            
if __name__ == "__main__":
    display_dashboard()

    