import rasterization_algo
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time


class Application:
    def __init__(self) -> None:
        self._window = tk.Tk()
        self._window.geometry("600x500")
        self._window.resizable(False, False)

        self._x0_label = tk.Label(self._window, text='x0')
        self._x0_label.place(x=120, y=20)

        self._x0_field = tk.Entry(self._window, width=10)
        self._x0_field.place(x=170, y=20)

        self._y0_label = tk.Label(self._window, text="y0")
        self._y0_label.place(x=320, y=20)

        self._y0_field = tk.Entry(self._window, width=10)
        self._y0_field.place(x=370, y=20)

        self._radius_label = tk.Label(self._window, text="Radius")
        self._radius_label.place(x=200, y=50)

        self._radius_field = tk.Entry(self._window, width=10)
        self._radius_field.place(x=275, y=50)

        self._bresenham_circle_button = tk.Button(self._window, command=self._onBresenhamCircleButtonClick,
                                                  text="Draw circle with Bresenham algorithm")
        self._bresenham_circle_button.place(x=200, y=80)

        self._x1_label = tk.Label(self._window, text="x1")
        self._x1_label.place(x=120, y=150)

        self._x1_field = tk.Entry(self._window, width=10)
        self._x1_field.place(x=170, y=150)

        self._y1_label = tk.Label(self._window, text="y1")
        self._y1_label.place(x=320, y=150)

        self._y1_field = tk.Entry(self._window, width=10)
        self._y1_field.place(x=370, y=150)

        self._x2_label = tk.Label(self._window, text="x2")
        self._x2_label.place(x=120, y=180)

        self._x2_field = tk.Entry(self._window, width=10)
        self._x2_field.place(x=170, y=180)

        self._y2_label = tk.Label(self._window, text="y2")
        self._y2_label.place(x=320, y=180)

        self._y2_field = tk.Entry(self._window, width=10)
        self._y2_field.place(x=370, y=180)

        self._bresenham_line_button = tk.Button(self._window, command=self._onBresenhamLineButtonClick,
                                               text="Draw line with Bresenham algorithm")
        self._bresenham_line_button.place(x=200, y=210)

        self._dda_button = tk.Button(self._window, command=self._onDDAButtonClick,
                                     text="Draw line with DDA algorithm")
        self._dda_button.place(x=220, y=240)

        self._step_button = tk.Button(self._window, command=self._onStepButtonClick,
                                      text="Draw line with step algorithm")
        self._step_button.place(x=220, y=270)

        self._time_label = tk.Label(self._window)
        self._time_label.place(x=150, y=400)
        

    def run(self) -> None:
        self._window.mainloop()

    def __draw_line(self, coordinates: list[tuple[int, int]]):
        fig = plt.figure(1)
        ax = fig.gca()

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        x_min, y_min = min(coordinates, key=lambda x: x[0])
        x_max, y_max = max(coordinates, key=lambda x: x[0])
        ax.set_xlim([x_min - 20, x_max + 20])
        ax.set_ylim([min(y_min, y_max) - 20, max(y_min, y_max) + 20])
        for (x, y) in coordinates:
            ax.plot(x, y, marker='s', color='black')
        fig.canvas.draw()
        x_ticks = np.arange(x_min - 20, x_max + 21)
        y_ticks = np.arange(min(y_min, y_max) - 20, max(y_min, y_max) + 21)
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)
        ax.grid(which='both')
        fig.show()

    def _onBresenhamCircleButtonClick(self) -> None:
        x0 = int(self._x0_field.get())
        y0 = int(self._y0_field.get())
        radius = int(self._radius_field.get())

        start = time.process_time()
        coordinates = rasterization_algo.bresenham_for_circle_algo((x0, y0), radius)
        end = time.process_time()

        self._time_label.config(text=f"Exceeded time: {end - start: .7f} ms")
        self.__draw_line(coordinates)

    def _onBresenhamLineButtonClick(self) -> None:
        x1 = int(self._x1_field.get())
        y1 = int(self._y1_field.get())
        x2 = int(self._x2_field.get())
        y2 = int(self._y2_field.get())

        start = time.process_time()
        try:
            coordinates = rasterization_algo.bresenham_for_line_algo((x1, y1), (x2, y2))
        except RuntimeError as err:
            messagebox.showerror(title="Error", message=str(err))
            return None
        end = time.process_time()

        self._time_label.config(text=f"Exceeded time: {end - start: .7f} ms")
        self.__draw_line(coordinates)

    def _onDDAButtonClick(self) -> None:
        x1 = int(self._x1_field.get())
        y1 = int(self._y1_field.get())
        x2 = int(self._x2_field.get())
        y2 = int(self._y2_field.get())

        start = time.process_time()
        coordinates = rasterization_algo.digital_differential_analyzer_algo((x1, y1), (x2, y2))
        end = time.process_time()

        self._time_label.config(text=f"Exceeded time: {end - start: .7f} ms")
        self.__draw_line(coordinates)

    def _onStepButtonClick(self) -> None:
        x1 = int(self._x1_field.get())
        y1 = int(self._y1_field.get())
        x2 = int(self._x2_field.get())
        y2 = int(self._y2_field.get())

        start = time.process_time()
        coordinates = rasterization_algo.step_algo((x1, y1), (x2, y2))
        end = time.process_time()

        self._time_label.config(text=f"Exceeded time: {end - start: .7f} ms")
        self.__draw_line(coordinates)
