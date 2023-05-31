import tkinter as tk
import math, random

# Константы
WIDTH = 1920
HEIGHT = 1080
SUN_RADIUS = 28
PLANET_RADIUS = {
    'Mercury': 8,
    'Venus': 18,
    'Earth': 18,
    'Mars': 14,
    'Jupiter': 28,
    'Saturn': 25,
    'Uranus': 20,
    'Neptune': 20
}
PLANET_COLORS = {
    'Mercury': 'gray',
    'Venus': 'sandy brown',
    'Earth': 'blue',
    'Mars': 'red',
    'Jupiter': 'orange',
    'Saturn': 'khaki',
    'Uranus': 'light blue',
    'Neptune': 'dark blue'
}
PLANET_SPEEDS = {
    'Mercury': 1,
    'Venus': 0.8,
    'Earth': 0.6,
    'Mars': 0.5,
    'Jupiter': 0.2,
    'Saturn': 0.15,
    'Uranus': 0.1,
    'Neptune': 0.08
}
PLANET_INFO = {
    'Mercury': {
        'Orbital Characteristics': '47,36 km/sec',
        'Physical Characteristics': '3,285E23 kg',
        'Temperature': '349.9 °C',
        'Atmosphere': 'Oxygen, Sodium, Hydrogen, Helium'
    },
    'Venus': {
        'Orbital Characteristics': '35 km/sec',
        'Physical Characteristics': '4,867E24 kg',
        'Temperature': '462 °C',
        'Atmosphere': 'Carbon Dioxide, Nitrogen'
    },
    'Earth': {
        'Orbital Characteristics': '29,76 km/sec',
        'Physical Characteristics': '5,973E24 kg',
        'Temperature': '12 °C',
        'Atmosphere': 'Nitrogen, Oxygen, Argon, Carbon dioxide'
    },
    'Mars': {
        'Orbital Characteristics': '24,13 km/sec',
        'Physical Characteristics': '6,39E23 kg',
        'Temperature': '-60 °С',
        'Atmosphere': 'Carbon Dioxide, Nitrogen, Argon, Oxygen, Carbon Monoxide'
    },
    'Jupiter': {
        'Orbital Characteristics': '13,07 km/sec',
        'Physical Characteristics': '1,898E27 kg',
        'Temperature': '-110 °С',
        'Atmosphere': 'Hydrogen, Helium, Methane and Ammonia'
    },
    'Saturn': {
        'Orbital Characteristics': '9,69 km/sec',
        'Physical Characteristics': '5,683Е26 kg',
        'Temperature': '-150 °C',
        'Atmosphere': 'Hydrogen, Helium'
    },
    'Uranus': {
        'Orbital Characteristics': '6,81 km/sec',
        'Physical Characteristics': '8,681E25 kg',
        'Temperature': '-195 °C',
        'Atmosphere': 'Hydrogen, Helium, Methane'
    },
    'Neptune': {
        'Orbital Characteristics': '5,4349 km/sec',
        'Physical Characteristics': '1,024E26 kg',
        'Temperature': '-200 °C',
        'Atmosphere': 'Hydrogen, Helium, Methane'
    }
}

class Planet:
    def __init__(self, canvas, name, radius, color, speed, orbit_radius):
        self.canvas = canvas
        self.name = name
        self.radius = radius[name]
        self.color = color
        self.speed = speed
        self.orbit_radius = orbit_radius
        self.angle = 0
        self.planet_id = self.canvas.create_oval(0, 0, 0, 0, fill=self.color)

    def move(self):
        self.angle += self.speed
        x = WIDTH / 2 + math.cos(math.radians(self.angle)) * self.orbit_radius
        y = HEIGHT / 2 + math.sin(math.radians(self.angle)) * self.orbit_radius
        self.canvas.coords(self.planet_id, x - self.radius, y - self.radius,
                           x + self.radius, y + self.radius)

class SolarSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.stars = []
        for i in range(190):
            x=random.randint(0, WIDTH)
            y=random.randint(0, HEIGHT)
            self.stars.append(self.canvas.create_oval(x, y, x+5, y+5, fill='white'))
            
        
        self.sun = self.canvas.create_oval(WIDTH/2 - SUN_RADIUS, HEIGHT/2 - SUN_RADIUS,
                                           WIDTH/2 + SUN_RADIUS, HEIGHT/2 + SUN_RADIUS, fill='yellow')

        self.planets = []
        for name, color in PLANET_COLORS.items():
            speed = PLANET_SPEEDS[name]
            orbit_radius = (PLANET_RADIUS[name] + 35) * (list(PLANET_COLORS.keys()).index(name) + 1)
            planet = Planet(self.canvas, name, PLANET_RADIUS, color, speed, orbit_radius)
            self.planets.append(planet)

        self.canvas.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        for planet in self.planets:
            x0, y0, x1, y1 = self.canvas.coords(planet.planet_id)
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                self.show_planet_info(planet.name)
                break

    def show_planet_info(self, planet_name):
        info = PLANET_INFO[planet_name]
        info_window = tk.Toplevel(self.root)
        info_window.title(planet_name)
        for i, (key, value) in enumerate(info.items()):
            label = tk.Label(info_window, text=key + ': ' + value)
            label.pack(pady=5)

    def animate(self):
        for planet in self.planets:
            planet.move()
        self.root.after(10, self.animate)

if __name__ == '__main__':
    root = tk.Tk()
    app = SolarSystemApp(root)
    app.animate()
    root.mainloop()
