import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GUI.LoginGUI import LoginGUI

def main():
    LoginGUI()
