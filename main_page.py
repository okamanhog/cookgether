import streamlit as st
from streamlit_option_menu import option_menu
from src.community_new import submit_recipe, show_community_recipes
from src.recipe_generator import recipe_generator_page
from src.food_share import submit_food_share, show_food_shares
from src.user_profile import user_profile_page
from src.about import about_page
from streamlit_lottie import st_lottie
import time

# REMOVE THIS CODE
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
###

def main():
    st_lottie_url = "https://lottie.host/5e40c7d4-3253-4ac8-9a96-4a3575da91f5/V4LHvS4XDN.json"

    # Show Lottie animation
    animation_placeholder = st.empty()
    st_lottie(st_lottie_url,height=100,width=100)

    # Simulate animation time (you can adjust this based on the actual animation duration)
    #time.sleep(1)  # Adjust the sleep duration based on your animation length

    # Clear the animation and show the main page
    animation_placeholder.empty()
    main_page()

def main_page():
    with st.sidebar:
        choice = option_menu("Cookgether",
                             ["🥘  Community",
                              "🗒️  AI Recipe Generator",
                              "🍎  Food Share",
                              "😀  Profile",
                              "📌  About"],
                             # create a menu bar
                                menu_icon="house", default_index=0)


    #if else statement to go to different pages
    #the page Community
    if choice =="🥘  Community":
        submit_recipe()
        show_community_recipes()


    #the page AI Recipe Generator
    elif choice =="🗒️  AI Recipe Generator":
        #login_page()
        recipe_generator_page()
        #collect_user_inputs()
        #generate_and_display_recipe(user_inputs)
        #update_database_with_recipe(ingredients, recipe_name, recipe_output, user_inputs)
        #recipe_generator_page()

    #the page Food Share
    elif choice =="🍎  Food Share":
        submit_food_share()
        show_food_shares()

    #the page Food Share
    elif choice =="😀  Profile":
        user_profile_page()


    #the page About
    elif choice =="📌  About":
        about_page()

if __name__ == "__main__":
    main()
