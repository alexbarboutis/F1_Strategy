from simulation import RaceSimulation  # adjust to your file name

def main():
    config_path = 'config/race_config.yaml'  # Change if your file name differs
    sim = RaceSimulation(config_path)

    print(f"Starting race: {sim.race_info.get('name', 'Unnamed')} ({sim.laps} laps)")

    while sim.current_lap < sim.laps:
        sim.simulate_lap()

    print("\nFinal classification:")
    for pos, name in enumerate(sim.order_history[-1], start=1):
        print(f"P{pos}: {name}")

    sim.plot_race()

if __name__ == "__main__":
    main()