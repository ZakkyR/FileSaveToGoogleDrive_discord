"""
投稿したファイルをGoogleDriveに投稿するBot
"""
# coding: utf-8
import sqlite3
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# GoogleAPI認証
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)