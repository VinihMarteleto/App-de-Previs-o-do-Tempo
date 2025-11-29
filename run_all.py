import threading
import subprocess

def run_main():
    # roda o main.py que coleta dados
    subprocess.run(["python", "src/main.py"])

def run_app():
    # roda o app.py que inicia o servidor Flask
    subprocess.run(["python", "src/app.py"])

if __name__ == "__main__":
    # cria duas threads para rodar simultâneo
    t1 = threading.Thread(target=run_main)
    t2 = threading.Thread(target=run_app)

    t1.start()
    t2.start()

    # mantém ambos rodando
    t1.join()
    t2.join()
