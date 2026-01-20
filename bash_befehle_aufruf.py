import subprocess
import sys


def execute_bash(command: str):
    """
    Führt einen Bash-Befehl aus und gibt ein Tupel zurück:
    (returncode, stdout)

    Bei Fehlern wird eine Fehlermeldung ausgegeben und das Skript beendet.

    Parameter:
    command (str): Der Bash-Befehl, der ausgeführt werden soll

    Rückgabe:
    tuple: (returncode: int, stdout: str)
    """
    try:
        result = subprocess.run(
            command,
            shell=True,  # erlaubt Ausführung von Strings wie in Bash
            capture_output=True,  # stdout und stderr werden erfasst
            text=True,  # gibt Strings statt Bytes zurück
            check=False  # wir prüfen Returncode selbst
        )

        if result.returncode != 0:
            print(f"Fehler beim Ausführen des Befehls: {command}")
            print(f"Fehlermeldung: {result.stderr.strip()}")
            sys.exit(result.returncode)

        return (result.returncode, result.stdout.strip())

    except Exception as e:
        print(f"Unerwarteter Fehler bei Befehl '{command}': {e}")
        sys.exit(1)