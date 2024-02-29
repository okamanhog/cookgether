import streamlit as st
from src.community_recipe import community_recipe
from src.community_upload import community_upload

#a list of the recipe names as captions
recipe_name = ['Mushroom and Cheese Stuffed Omelette',
                   'Roasted Carrot and Tomato Soup',
                   'Caprese Salad with Tomatoes and Cheese',
                   'Mushroom and Cheese Stuffed Omelette',
                   'Roasted Carrot and Tomato Soup',
                   'Caprese Salad with Tomatoes and Cheese',
                    'Mushroom and Cheese Stuffed Omelette',
                   'Roasted Carrot and Tomato Soup',
                   'Caprese Salad with Tomatoes and Cheese'
                   ]
#a list of the image path for uploading the image
#image_path = ['https://www.cuisinefiend.com/RecipeImages/Cheese%20and%20mushroom%20omelette/cheese-and-mushroom-omelette-2-768.jpg',
                  #'https://i0.wp.com/healthylittlevittles.com/wp-content/uploads/2021/09/Roasted-Tomato-Carrot-Soup-5.jpg?w=800&ssl=1']


def community_page():
    # Define the number of columns and rows
    num_columns = 3
    num_rows = len(recipe_name) // num_columns + (len(recipe_name) % num_columns > 0)

    for row in range(num_rows):
        recipe_columns = st.columns(num_columns)

        for col in range(num_columns):
            recipe_index = row * num_columns + col
            if recipe_index < len(recipe_name):
                with recipe_columns[col]:
                    st.write(recipe_name[recipe_index])
                    #file_path = image_path[recipe_index]
                    #food_image = st.image(file_path, caption=recipe_name[recipe_index])


