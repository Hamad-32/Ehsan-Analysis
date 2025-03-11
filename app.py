import requests
import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from pathlib import Path

def predict_api(value1, value2, value3, value4):
    url = "https://ehsan-ld2g.onrender.com/predict"
    payload = {
        "Number_of_donations": value1,
        "Beneficiaries": value2,
        "Location_encoded": value3,
        "Hijri_Month": value4
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("prediction", "لا يوجد توقع متاح")
        else:
            return f"خطأ في الاستجابة: {response.status_code}"
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

def main():
    st.set_page_config(layout="wide", page_title="منصة إحسان")
    
    st.markdown("---")
    st.markdown("<h1 style='text-align: center; color: black;'>أدخل القيم للتنبؤ</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        input1 = st.text_input("القيمة الأولى", placeholder="أدخل القيمة الأولى")
        input2 = st.text_input("القيمة الثانية", placeholder="أدخل القيمة الثانية")
    with col2:
        input3 = st.text_input("القيمة الثالثة", placeholder="أدخل القيمة الثالثة")
        input4 = st.text_input("القيمة الرابعة", placeholder="أدخل القيمة الرابعة")
    
    if st.button("تنبؤ", key="predict_button"):
        if input1 and input2 and input3 and input4:
            try:
                value1 = float(input1)
                value2 = float(input2)
                value3 = float(input3)
                value4 = float(input4)
                prediction = predict_api(value1, value2, value3, value4)
                st.success(f"نتيجة التنبؤ: {prediction}")
            except ValueError:
                st.error("الرجاء إدخال قيم رقمية صحيحة.")
        else:
            st.warning("الرجاء ملء جميع الحقول.")

if __name__ == "__main__":
    main()
