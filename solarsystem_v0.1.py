import tkinter as tk

# Константы
WIDTH = 800
HEIGHT = 600
PLANET_RADIUS = 20
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
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Venus': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Earth': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Mars': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Jupiter': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Saturn': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Uranus': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    },
    'Neptune': {
        'Orbital Characteristics': '...',
        'Physical Characteristics': '...',
        'Temperature': '...',
        'Atmosphere': '...'
    }
}

class Planet:
    def __init__(self, canvas, name, radius, color, speed):
        self.canvas = canvas
        self.name = name
        self.radius = radius
        self.color = color
        self.speed = speed
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.planet_id = self.canvas.create_oval(0, 0, 0, 0, fill=self.color)

    def move(self):
        self.x += self.speed
        self.y = HEIGHT / 2
        self.canvas.coords(self.planet_id, self.x - self.radius, self.y - self.radius,
                           self.x + self.radius, self.y + self.radius)

class SolarSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solar System")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        self.planets = []
        for name, color in PLANET_COLORS.items():
            speed = PLANET_SPEEDS[name]
            planet = Planet(self.canvas, name, PLANET_RADIUS, color, speed)
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
