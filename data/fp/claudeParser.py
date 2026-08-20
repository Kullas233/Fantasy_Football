import re

INPUT_PATH = 'Fantasy_Football_26/data/fp/all.txt'
OUTPUT_PATH = 'Fantasy_Football_26/data/fp/data.csv'

# A rank line looks like "157\t\t" (rank number followed by two empty tab-separated fields)
RANK_LINE = re.compile(r'^\d+\t\t$')

# A name line looks like "Ja'Marr Chase (CIN)" or "Malik Nabers (NYG) " (trailing space)
NAME_LINE = re.compile(r'^(.+?)\s*\(([A-Z]{2,4})\)\s*$')


def just_get_letters(text):
    """Strip everything but uppercase letters, e.g. 'WR6' -> 'WR'."""
    return ''.join(ch for ch in text if re.match('[A-Z]', ch))


def parse_players(lines):
    players = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i].rstrip('\n')

        if not RANK_LINE.match(line):
            i += 1
            continue

        rank = line.split('\t')[0]
        i += 1

        # Skip anything until we hit the "Name (TEAM)" line (defensively skips
        # blank lines / tier separators like "Tier 2\t \tCustomize Tiers")
        while i < n and not NAME_LINE.match(lines[i].rstrip('\n')):
            i += 1
        if i >= n:
            break

        name_line = lines[i].rstrip('\n')
        match = NAME_LINE.match(name_line)
        name, team = match.group(1).strip(), match.group(2)
        i += 1
        if i >= n:
            break

        # Pos/bye line, e.g. "RB1\t6\t" or "RB1\t6\tCoach Upside rating"
        # (the "Coach Upside rating" / "Coach Bust rating" / star-rating /
        # delta lines that may follow are simply ignored - we resync on the
        # next rank line)
        pos_line = lines[i].rstrip('\n')
        i += 1
        parts = pos_line.split('\t')
        pos_field = parts[0] if parts else ''
        pos = just_get_letters(pos_field)

        # DST rows: name line is "Houston Texans (HOU)" -> "Texans Defense"
        if pos == 'DST':
            name = name.split(' ')[-1] + ' Defense'

        # Known name correction
        if name == 'Hollywood Brown':
            name = 'Marquise Brown'

        # Known team code correction
        if team == 'JAC':
            team = 'JAX'

        players.append((rank, name, pos, team))

    return players


with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()

players = parse_players(lines)

out_lines = ["Rank,Name,Pos,Team,Cost"]
for rank, name, pos, team in players:
    out_lines.append(f"{rank},{name},{pos},{team},-1")

with open(OUTPUT_PATH, 'w') as f:
    f.write("\n".join(out_lines) + "\n")

print(f"Parsed {len(players)} players -> {OUTPUT_PATH}")
