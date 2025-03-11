import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from pathlib import Path

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("model_ehsan.csv")

def creat_model_charts():
    X4 = load_data()

    fig = px.scatter_3d(
        X4,  # Use only the first 10 rows for testing
        x='Beneficiaries', 
        y='Location_encoded', 
        z='Hijri_Month',
        color='y_pred_4',
        color_continuous_scale=px.colors.sequential.Viridis,  # Add color scale
        title="3D Scatter Plot of Beneficiaries, Location, and Hijri Month"
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),  # Adjust margins
        scene=dict(
            xaxis_title="Beneficiaries",
            yaxis_title="Location Encoded",
            zaxis_title="Hijri Month"
        )
    )
    return fig

def creat_model_charts1():
    X4 = load_data()

    fig = px.scatter_3d(
        X4,  # Use only the first 10 rows for testing
        x='Number of donations', 
        y='Location_encoded', 
        z='Beneficiaries',
        color='y_pred_4',
        color_continuous_scale=px.colors.sequential.Viridis,  # Add color scale
        title="3D Scatter Plot of Beneficiaries, Location, and Hijri Month"
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),  # Adjust margins
        scene=dict(
            xaxis_title="Beneficiaries",
            yaxis_title="Location Encoded",
            zaxis_title="Hijri Month"
        )
    )
    return fig

def load_css(theme):
    """Load custom CSS with colors defined by the chosen theme."""
    custom_css = f"""
    <style>
        .stApp {{
            background: {theme['background']};
            text-align: right;
            direction: rtl;
            color: {theme['text_color']};
        }}
        h1, h2, h3 {{
            font-family: {theme['header_font']};
            color: {theme['text_color']};
        }}
        /* Hero Section Styling */
        .hero {{
            background: linear-gradient({theme['hero_overlay']}, {theme['hero_overlay']}), 
                        url('https://albiladdaily.com/wp-content/uploads/2021/04/%D9%85%D9%86%D8%B5%D8%A9-%D8%A7%D8%AD%D8%B3%D8%A7%D9%86-1170x594.jpg') center/cover;
            padding: 4rem 2rem;
            border-radius: 30px;
            margin: 2rem 0;
            height: 500px;
        }}
        /* Price Card Styling */
        .price-card {{
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-right: 5px solid;
            color: {theme['text_color']};
        }}
        .price-card.apartment {{ border-color: {theme['accent1']}; }}
        .price-card.villa {{ border-color: {theme['accent2']}; }}
        .price-card.land {{ border-color: {theme['accent3']}; }}
        .price-card.4 {{ border-color: {theme['accent4']}; }}
        /* Comparison Box Styling */
        .comparison-box {{
            background: linear-gradient(135deg, #ffffff 0%, {theme['background']} 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid #e9ecef;
        }}
        /* Recommendation Box Styling */
        .recommendation-box {{
            background: {theme['recommendation_bg']};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            margin: 2rem 0;
        }}
        /* Example Section Styling */
        .example-section {{
            margin-top: 3rem;
            font-size: 1.8rem;
            line-height: 1.7;
        }}
        .example-section h2 {{
            font-size: 2.4rem;
            margin-bottom: 1rem;
            color: {theme['text_color']};
        }}
        .highlight {{
            font-weight: bold;
            color: {theme['accent1']};
            font-size: 1.9rem;
        }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def hero_section(theme):
    """Display the hero section with background image and title."""
    hero_html = f"""
    <div class="hero">
        
       
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def info_sections():
    """Show information sections explaining the choices and add dummy graph images."""
    st.html("""<!DOCTYPE html>
<html lang="ar">

<body>

            
<title> عن إحسان   </title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 18px;
            line-height: 1.6;
            background-color: #f8f9fa;
            margin: 20px;
            text-align: right;
            direction: rtl;
        }
        .custom-box {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-right: 5px solid #579091;
            color: #657b83;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .custom-box h1 {
            color: #579091;
            font-size: 35px;
            margin-bottom: 10px;
            border-bottom: 2px solid #579091;
            padding-bottom: 5px;
            display: inline-block;
        }
        .custom-box p {
            font-size: 30px;
            color: #444;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="custom-box">
    <h1> عن إحسان </h1>
    <p>إحسان منصة وطنية تدعم العمل الخيري باستخدام التقنية والذكاء الاصطناعي، بهدف توصيل التبرعات لمستحقيها بأفضل طريقة. تأسست بأمر سامي لتكون حلقة وصل بين المتبرعين والمشاريع المحتاجة، مما يعزز الشفافية والأثر الإيجابي.</p>
</div>

<div class="custom-box">
    <h1>تعودوا الخير فإن الخير عادة</h1>
    <p>  اهلاً انا اسمي "فهد"، اعمل متطوعًا في منصة إحسان, احب أن ادرس البيانات واحللها لأفهم كيف يمكن للخير أن ينتشر بشكل أكبر من خلال طرح المشاريع الخيرية والتنموية.</p>
    
</div>
            
</body>
</html>
""")

