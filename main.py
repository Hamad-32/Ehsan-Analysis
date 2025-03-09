import streamlit as st


st.markdown(
    """
    <style>

        .stApp {
            background-color: #eae2d9; /* Light gray */
            direction: rtl;

        }
        [data-testid="stSidebar"] {
            background-color: #464d70; /* Dark Blue-Gray */
        
    </style>
    """,
    unsafe_allow_html=True
)

# def load_css():
#     with open("css/main.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Apply CSS
# load_css()



st.markdown(
    """
    <style>
        .custom-image{
            border-radius: 10px; /* Adjust border radius */
            width: 120%; /* Increase width, adjust as needed */
            border-radius: 30px;
            display: block;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the image with a custom class
st.markdown('<img src="https://ehsansocialimages.s3.me-south-1.amazonaws.com/social-projects.png" class="custom-image">', unsafe_allow_html=True)




st.markdown(
    """ 
    
    <div class="head-div"">
    <h3> منصة إحسان عطاء دائم</h3>
    <h5>         في البداية انا حمد حديث تخرج وابحث عن وظيفة مناسبة لي ولكن مااعرف كيف ابدا ماعرف ايش المهارات الي احتاج اطورها؟ او حتى اللغات الي لازم اتقنها ف قررت اجمع البيانات وابدا احللها عشان احصل إجابات وافيه وكافيه</h5>
    </div>


    <div class="head-div">

    <h4> تعال معي خلني اوريك اكثر الوظائف المطروحه على المنصه الوطنية جدارات حسب مناطق المملكة</h4>
    </div>

        """,

        unsafe_allow_html=True

)


