def recommend_meals(dietary_preferences, meals_df):
    if not dietary_preferences:
        return []
    
    # Boolean filtering: Select meals that match ALL selected dietary tags
    filtered_meals = meals_df
    for pref in dietary_preferences:
        filtered_meals = filtered_meals[filtered_meals['dietary_tags'].str.contains(pref, case=False, na=False)]
    
    # Return list of dictionaries for template rendering
    return filtered_meals[['meal_name', 'ingredients', 'calories']].to_dict('records')