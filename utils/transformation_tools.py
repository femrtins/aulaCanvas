from utils.glut_utils import *

class TransformationTools:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = None
        self.start_y = None
        self.selected_geometry = None

    def start_transform(self, geometry, x, y):
        self.selected_geometry = geometry
        self.start_x = x
        self.start_y = y

    def translate(self, current_x, current_y):
        if not self.selected_geometry or self.start_x is None:
            return

        # Calculate displacement
        dx = current_x - self.start_x
        dy = current_y - self.start_y

        # Update geometry position
        self.selected_geometry.x0 += dx
        self.selected_geometry.y0 += dy

        # For circles, update center
        if hasattr(self.selected_geometry, 'radius'):
            pass  # Center is already updated with x0, y0

        # Update start position for next movement
        self.start_x = current_x
        self.start_y = current_y

    def scale(self, current_x, current_y):
        if not self.selected_geometry or self.start_x is None:
            return

        # Calculate scale factor based on distance from start point
        dx = current_x - self.start_x
        dy = current_y - self.start_y
        scale_factor = 1.0 + (dx + dy) / 100.0  # Adjust divisor for sensitivity

        # Scale geometry
        if hasattr(self.selected_geometry, 'width'):
            self.selected_geometry.width *= scale_factor
            self.selected_geometry.height *= scale_factor
        elif hasattr(self.selected_geometry, 'radius'):
            self.selected_geometry.radius *= scale_factor

        # Update start position
        self.start_x = current_x
        self.start_y = current_y