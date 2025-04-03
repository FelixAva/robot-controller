class Position:
  def __init__(self, id, categories, angles):
    self.id = id
    self.categories = categories
    self.angles = angles

  def get_position(self):
    return self.current_position

  def set_position(self, position: str):
    self.current_position = position

  def get_angles(self, position: str):
    return self.angles

  def set_angles(self, angles):
    self.angles = angles

class PositionManager:
  def __init__(self, robot):
    self.saved_positions = {
      "A": {
        "categories": ["pet"],
        "angles": [0, 70, -38, 0, -30, 0]
      },
      "B": {
        "categories": ["pet"],
        "angles": [90, 70, -38, 0, -30, 0]
      },
      "C": {
        "categories": ["pet"],
        "angles": [-90, 70, -38, 0, -30, 0]
      }
    }
    self.current_position = "Home"
    self.robot = robot

  def save_current_position(self):
    pass

  def get_robot_status(self):
    return self.robot.getStatus()

  def get_current_angles(self):
    def filter_angles(status):
      status_angles = ["angle_X", "angle_Y", "angle_Z", "angle_A", "angle_B", "angle_C"]
      angles = [status.get(x) for x in status_angles]
      return angles

    status = self.get_robot_status()
    current_angles = filter_angles(status)
    print(current_angles)

  def get_angles_of(self, position):
    angles = self.saved_positions[position]

    return angles["angles"]

  def get_home_angles(self):
    def reverse_angles(current_angles):
      angle = [x * -1 for x in current_angles] # Create a new list with the inverse of the angles
      return angle

    current_angles = self.get_angles_of(self.current_position)

    return reverse_angles(current_angles)

  def get_to_home(self):
    home_angles = self.get_home_angles()

    self.robot.writeangle(position=1, x=home_angles[0], y=home_angles[1], z=home_angles[2], a=home_angles[3], b=home_angles[4], c=home_angles[5])
    self.current_position = "Home"

  def get_to(self, position: str):
    position = position.upper()
    if self.current_position == position:
      print("You're already at: " + position)
      return

    new_angles = self.saved_positions[position.upper()]
    new_angles = new_angles["angles"]

    self.robot.writeangle(position=1, x=new_angles[0], y=new_angles[1], z=new_angles[2], a=new_angles[3], b=new_angles[4], c=new_angles[5])
    self.current_position = position
