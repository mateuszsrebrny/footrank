from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List, Dict

app = FastAPI()


app = FastAPI()

# Placeholder for rankings data (would typically be retrieved from a database or an API)
rankings_data = {
    "current": [
        {"nation": "Spain", "points": 1000},
        {"nation": "Germany", "points": 950},
        {"nation": "France", "points": 925},
        {"nation": "England", "points": 900},
    ],
    "previous": [
        {"nation": "Spain", "points": 1000},
        {"nation": "Germany", "points": 950},
        {"nation": "France", "points": 920},
        {"nation": "England", "points": 905},
    ]
}

@app.get("/rankings", response_model=List[Dict])
def get_current_rankings():
    """
    Fetch current national rankings of European football nations.
    """
    try:
        return sorted(rankings_data["current"], key=lambda x: x['points'], reverse=True)
    except Exception:
        raise HTTPException(status_code=500, detail="Rankings data is unavailable.")


@app.get("/rankings/changes", response_model=List[Dict])
def get_ranking_changes():
    """
    Compare and show changes in rankings after a round of games.
    """
    try:
        previous_rankings = rankings_data["previous"]
        current_rankings = rankings_data["current"]

        # Generate a list of rankings changes
        changes = []
        for i, current in enumerate(current_rankings):
            previous = next((team for team in previous_rankings if team['nation'] == current['nation']), None)
            if previous:
                change = current['points'] - previous['points']
                changes.append({
                    "nation": current['nation'],
                    "previous_points": previous['points'],
                    "current_points": current['points'],
                    "change": change,
                    "arrow": "up" if change > 0 else "down" if change < 0 else "no change"
                })

        return changes
    except Exception:
        raise HTTPException(status_code=500, detail="Error retrieving ranking changes.")

@app.get('/')
def hello_world():
    return "<html><body><b>Hello,World</b></body></html>"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)


