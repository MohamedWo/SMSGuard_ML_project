import streamlit as st
import pickle

# --- تحميل الموديل ---
with open("spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# --- واجهة التطبيق ---
st.title("📩 SMS Spam Detection App")
st.write("أدخل رسالة وسيقوم النموذج بتحديد ما إذا كانت Spam أم Ham")

# إدخال المستخدم
user_input = st.text_area("اكتب الرسالة هنا:")

# زر التنبؤ
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("من فضلك اكتب رسالة أولاً")
    else:
        # تحويل النص
        input_vect = vectorizer.transform([user_input])
        prediction = model.predict(input_vect)[0]

        # إظهار النتيجة
        if prediction == "spam":
            st.error("🚨 النتيجة: الرسالة **Spam** ❌")
        else:
            st.success("✅ النتيجة: الرسالة **Ham** (غير مزعجة)")
# python -m streamlit run SMS.py
