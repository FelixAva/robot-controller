import serial
import time
import threading as th
from wlkata_UART import Wlkata_UART, MS4220_UART
from position import PositionManager

def pick_a_b ():
  # Go A
  positionMng.get_to("a")
  time.sleep(2)

  # Take the item
  robot.pump(1)
  time.sleep(3)

  # Go to Home
  positionMng.get_to_home()
  time.sleep(2)

  # Go to C
  positionMng.get_to("C")
  time.sleep(2)

  # Leave the item
  robot.pump(0)
  time.sleep(2)

  # Homming
  positionMng.get_to_home()

def get_home():
  pass

def setup_serial_connection(port_name):
    ser = serial.Serial(port_name, 115200, timeout=1)
    robot = Wlkata_UART()
    conveyor = MS4220_UART()
    conveyor.init(ser, -1)
    robot.init(ser, -1)
    return robot

if __name__ == "__main__":
    port_name = "/dev/ttyUSB0"  # Cambia esto al puerto correcto

    # Configurar la conexión serial
    robot = setup_serial_connection(port_name)

    # Configurar las posiciones
    positionMng = PositionManager(robot)

    # First record
    pick_a_b()
    # print(f"Now you are in: {positionMng.current_position}")


    #! fefefefefefe
    # current_status = robot.getStatus()
    # get_home = pos_a.get_home_angles(current_status)



    #* Go back to Home position
    # print("Starting Homming")
    # robot.homing()



# posicion deseada (0mm, 1650mm, 0m m)
