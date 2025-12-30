"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800 
        and neutrons_emitted > 500 
        and temperature * neutrons_emitted < 500000):
        return True
    return False

        


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif 60 <= efficiency < 80:
        return 'orange'
    elif 30 <= efficiency < 60:
        return 'red'
    else:
        return 'black'



def fail_safe(temperature, neutrons_produced_per_second, threshold):
    generated_value = temperature * neutrons_produced_per_second
    lower_limit = threshold * 0.90
    upper_limit = threshold * 1.10

    if generated_value < lower_limit:
        return 'LOW'
    elif lower_limit <= generated_value <= upper_limit:
        return 'NORMAL'
    else:
        return 'DANGER'

