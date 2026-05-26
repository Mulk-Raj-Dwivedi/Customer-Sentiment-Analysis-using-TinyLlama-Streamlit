# app.py

import streamlit as st
import pandas as pd
import json
import tempfile
import os
import glob

#########################################################
# IMPORT FUNCTIONS FROM YOUR EXISTING FILE
#########################################################

from voc_extract_sentiment_test import (

    _extract_transcript_text,
    extract_customer_only_text,
    generator
)

#########################################################
# PAGE CONFIG
#########################################################

st.set_page_config(
    page_title="Customer Sentiment Analysis",
    page_icon="💬",
    layout="wide"
)

#########################################################
# TITLE
#########################################################

st.title("💬 Customer Sentiment Analysis")
st.markdown(
    "Upload transcript JSON files to predict customer sentiment."
)

#########################################################
# FILE UPLOADER
#########################################################

uploaded_files = st.file_uploader(
    "Upload Transcript JSON Files",
    type=["json"],
    accept_multiple_files=True
)

#########################################################
# PROCESS BUTTON
#########################################################

if st.button("Run Sentiment Analysis"):

    if not uploaded_files:
        st.warning("Please upload transcript JSON files.")
        st.stop()

    results = []

    progress_bar = st.progress(0)

    #####################################################
    # PROCESS EACH FILE
    #####################################################

    for idx, uploaded_file in enumerate(uploaded_files):

        try:

            #################################################
            # LOAD JSON
            #################################################

            transcript_data = json.load(uploaded_file)

            #################################################
            # EXTRACT TRANSCRIPT
            #################################################

            full_transcript = _extract_transcript_text(
                transcript_data
            )

            #################################################
            # EXTRACT CUSTOMER TEXT
            #################################################

            customer_text = extract_customer_only_text(
                full_transcript
            )

            #################################################
            # SKIP EMPTY
            #################################################

            if not customer_text.strip():

                sentiment = "No Customer Text"

            else:

                #################################################
                # PROMPT
                #################################################

                prompt = f"""
You are a sentiment analysis system.

Analyze ONLY the CUSTOMER conversation.

Classify the OVERALL customer sentiment.

Rules:

- Negative:
customer is angry, frustrated, upset,
complaining, dissatisfied, disappointed,
threatening escalation, or unhappy.

- Neutral:
customer is asking questions calmly
without strong emotion.

- Positive:
customer is happy, satisfied,
appreciative, thankful, or pleased.

Return ONLY ONE WORD:

Positive
Neutral
Negative

Customer Conversation:
{customer_text}

Sentiment:
"""

                #################################################
                # MODEL INFERENCE
                #################################################

                response = generator(
                    prompt,
                    max_new_tokens=5,
                    do_sample=False,
                    temperature=0.0
                )

                #################################################
                # CLEAN OUTPUT
                #################################################

                generated_text = response[0][
                    "generated_text"
                ]

                generated_text = generated_text.replace(
                    prompt,
                    ""
                ).strip()

                #################################################
                # FINAL SENTIMENT
                #################################################

                valid_sentiments = [
                    "Positive",
                    "Neutral",
                    "Negative"
                ]

                sentiment = "Unknown"

                for item in valid_sentiments:

                    if item.lower() in generated_text.lower():

                        sentiment = item
                        break

            #################################################
            # METADATA
            #################################################

            metadata = transcript_data.get(
                "metadata",
                {}
            )

            call_id = metadata.get(
                "call_id",
                uploaded_file.name
            )

            #################################################
            # STORE RESULTS
            #################################################

            results.append({

                "call_id": call_id,

                "file_name": uploaded_file.name,

                "customer_sentiment": sentiment,

                "customer_text": customer_text
            })

        except Exception as e:

            results.append({

                "call_id": "ERROR",

                "file_name": uploaded_file.name,

                "customer_sentiment": f"ERROR: {str(e)}",

                "customer_text": ""
            })

        #####################################################
        # UPDATE PROGRESS
        #####################################################

        progress_bar.progress(
            (idx + 1) / len(uploaded_files)
        )

    #########################################################
    # CREATE DATAFRAME
    #########################################################

    df = pd.DataFrame(results)

    #########################################################
    # DISPLAY RESULTS
    #########################################################

    st.success("Sentiment Analysis Completed!")

    st.dataframe(
        df,
        use_container_width=True
    )

    #########################################################
    # DOWNLOAD CSV
    #########################################################

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="Download Results CSV",

        data=csv,

        file_name="sentiment_results.csv",

        mime="text/csv"
    )