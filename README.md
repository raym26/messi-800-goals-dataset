# Messi 800 Goals Dataset...and Claude Code Experimentation

A comprehensive dataset documenting Lionel Messi's first 800 career goals, manually transcribed from video footage. This dataset captures detailed information about each goal including location, type, opponent, and context.

## About This Project

This dataset was created for two main purposes:
1. **Data Sharing**: Contributing to the sports analytics community by providing detailed, manually curated data about one of football's greatest players
2. **Learning Claude Code**: Using this project as a hands-on way to explore Claude Code's capabilities for data processing, analysis, and collaborative development

## Dataset Overview

- **Total Goals**: 800
- **Date Range**: May 1, 2005 - March 23, 2023
- **Time Span**: ~18 years of Messi's career
- **Teams**: FC Barcelona, Paris St Germaine and Argentina National Team

## Source

Data was manually transcribed from the YouTube compilation:
[Lionel Messi - All 800 Goals](https://www.youtube.com/watch?v=IscGtF_A14A&t=751s)

A Jupyter notebook (`messi_goals_analysis.ipynb`) with visualization examples is included in this repository.

## Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| `goal_number` | Integer | Sequential goal number (1-800) |
| `date` | Date | Date the goal was scored (YYYY-MM-DD) |
| `team` | String | Team Messi was playing for (FCBarcelona or Argentina) |
| `opponent` | String | Opposing team |
| `competition` | String | Competition code (e.g., LL=La Liga, CL=Champions League, CDR=Copa del Rey) |
| `is_home` | Integer | Home game indicator (1=home, 0=away) |
| `assist_player` | String | Player who provided the assist, or "none" if unassisted |
| `shot_x` | Integer | X-coordinate of shot location on field (see Coordinate System below) |
| `shot_y` | Integer | Y-coordinate of shot location on field (see Coordinate System below) |
| `body_part` | Integer | Body part used (1=Left Foot, 2=Right Foot, 3=Head) |
| `goal_type` | Integer | Type of goal (0=Regular Play, 1=Penalty, 2=Free Kick, 3=Other) |
| `finish_type` | String | Style of finish (e.g., tap-in, chip, header, solo, self rebound) |
| `milestone` | String | Notable milestone markers (if applicable) |

## Coordinate System

The shot coordinates use the **Opta coordinate system**, a standardized soccer pitch coordinate format:

### Coordinate Ranges
- **X-axis (shot_x)**: 0-50 (attacking half of the pitch, left to right)
  - 0 = Halfway line
  - 50 = Goal line
  - ~11-12 = Penalty spot
- **Y-axis (shot_y)**: 0-100 (pitch width, bottom to top)
  - 0 = Bottom touchline
  - 50 = Center of the pitch
  - 100 = Top touchline

### Visualization
The coordinates represent the **attacking direction from left to right**, showing only the half of the pitch where goals are scored.

To visualize these coordinates, you can use the `mplsoccer` library:

```python
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('messi_goals.csv')

# Create pitch (Opta coordinates)
pitch = Pitch(pitch_type='opta', pitch_color='grass', 
              line_color='white', linewidth=2)
fig, ax = pitch.draw(figsize=(16, 10))

# Plot goals
pitch.scatter(df['shot_x'], df['shot_y'], 
              c='white', s=80, alpha=0.8,
              edgecolors='red', linewidth=1, ax=ax)

# Focus on attacking half (left side)
ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

plt.title("Messi's Goals - Shot Locations")
plt.show()
```

### Key Positions
- **Penalty Spot**: Approximately (11-12, 50)
- **Six-yard Box**: X: ~5.5, Y: 37-63
- **Penalty Box**: X: 0-17, Y: 21-79

**Note**: Coordinates are approximate, estimated from video footage. The closer to the goal (higher X values), the more accurate the positioning.

## Competition Codes

- **LL**: La Liga (Spanish League)
- **CL**: UEFA Champions League
- **CDR**: Copa del Rey (Spanish Cup)
- **IF**: International Friendly
- **WCQ**: World Cup Qualifier
- **CA**: Copa America

## Usage Examples

### Installation
For visualization capabilities, install the required packages:
```bash
pip install pandas matplotlib mplsoccer seaborn numpy
```

### Python
```python
import pandas as pd

# Load the dataset
df = pd.read_csv('messi_goals.csv')

# Goals by competition
print(df['competition'].value_counts())

# Goals by year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
print(df['year'].value_counts().sort_index())

# Most common assist providers
print(df['assist_player'].value_counts().head(10))
```

### R
```r
# Load the dataset
df <- read.csv('messi_goals.csv')

# Goals by team
table(df$team)

# Average goals per year
df$year <- format(as.Date(df$date), "%Y")
table(df$year)
```

## Data Collection Methodology

The data was manually transcribed from video footage, capturing:
- Visible information from match footage
- Goal characteristics observable in replays
- Shot coordinates estimated from camera angles
- Assist information when identifiable

**Note**: Some fields contain approximate values due to video limitations. Coordinates are estimated based on visual observation.

## Known Limitations

- Shot coordinates are approximate based on video angles
- Some assist information is marked as "unknown" when not clearly visible
- Body part codes need further documentation
- Goal type codes require standardization
- Messi has scored 50+ additional goals since this dataset's cutoff

## Contributing

This repository is set up to explore Claude Code's capabilities. Feel free to:
- Open issues for data corrections or improvements
- Suggest additional analysis or visualizations
- Propose data enrichment ideas
- Tag @claude in issues to see AI-assisted development in action

## Future Enhancements

Potential additions to explore:
- Goal importance (equalizer, winner, etc.)
- Match final scores
- Tournament stages
- Season information
- Video timestamp links
- Additional statistical analysis
- Interactive visualizations

## License

This dataset is made available for educational and research purposes. The underlying football match data is factual information and not subject to copyright.

## Acknowledgments

- Data source: [Lionel Messi - All 800 Goals](https://www.youtube.com/watch?v=IscGtF_A14A&t=751s), [transfermarkt.us(for assist data)](https://www.transfermarkt.us/)
- Created as a learning project for sports analytics and Claude Code exploration
- Thanks to the football statistics community for inspiration

---

**Note**: This dataset represents the first 800 goals of Messi's career. He has since surpassed 850+ career goals.
