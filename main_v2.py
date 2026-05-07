import os
import time
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich import box

console = Console()

class VanguardOS:
    def __init__(self):
        self.name = "Vanguard-OS"
        self.version = "1.2"
        self.developer = "Nader Ahmed"
        self.memory_total = 8192
        self.files = ["kernel.sys", "bootloader.bin", "config.json", "firewall.rules"]
        self.processes = [
            {"pid": 101, "name": "System_Init", "burst": 5, "priority": 1},
            {"pid": 202, "name": "Net_Monitor", "burst": 8, "priority": 3},
            {"pid": 303, "name": "Security_Scan", "burst": 12, "priority": 2}
        ]

    def show_header(self):
        console.print(Panel.fit(
            f"[bold red]{self.name} v{self.version}[/bold red]\n"
            f"[cyan]Cybersecurity & OS Simulator | Dev: {self.developer}[/cyan]",
            border_style="bold blue", box=box.DOUBLE
        ))

    # 1. Process Management (Round Robin & Priority)
    def process_mgmt(self):
        console.print("\n[bold yellow]🔄 CPU Scheduling (Round Robin)[/bold yellow]")
        table = Table(box=box.ROUNDED)
        table.add_column("PID")
        table.add_column("Process")
        table.add_column("Burst Time")
        table.add_column("Priority")
        
        for p in self.processes:
            table.add_row(str(p['pid']), p['name'], f"{p['burst']}ms", str(p['priority']))
        console.print(table)

        with Progress(transient=True) as progress:
            task = progress.add_task("[cyan]Executing Cycles...", total=len(self.processes))
            for p in self.processes:
                time.sleep(0.6)
                console.print(f"  [green]✔[/green] Quantum allocated to [magenta]{p['name']}[/magenta]")
                progress.update(task, advance=1)
        console.print("[italic green]All processes synchronized.[/italic green]")

    # 2. Memory Management (Paging Simulation)
    def memory_mgmt(self):
        console.print("\n[bold blue]🧠 Memory & Paging System[/bold blue]")
        used = random.randint(2000, 5000)
        console.print(f"RAM Status: {used}MB / {self.memory_total}MB")
        
        with Progress(BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%")) as progress:
            progress.add_task("Paging...", total=100, completed= (used/self.memory_total)*100)
        console.print("[dim]Logic: Segmentation and Paging active. No Page Faults.[/dim]")

    # 3. File System (EXT4 Simulation)
    def file_system(self):
        console.print("\n[bold green]📁 File System Manager[/bold green]")
        table = Table(box=box.SIMPLE)
        table.add_column("Name", style="bold")
        table.add_column("Perms")
        for f in self.files:
            table.add_row(f"📄 {f}", "rwxr-xr-x")
        console.print(table)

    # 4. Deadlock Detection (Banker's Algorithm Sim)
    def deadlock_check(self):
        console.print("\n[bold red]🛡 Deadlock Detection Engine[/bold red]")
        console.print("Checking Resource Allocation Graph...")
        time.sleep(1)
        console.print("[bold green]Safe State:[/bold green] No Deadlock Detected. System is secure. ✅")

    # 5. I/O Management
    def io_mgmt(self):
        console.print("\n[bold]🔌 Connected Devices:[/bold] [green]Keyboard, Mouse, Network_Adapter[/green]")
        cmd = console.input("[bold red]Vanguard@Admin:~$ [/bold red]")
        console.print(f"Executing '{cmd}' via I/O Interrupt...")

# ================= Main Execution =================
if __name__ == "__main__":
    os_sim = VanguardOS()
    os_sim.show_header()
    
    while True:
        console.print("\n[1] Processes [2] Memory [3] Files [4] Deadlock [5] I/O [0] Exit")
        choice = console.input("\n[bold cyan]Select Module > [/bold cyan]")

        if choice == "1": os_sim.process_mgmt()
        elif choice == "2": os_sim.memory_mgmt()
        elif choice == "3": os_sim.file_system()
        elif choice == "4": os_sim.deadlock_check()
        elif choice == "5": os_sim.io_mgmt()
        elif choice == "0": break
        else: console.print("[red]Error: Unknown Module.[/red]")

