import math

class Force(object):
    """
    Force Class
    Contains a magnitude and angle of a force
    Allows for the calculation of the x and y components of the force
    """
    def __init__(self, magnitude : float=0.00, angle: float=0.00):
        """
        Force constructor
        :param magnitude: Magnitude of the force
        :param angle: Angle of the force
        """
        self._magnitude = magnitude
        self._angle = angle
        pass

    def get_magnitude(self) -> float:
        """
        Returns the magnitude of the force
        :return: int: magnitude of the force
        """
        return self._magnitude

    def get_angle(self) -> float:
        """
        Returns the angle of the force
        :return: int: angle of the force
        """
        return self._angle

    def get_components(self) -> tuple:
        """
        Returns the x and y components of the force.
        x = magnitude * cos(angle)
        y = magnitude * sin(angle)
        :return: tuple: x and y components of the force
        """
        fx = self._magnitude * math.cos(math.radians(self._angle))
        fy = self._magnitude * math.sin(math.radians(self._angle))
        return fx, fy


    def __str__(self):
        """
        Returns a string representation of the force
        :return: str: string representation of the force
        """
        return ("Magnitude: {:.2f}\nAngle: {:.2f}"
                .format(self._magnitude, self._angle))

    def __eq__(self, other):
        """
        Compares two Force objects for equality
        :param other: Force object to compare to
        :return: bool: True if the objects are equal, False otherwise
        """
        if isinstance(other, Force):
            return (self._magnitude == other._magnitude
                    and self._angle == other._angle)
        return False

    def __add__(self, other):
        """
        Adds two Force objects together
        :param other: Force object to add to self
        :return: Force: new Force object with the sum of the two forces
        """
        if isinstance(other, Force):
            fx_sum, fy_sum = self.get_components()
            fx_sum += other.get_components()[0]
            fy_sum += other.get_components()[1]
            other._magnitude = math.sqrt(fx_sum ** 2 + fy_sum ** 2)
            other._angle = math.degrees(math.atan(fy_sum / fx_sum))
            if other._angle < 0:
                other._angle += 360
            return other
        return None


class ForceCalculator(object):
    """
    ForceCalculator Class
    Contains a dictionary of forces
    Allows for the addition, removal, and computation of forces
    """
    def __init__(self, forces: dict=None):
        """
        ForceCalculator constructor
        :param forces: Dictionary of forces.
        If none is provided, an empty dictionary is created.
        """
        self._forces = forces if forces is not None else {}
        pass

    def get_forces(self) -> dict:
        """
        Returns the dictionary of forces
        :return: dict: dictionary of forces
        """
        return self._forces

    def add_force(self, name: str, magnitude: float, angle: float) -> None:
        """
        Adds a force to the dictionary of forces
        :param name: Name of the force.
        If the name already exists, a RuntimeError is raised.
        :param magnitude: Magnitude of the force
        :param angle: Angle of the force
        :return: None
        """

        if name in self._forces:
            raise RuntimeError("\nForce object {} already exists!"
                               .format(name))
        else:
            self._forces[name] = Force(magnitude, angle)
        pass

    def remove_force(self, name: str) -> None:
        """
        Removes a force from the dictionary of forces
        :param name: Removes the force with the given name.
         If the name does not exist, a RuntimeError is raised.
        :return: None
        """
        if name not in self._forces:
            raise RuntimeError("\nForce object {} does not exist!"
                               .format(name))
        else:
            del self._forces[name]
        pass

    def __getitem__(self, name) -> Force:
        """
        Returns the force with the given name
        :param name: Name of force to return
        :return: Force: force with the given name
        """
        if name not in self._forces:
            raise RuntimeError("\nForce object {} does not exist!"
                               .format(name))
        return self._forces[name]

    def compute_net_force(self) -> Force:
        """
        Computes the net force of all the forces in the dictionary
        :return: Force: net force of all the forces
        """
        net_force = Force()
        if len(self._forces) != 0:
            for force in self._forces.values():
                net_force += force
        return net_force

    def __str__(self):
        """
        Returns a string representation of the ForceCalculator object
        :return: str: string representation of the ForceCalculator object
        """
        force_str = ""
        count = 1
        for name, force in self._forces.items():
            force_str += ("\nForce #{:02}: {}\n{}"
                          .format(count, name, str(force)))
            count += 1
        return force_str