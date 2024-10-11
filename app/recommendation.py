from fastapi import HTTPException
from app.data import users, items


def get_recommendations(user_id: int):
    # Trouver l'utilisateur
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Obtenir les éléments aimés par l'utilisateur
    liked_items = [item for item in items if item["id"] in user["liked_items"]]

    # Extraire les tags des items aimés
    liked_tags = {tag for item in liked_items for tag in item["tags"]}

    # Recommander des items basés sur les tags similaires
    recommendations = [item for item in items if
                       item["id"] not in user["liked_items"] and any(tag in liked_tags for tag in item["tags"])]

    return recommendations
