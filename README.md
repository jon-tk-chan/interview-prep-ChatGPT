# interview-prep-ChatGPT
App for displaying data science concepts and explanations from ChatGPT. Responses are contained in `explanations.json` and were created using ChatGPT using `make_explanations.py` script to read in key terms from `data/key_terms.csv`.

Usage: for job interview prep, for personal learning, for understanding ChatGPT workflow

![](https://github.com/jon-tk-chan/interview-prep-ChatGPT/blob/main/media/demo.gif)

Link to app (Hosted on Streamlit Community Cloud): https://jon-tk-chan-interview-prep-chatgpt-app-dpquof.streamlit.app/

Note: ChatGPT explanations were generated using author's API key and stored as a static json file to reduce time and ensure functionality even when ChatGPT is inaccessible. Additional terms will be added by author and Cloud app will be updated as author sees fit.

FOR AUTHOR: 

To update explanations:

1. in excel, add terms to `data/key_terms.csv` (keyTerms column nec cessary)
2. in terminal: `python make_explanations.py` (takes a while to run)
3. in terminal: `streamlit run app.py` 
4. in web browser, access app at: http://localhost:8501

(for Streamlit Community Cloud version, commit and push updated `explanations.json` to this repo, access the app using the above link, click on 'manage app' in bottom right corner, select 'reboot app')