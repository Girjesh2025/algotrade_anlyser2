from app import main
import streamlit as st

# This is necessary for Vercel deployment
def handler(request, response):
    return response(200, main())
