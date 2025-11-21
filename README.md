# 🏷️ Smart File Renamer

<div align="center">

![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Created by [Albin Sajeev](https://github.com/albinsajeev)**

> **Clean messy filenames and organize them into a perfect sequence (001, 002...) automatically.**

[⬇️ **Download Latest App (v1.0)**](https://github.com/albinsajeev/Smart-File-Renamer/releases)

</div>

---

## 🧐 The Problem
We've all downloaded courses or file collections that look like a mess. Windows often sorts them incorrectly because it treats numbers as text (placing "10" before "2"), making it frustrating to view files in the correct order.

## 💡 The Solution
**Smart File Renamer** is a Windows GUI tool that intelligently cleans filenames. It uses **Regex** to detect the "real" name of the file, strips away junk prefixes, and applies a clean, zero-padded numbering system.

### **See the Difference**

| ❌ Messy (Before) | ✅ Cleaned (After) |
| :--- | :--- |
| `1. Introduction.mp4` | `001_Introduction.mp4` |
| `10. Summary.mp4` | `010_Summary.mp4` |
| `001_001_Chapter 1.mp4` | `001_Chapter 1.mp4` |
| `2 - Setup Guide.pdf` | `002_Setup Guide.pdf` |

---

## 🚀 Key Features

### 🧹 Regex-Based Cleaning
Automatically identifies and removes messy prefixes like `0