def price_comparison_section(theme):
    """Render the price comparison cards for different property types.
       The apartment card now displays a Plotly bar chart instead of a dummy image.
    """
    # Model Charts
    st.markdown("# كيف تعكس أرقام إحسان تأثير العمل الخيري؟   ")
    with st.container():
        st.markdown("", unsafe_allow_html=True)
        st.plotly_chart(creat_model_charts(), use_container_width=True) 
   # fig = creat_model_charts()
   # fig.show()
    

    with st.container():
        st.markdown("", unsafe_allow_html=True)
        st.plotly_chart(creat_model_charts1(), use_container_width=True) 

    with st.container():
        # Open the container with HTML
        st.markdown(f"""
        <div class="price-card apartment">
            <h1>الرؤى</h1>
            <h1 style="color: {theme['accent2']};">تحليل مجموعات مشاريع إحسان</h1>
            <div style="font-size: 24px; line-height: 1.8; margin-top: 20px; color: black;">
        """, unsafe_allow_html=True)

        # Add the content using Markdown (no HTML)
        st.markdown("""
        <p style="font-size: 24px; color: #8A2BE2; font-weight: bold;"> المجموعة الأولى _0 (البنفسج):</p>  
        - تمثل مشاريع إحسان من بداية 2024 وحتى الآن.  
        - موزعة على جميع المناطق.  
        - عدد المستفيدين أقل من ١٠٠ ألف.  
        - عدد المتبرعين لا يتجاوز 64 ألف.  

        <p style="font-size: 24px; color: #FF69B4; font-weight: bold;"> المجموعة الثانية _1 (الوردي):</p>  
        - تمثل مشاريع إحسان في مكة المكرمة والمدينة خلال الأشهر 5 حتى 12.  
        - عدد المتبرعين لا يتجاوز 64 ألف.  
        - عدد المستفيدين ما بين 240 ألف و 320 ألف.  

        <p style="font-size: 24px; color: #FFA500; font-weight: bold;"> المجموعة الثالثة _2 (البرتقالي):</p>  
        - تمثل مشاريع إحسان في مكة المكرمة خلال الأشهر 8 حتى 12.  
        - عدد المتبرعين لا يتجاوز 53 ألف.  
        - عدد المستفيدين بين 500 ألف و 600 ألف.  

        <p style="font-size: 24px; color: #FFFF00; font-weight: bold;"> المجموعة الرابعة _3 (الأصفر):</p>  
        - تمثل مشاريع إحسان في مكة المكرمة خلال الأشهر 7 حتى 10.  
        - عدد المتبرعين لا يتجاوز 25 ألف.  
        - عدد المستفيدين غير محدد.  
        """, unsafe_allow_html=True)

        # Close the HTML div
        st.markdown("""
            </div>
        </div>
        """, unsafe_allow_html=True)

   # Add a new section for user input and prediction
    st.markdown("---")  # Add a horizontal line for separation
    st.markdown("<h1 style='text-align: center; color: black;'>أدخل القيم للتنبؤ</h1>", unsafe_allow_html=True)

    # Create four text input fields
    col1, col2 = st.columns(2)  # Split the layout into two columns

    with col1:
        input1 = st.text_input("القيمة الأولى", placeholder="أدخل القيمة الأولى")
        input2 = st.text_input("القيمة الثانية", placeholder="أدخل القيمة الثانية")

    with col2:
        input3 = st.text_input("القيمة الثالثة", placeholder="أدخل القيمة الثالثة")
        input4 = st.text_input("القيمة الرابعة", placeholder="أدخل القيمة الرابعة")

    # Add a button for prediction
    if st.button("تنبؤ", key="predict_button"):
        # Validate inputs
        if input1 and input2 and input3 and input4:
            try:
                # Convert inputs to numeric values (if needed)
                value1 = float(input1)
                value2 = float(input2)
                value3 = float(input3)
                value4 = float(input4)

                # Perform prediction (replace this with your actual prediction logic)
                prediction = value1 + value2 + value3 + value4  # Example logic
                st.success(f"نتيجة التنبؤ: {prediction}")
            except ValueError:
                st.error("الرجاء إدخال قيم رقمية صحيحة.")
        else:
            st.warning("الرجاء ملء جميع الحقول.")

def recommendation_section(theme):
    """Display recommendations and tips for decision making with enhanced text size."""
    # Load the image and convert it to base64
    image_path = Path(r"C:\Users\sulta\Downloads\qr.png")  # Use raw string for path
    if image_path.exists():
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    else:
        st.error("Image file not found!")
        return

    st.markdown(f"""
    <div class="recommendation-box" style="font-size: 2rem; padding: 2rem;">
        <h2 style="font-size: 3rem; margin-bottom: 1rem;">وجبات الإفطار لضيوف الرحمن</h2>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
            <!-- Text on the left -->
            <div style="border-left: 3px solid {theme['accent1']}; padding-left: 1rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;"></h3>
                <p style="font-size: 2rem; line-height: 1.5; margin: 0;">
                    <strong>✓ رقم الحالة : P49680</strong><br>
                </p>
            </div>
            <!-- Image on the right -->
            <div style="border-left: 3px solid {theme['accent2']}; padding-left: 1rem;">
                <img src="data:image/png;base64,{encoded_image}" alt="وجبات الإفطار" style="width: 100%; border-radius: 15px;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="   منصة إحسان")

    # Pastel theme configuration
    pastel_theme = {
        "background": "#d2d6d9",
        "text_color": "#595959",
        "accent1": "#61898e",
        "accent2": "#cb4b16",
        "accent3": "#268bd2",
        "accent4": "#268bd2",
        "hero_overlay": "rgb(201 201 201 / 40%)",
        "header_font": "'Tajawal', sans-serif",
        "recommendation_bg": "#657b83",
    }

    theme = pastel_theme

    load_css(theme)
    hero_section(theme)
    info_sections()
    price_comparison_section(theme)
    recommendation_section(theme)

 

if __name__ == "__main__":
    main()
