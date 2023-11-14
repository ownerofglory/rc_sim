import math
import matplotlib.pyplot as plt

class SchemeConfig:
    def __init__(self, resistance, capacity, v_source):
        self.__resistance = resistance
        self.__capacity = capacity
        self.__v_source = v_source
        pass

    def calc_voltage(self, time):
        time_const = self.__resistance * self.__capacity # (R * C)
        pow = -(time/time_const) # -t / (R * C)

        return self.__v_source * (1 - math.exp(pow))
    
    def calc_current(self, time):
        time_const = self.__resistance * self.__capacity # (R * C)
        pow = -(time/time_const) # -t / (R * C)

        v_derr = self.__v_source / time_const * math.exp(pow) 

        return self.__capacity * v_derr


def get_voltage_graph(scheme, x_vals):
    y_vals = []

    for x in x_vals:
        voltage = scheme.calc_voltage(x)
        y_vals.append(voltage)

    return y_vals

def get_current_graph(scheme, x_vals):
    y_vals = []

    for x in x_vals:
        voltage = scheme.calc_current(x)
        y_vals.append(voltage)

    return y_vals


def main():
    # plot options
    # 'x' axis
    x_min = 0
    x_max = 1000 
    x_step = 1
    x_scale = 20_000 # 

    markers = [100]

    # function options
    v_source = 12
    resistance = 100
    capacity = 47E-6

    # -------------
    # scheme config
    scheme = SchemeConfig(resistance, capacity, v_source)

    x_vals = range(x_min, x_max, x_step)

    time_vals = [x / x_scale for x in x_vals]
    voltage_vals = get_voltage_graph(scheme, time_vals)
    current_vals = get_current_graph(scheme, time_vals)

    plt.ylabel("V(t), V")
    plt.xlabel("t, s")

    _, (ax_volt, ax_cur) = plt.subplots(1, 2, sharex='col')

    # Plot voltage
    ax_volt.plot(time_vals, voltage_vals, "-bD", markevery=markers, label="Voltage")
    ax_volt.grid(True, linestyle='-.', linewidth=0.5)
    ax_volt.set_xlabel('time (s)')
    ax_volt.set_ylabel('V(t), V')
    ax_volt.title.set_text(f"R={resistance}; C={capacity}; V_source={v_source}")
    ax_volt.legend()

    # Plot current
    ax_cur.plot(time_vals, current_vals, "-g", label="Current")
    ax_cur.grid(True, linestyle='-.')
    ax_cur.set_xlabel('time (s)')
    ax_cur.set_ylabel('i(t), A')
    ax_cur.title.set_text(f"R={resistance}; C={capacity}; V_source={v_source}")
    ax_cur.legend()

    plt.show()

    pass

if __name__ == "__main__":
    main()
    pass