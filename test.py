import pandas as pd
import streamlit as st
import plotly.express as px
# Load data

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
            
<div class="custom-box">
    <h1>  دور البيانات في تعزيز العمل الخيري </h1>
    <p>تعتمد منصة إحسان على تحليل البيانات لتحديد أكثر المشاريع احتياجًا، وضمان وصول التبرعات بطريقة فعالة.</p>
</div>

            
</body>
</html>
""")
    
    
   

def price_comparison_section(theme):
    """Render the price comparison cards for different property types.
       The apartment card now displays a Plotly bar chart instead of a dummy image.
    """
    st.markdown("# كيف تعكس أرقام إحسان تأثير العمل الخيري؟   ")
    # For the Apartment card, replace the dummy image with a Plotly graph.
    with st.container():
        st.markdown(f"""
        <div class="price-card apartment">
            <h1>أكبر المبالغ تبرعاً</h1>
            <h1 style="color: {theme['accent1']};">من900,000 ر.س الى 1,100,000</h1>
        </div>
        """, unsafe_allow_html=True)

        

    # For the Villa and Land cards, we still use the dummy image.

    with st.container():
        st.markdown(f"""
        <div class="price-card villa">
            <h1>الشركاء الأكثر مشاركة </h1>
            <h1 style="color: {theme['accent2']};">من900,000 ر.س الى 1,100,000</h1>

        </div>
        """, unsafe_allow_html=True)
        


    with st.container():
            st.markdown(f"""
            <div class="price-card land">
                <h1>أعلى عدد مستفيدين</h1>
                <h1 style="color: {theme['accent3']};">من900,000 ر.س الى 1,100,000</h1>
            </div>
            """, unsafe_allow_html=True)
    with st.container():
            st.markdown(f"""
            <div class="price-card 4">
                <h1>أنماط التبرع في رمضان  </h1>
                <h1 style="color: {theme['accent4']};">من900,000 ر.س الى 1,100,000</h1>
            </div>
            """, unsafe_allow_html=True)
            





def recommendation_section(theme):
    """Display recommendations and tips for decision making with enhanced text size."""

    st.html("""<!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <title>بحث عن منزل في الرياض</title>
      <style>
        body {
          font-size: 24px;
          line-height: 1.5;
        }
      </style>
    </head>
    <body>
     <h1> في النهاية، قرار سليمان يعتمد على أولوياته واحتياجاته. هل يفضل المساحة الأكبر والخصوصية التي توفرها الفيلا؟ أم يفضل الموقع الراقي والخدمات المتاحة في الشقة؟ وربما يفكر في شراء أرض وبناء منزله المستقبلي وفقًا لرؤيته الخاصة. مهما كان خياره، الأهم أن يجد المكان الذي يشعر فيه بالراحة والاستقرار. 
    </body>
    </html>
    """)
    st.markdown(f"""
    <div class="recommendation-box" style="font-size: 2rem; padding: 2rem;">
        <h2 style="font-size: 3rem; margin-bottom: 1rem;">💡 نصائح لاتخاذ القرار</h2>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
            <div style="border-left: 3px solid {theme['accent1']}; padding-left: 1rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;">العوامل المهمة:</h3>
                <p style="font-size: 2rem; line-height: 1.5; margin: 0;">
                    <strong>✓ قرب الخدمات الأساسية</strong><br>
                    <strong>✓ جودة البناء</strong><br>
                    <strong>✓ مستقبل المنطقة</strong>
                </p>
            </div>
            <div style="border-left: 3px solid {theme['accent2']}; padding-left: 1rem;">
                <h3 style="font-size: 2.2rem; margin-bottom: 0.5rem;">التوصيات:</h3>
                <p style="font-size: 2rem; line-height: 1.5; margin: 0;">
                    <strong>✓ زيارة الموقع شخصيًا</strong><br>
                    <strong>✓ دراسة خيار التمويل</strong><br>
                    <strong>✓ مقارنة عروض مختلفة</strong>
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



def main():
    st.set_page_config(layout="wide", page_title="رحلة البحث عن منزل")

    # Pastel theme configuration
    pastel_theme = {
        "background": "#d2d6d9",
        "text_color": "#595959",
        "accent1": "#b58900",
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