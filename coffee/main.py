import streamlit as st
from database import create_connection, create_tables, dump

conn = create_connection
create_tables(conn)
st.header("This is homepage")
st.image('images/Ripple Orange/orange.jpg')
colm1, colm2, colm3 = st.columns(3)

with colm1:
        st.image('images/Ripple Orange/orange.jpg')
        buy = st.button('buy me')
# with colm2:
#         st.image('images/Ripple Blue/blue.jpg')
#         buyy = st.button('buy me')
# with colm3:
#         st.image('images/Ripple Red/red.jpg', caption='red coffee')
#         buyyy = st.button('buy me')
# with st.form:
#     username = st.input_text("Username")
#     password = st.input_text("Password", type="password")
#     login_button = st.button("Login")
#     if login_button:
#             st.success("Login successful!")
#             st.rerun()
#     else:
#             st.error("Invalid username or password")

# tabl, tab2 = st.tabs(["Login", "Register"])
# with tabl:
#         # username = st.text_input("Username")
#         # password = st.text_input("Password", type="password")
#         # login_button = st.button("Login")
#        pass
        
# with tab2:
#         conn = create_connection()
#         username = st.text_input("Username")
#         password = st.text_input('Password')
#         email = st.text_input('Email')
#         register_button = st.button("register")
#         if register_button:
#                 dump(conn, username, password, email)



st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


