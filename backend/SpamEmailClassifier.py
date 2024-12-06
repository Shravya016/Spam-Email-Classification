import streamlit as st
import pickle

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

def main():
    st.title("Email Spam Classification Application")
    st.markdown("""
        This is a **Machine Learning** application to classify emails as **Spam** or **Ham**.
        Enter an email message in the text area and click **Classify** to determine if it's spam or not.
    """)

    st.subheader("Email Classification")
    user_input = st.text_area("Enter an email to classify", height=150, max_chars=5000)

    if st.button("Classify"):
        if user_input:
            with st.spinner('Classifying your email...'):
                data = [user_input]
                vect = cv.transform(data)
                result = model.predict(vect)
                if result[0] == 0:
                    st.success("✅ This is **Not A Spam Email**")
                else:
                    st.error("❌ This is **A Spam Email**")
        else:
            st.warning("Please enter an email to classify.")
            
    st.markdown("""
        **What is Spam?**
        
        Spam refers to unwanted, unsolicited emails often sent in bulk to a large number of users.
        It usually includes promotional content, phishing attacks, or other types of malicious communication.
    """)

if __name__ == "__main__":
    main()
