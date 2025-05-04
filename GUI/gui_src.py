import  streamlit as st  
def main():
    st.set_page_config(page_title="PDF RAG Explorer", layout="wide")
    
    # Αρχικοποίηση session state
    if 'rag' not in st.session_state:
        st.session_state.rag = None
    if 'docs_processed' not in st.session_state:
        st.session_state.docs_processed = False
    
    st.session_state.docs_processed = True
    # Στήλη για φόρτωση εγγράφων
    # with st.sidebar:
    #     st.header("File mngmnt")
    #     uploaded_files = st.file_uploader(
    #         "Upload PDF files",
    #         type="pdf",
    #         accept_multiple_files=True,
    #         help="Chhoose up to 5 PDF files for processing.",
    #     )

    #     if uploaded_files and len(uploaded_files) > 0:
    #         if st.button("Pdf processing") and len(uploaded_files) <=5:
    #             with st.spinner("Processing documents please wait."):
    #                 try:
    #                     #st.session_state.rag = RagSystem(uploaded_files)
    #                     st.session_state.docs_processed = True
    #                     st.success("Work done!")
    #                 except Exception as e:
    #                     st.error(f"Error with code: {str(e)}")
    #         elif len(uploaded_files) >5:
    #             st.warning("Max 5 files!!!!") 
##Θωρώ οτι είναι ετοιμο db
    st.title("🔍 PDF smart search")
    #st.session_state.rag = RagSystem()


    if st.session_state.docs_processed:
        query = st.text_input("", placeholder="")
        
        if st.button("Search") and query:
            with st.spinner("On going query..."):
                try:
                    results = st.session_state.rag.search(query)
                    
                    st.subheader("📌 Search results")
                    for i, result in enumerate(results[:5]):  
                        with st.expander(f"Extract {i+1} | SRC: {result['source']}"):
                            st.markdown(f"**Score:** {result['score']:.2f}")
                            st.markdown(f"**Text:**\n{result['chunk']}")
                            st.markdown(f"**Page:** {result['page']}") 
                except Exception as e:
                    st.error(f"Error with code: {str(e)}")

        

    else:
        st.info("Please upload PDF files to start searching.")
if __name__ == "__main__":
    main()
