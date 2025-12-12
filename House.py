import streamlit as st

st.markdown("## Welcome Delaney Carr")
st.markdown("### Click to access your schedule")


if st.button("Open spring 2026 file"):
    pdf_path = "PDF_DelaneyCarr_Transcript_25_26.pdf"  # Ensure the file name is correct and exists in the directory
    
    # Display the PDF in Streamlit
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="Download the schedule",
            data=pdf_file,
            file_name=pdf_path,
            mime="application/pdf"
        )
    st.markdown("### The file has been loaded. You can also download it above.")