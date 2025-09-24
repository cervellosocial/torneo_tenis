def round_robin_schedule(num_players):
    if num_players % 2 != 0:
        num_players += 1  # Add a dummy player for odd numbers

    players = list(range(1, num_players + 1))
    rounds = num_players - 1
    schedule = []

    for round in range(rounds):
        pairs = []
        for i in range(num_players // 2):
            p1 = players[i]
            p2 = players[num_players - 1 - i]
            if num_players % 2 == 0 or (p1 != num_players and p2 != num_players):  # skip dummy only for odd
                pairs.append((p1, p2))
        schedule.append(pairs)
        # Standard round-robin rotation for even numbers: rotate all except the first
        players = [players[0]] + players[2:] + [players[1]]
    return schedule

# Example usage:
schedule = round_robin_schedule(12)

#Format as md table
num_players = 12
num_matches = num_players // 2
# Header
header = ["Dia"] + [f"Partido {i+1}" for i in range(num_matches)]
print("| " + " | ".join(header) + " |")
print("|" + "-----|" * len(header))
# Rows
for day, matches in enumerate(schedule, 1):
    row = [str(day)]
    for p1, p2 in matches:
        row.append(f"j{p1} vs j{p2}")
    print("| " + " | ".join(row) + " |")
