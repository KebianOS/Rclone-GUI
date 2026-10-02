import subprocess


class Rclone:

    def version(self):
        resultado = subprocess.run(
            ["rclone", "version"],
            capture_output=True,
            text=True
        )

        return resultado.stdout

    def listar_remotos(self):
        resultado = subprocess.run(
            ["rclone", "listremotes"],
            capture_output=True,
            text=True
        )

        return resultado.stdout.splitlines()