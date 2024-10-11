from fastapi import FastAPI
from app.recommendation import get_recommendations

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the recommendation API"}

@app.get("/recommend/{user_id}")
def recommend_items(user_id: int):
    recommendations = get_recommendations(user_id)
    return recommendations