import streamlit as st
import google.generativeai as genai

   
# PAGE CONFIG
   

st.set_page_config(
    page_title="AI Policy Advisor",
    page_icon="🧠",
    layout="wide"
)

   
# GEMINI CONFIG
   

genai.configure(
    api_key="AQ.Ab8RN6I5LDpZMawhq21LndC30-NDGDnW9d1Ku7jHeH41UHEiEw"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

   
# PAGE HEADER
   

st.title(" AI Policy Advisor")

st.write(
    """
    This module uses Generative AI to provide policy insights
    related to innovation, patents, R&D investment,
    FDI inflows, trade openness, and economic development.
    """
)

st.divider()

   
# QUESTION INPUT
   

question = st.text_area(
    "Enter Your Policy Question",
    height=150,
    placeholder="Example: How can India increase patent generation by 20%?"
)

   
# GENERATE RESPONSE
   

if st.button("🚀 Generate Policy Advice"):

    if question.strip() == "":
        st.warning("Please enter a policy question.")
    else:

        try:

            with st.spinner("Generating AI response..."):

                prompt = f"""
                You are an innovation policy expert.

                Project Context:
                This project focuses on:

                - Patent Generation
                - Innovation Policy
                - R&D Investment
                - Foreign Direct Investment
                - Trade Openness
                - Digital Infrastructure
                - Innovation-led Economic Growth

                User Question:
                {question}

                Give the answer in the following format:

                1. Analysis
                2. Key Policy Actions
                3. Expected Benefits

                Keep the answer concise and practical.
                """

                response = model.generate_content(
                    prompt
                )

                st.subheader("📋 AI Policy Analysis")

                st.write(response.text)

        except Exception as e:

            st.error(
                f"Error: {e}"
            )


# SAMPLE QUESTIONS


st.divider()

st.subheader("Sample Questions")

st.markdown("""
- How can India increase patent generation by 20%?
- What is the role of R&D investment in innovation growth?
- How can FDI improve technological innovation?
- What policies can strengthen India's innovation ecosystem?
- How does digital infrastructure affect innovation performance?
""")