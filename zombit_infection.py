def answer(population, patient_x, patient_y, strength):

    def is_susceptible(y, x):
        resistance = population[y][x]
        return resistance <= strength

    def is_in_bounds(y, x):
        try:
            return True if x in range(0, (len(population[y]))) and y in range(0, (len(population))) else False
        except IndexError:
            return False

    def get_susceptible_rabbits(y, x):
        susceptible_rabbits = list()
        coords = list([[y, x-1], [y, x+1], [y-1, x], [y+1, x]])
        for (y, x) in coords:
            if is_in_bounds(y, x) and is_susceptible(y, x) and not already_infected(y, x):  # check left
                susceptible_rabbits.append([y, x])
        return susceptible_rabbits

    def make_infected(y, x):
        population[y][x] = -1

    def already_infected(y, x):
        return population[y][x] == -1

    def spread_from(biter):
        for victim in get_susceptible_rabbits(*biter):
            make_infected(*victim)
            spread_from(victim)

    def inject(patient):
        if is_susceptible(*patient):
            make_infected(*patient)
            spread_from(patient)

    patient_z = [patient_y, patient_x]
    inject(patient_z)
    return population
