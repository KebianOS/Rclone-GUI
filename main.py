from rclone_gui.rclone import Rclone


rclone = Rclone()

print("Versión de rclone:")
print(rclone.version())

print("Remotos:")
print(rclone.listar_remotos())