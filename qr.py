import qrcode 
import streamlit as st
from io import BytesIO


st.title("Anything QR 👾")
st.image("C:/Users/raktm/rk/images.png")
up_file=st.file_uploader(" Upload your stuff here (image,pdf,etc.) .", type=None)
txt_inp=st.text_area("Enter your text here.", height=10)

def gen_qr(data):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    return img

if st.button("Generate QR"):
    if up_file:
        f_data=up_file.read()
        q_im=gen_qr(f_data)
        st.success("QR code generated successfully for the file.")
        
    elif txt_inp.strip():
        q_im=gen_qr(txt_inp)
        st.success("QR code generated successfully for the text.")
        
    else:
        st.warning("Please upload a file or enter some text.")
        q_im=None
        
    if q_im:
        buffer=BytesIO()
        q_im.save(buffer, format="PNG")
        st.image(buffer)
        st.download_button("Download QR code", buffer, "QR.png", "image/png")
        
