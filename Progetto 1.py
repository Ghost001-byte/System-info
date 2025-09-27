import platform
import os
import psutil

def mostra_info_os():
	print("Sistema operativo:", platform.system())
	print("Versione OS:", platform.version())
	print("Release:", platform.release())
	print("Nome macchina:", platform.node())
	print("Architettura:", platform.machine())
	print("Processore:", platform.processor())

def mostra_info_hardware():
	print("\n--- Hardware ---")
	print("CPU fisica:", psutil.cpu_count(logical=False))
	print("CPU logica:", psutil.cpu_count(logical=True))
	print("Frequenza CPU:", psutil.cpu_freq().current, "MHz")
	print("RAM totale:", round(psutil.virtual_memory().total / (1024**3), 2), "GB")
	print("Disco totale:", round(psutil.disk_usage('/').total / (1024**3), 2), "GB")

if __name__ == "__main__":
	mostra_info_os()
	mostra_info_hardware()
