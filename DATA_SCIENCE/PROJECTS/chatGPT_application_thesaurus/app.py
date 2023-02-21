import streamlit as st
import json

st.set_page_config(page_title="ChatGPT Explanations - Data Science Terms",
                    page_icon=":speech_bubble:",
                    layout="wide")

in_file = "explanations.json"

@st.cache
def get_json_data(input_name):
    """Return python dict of dicts from json"""

    with open(input_name, "r") as f:
        data = json.load(f)
    
    return data

data_dict = get_json_data(in_file)

st.sidebar.header("Selection tools: ")

key_term = st.sidebar.selectbox(
    "Select a term to define:  ",
    options=data_dict.keys()
)

curr_dict = data_dict[key_term]
basic_explanation=curr_dict["exp_short"]
simple_explanation=curr_dict["exp_5yo"]
expert_explanation=curr_dict["exp_expert"]

st.markdown("## ChatGPT Explanations for Data Science Interviews")
st.markdown(f"### Key Term: {key_term}")
st.markdown(f"""
    #### Standard Explanation: \n
    {basic_explanation}
""")

left_column, right_column = st.columns(2)



with left_column:
    st.subheader(":boy: ELI5 Explanation")
    st.markdown(f"{simple_explanation}")

with right_column:
    st.subheader(":older_man: Expert Explanation")
    st.markdown(f"{expert_explanation}")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)