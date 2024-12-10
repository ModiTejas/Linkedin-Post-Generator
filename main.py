import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    # Styled header
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>LinkedIn Post Generator 🚀</h1>",
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px; color: #555;'>Effortlessly create engaging posts for LinkedIn in just a few clicks!</p>",
                unsafe_allow_html=True)
    st.markdown("<hr style='border:2px solid #bbb; margin:10px 0;'>",
                unsafe_allow_html=True)

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        # Dropdown for Topic (Tags) with compact styling
        st.markdown("<p style='font-size:18px; color:#3498db; margin-bottom:2px;'>📝 <b>Topic:</b></p>",
                    unsafe_allow_html=True)
        selected_tag = st.selectbox("", options=tags)
        st.markdown("<p style='font-size:12px; color:gray;'>Select the theme or topic for your post.</p>",
                    unsafe_allow_html=True)

    with col2:
        # Dropdown for Length with compact styling
        st.markdown("<p style='font-size:18px; color:#28a745; margin-bottom:2px;'>⏳ <b>Length:</b></p>",
                    unsafe_allow_html=True)
        selected_length = st.selectbox("", options=length_options)
        st.markdown("<p style='font-size:12px; color:gray;'>Choose the post length: Short, Medium, or Long.</p>",
                    unsafe_allow_html=True)

    with col3:
        # Dropdown for Language with compact styling
        st.markdown("<p style='font-size:18px; color:#9b59b6; margin-bottom:2px;'>🌐 <b>Language:</b></p>",
                    unsafe_allow_html=True)
        selected_language = st.selectbox("", options=language_options)
        st.markdown("<p style='font-size:12px; color:gray;'>Pick the language: English or Hinglish.</p>",
                    unsafe_allow_html=True)

    # Generate Button with styling
    st.markdown("<div style='text-align: center; margin-top:20px;'>",
                unsafe_allow_html=True)
    if st.button("✨ Generate Post ✨"):
        # Generate and display the post
        post = generate_post(selected_length, selected_language, selected_tag)
        st.markdown("<hr style='border:1px solid #ccc; margin:20px 0;'>",
                    unsafe_allow_html=True)

        # Output section without the "Your Generated Post" line
        st.markdown(f"""
            <div style='
                padding:10px; 
                border-radius:10px; 
                background-color:rgba(255, 255, 255, 0.1); 
                color:inherit;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
                <p style='font-size:16px;'>{post}</p>
            </div>
        """, unsafe_allow_html=True)

    # Footer for branding
    st.markdown("<hr style='border:2px solid #bbb; margin:20px 0;'>",
                unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()
