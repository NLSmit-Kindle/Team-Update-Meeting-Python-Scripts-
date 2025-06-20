
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import Label
import io
import time
import os
import logging
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import gspread
from PIL import Image, ImageTk
script_dir = os.getcwd()
print(script_dir)