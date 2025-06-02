from auth import login
from modulos import (
    network_monitor, log_analyzer, vuln_scanner, attack_prevention,
    web_traffic_analyzer, alert_system, incident_logger, report_generator
)

def show_menu():
    print("\n--- Sistema de Detección y Prevención de Ataques ---")
    print("1. Monitorear tráfico de red")
    print("2. Analizar registros del sistema")
    print("3. Escanear vulnerabilidades")
    print("4. Implementar mecanismos de prevención")
    print("5. Analizar tráfico web")
    print("6. Sistema de alertas y notificaciones")
    print("7. Registrar incidentes")
    print("8. Generar informe de seguridad")
    print("9. Salir")

def main():
    if login():
        while True:
            show_menu()
            choice = input("Seleccione una opción: ")
            if choice == "1":
                network_monitor.run()
            elif choice == "2":
                log_analyzer.run()
            elif choice == "3":
                vuln_scanner.run()
            elif choice == "4":
                attack_prevention.run()
            elif choice == "5":
                web_traffic_analyzer.run()
            elif choice == "6":
                alert_system.run()
            elif choice == "7":
                incident_logger.run()
            elif choice == "8":
                report_generator.run()
            elif choice == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    main()
