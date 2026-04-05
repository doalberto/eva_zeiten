pace = 60 / 275  # Sekunden pro Meter (275m = 60s)

with open("zeiten.txt", "w") as f:
    for d in range(50, 251, 50):
        t = d * pace
        f.write(f"{d}m {t:.1f}s\n")

print("zeiten.txt wurde erstellt.")
