# durgesh-codes
A blockchain platform ensuring farm-to-consumer transparency and authenticity in the Ayurvedic supply chain.
# AyurTrace: Blockchain-Enabled Ayurvedic Supply Chain 🏆

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Framework](https://img.shields.io/badge/Framework-FastAPI-blue) ![Status](https://img.shields.io/badge/Status-PoC_&_UI_Prototype-green)

A FastAPI backend that generates unique QR codes for Ayurvedic product batches, serving as the foundational layer for a transparent, blockchain-powered supply chain.

---

> ⚠️ **Project Status: Backend PoC (FastAPI) + UI Prototype**
>
> This repository contains the **Python backend source code** and showcases the **working UI prototype** for our 1st Place winning project at the internal Smart India Hackathon 2025 in Jaipur. The FastAPI backend demonstrates the core data entry and QR code generation logic developed during the hackathon.

## 🌿 The Problem

The Ayurveda industry suffers from a lack of transparency. Consumers have no verifiable way to confirm the origin or purity of products, leading to a trust deficit. Farmers who produce high-quality, authentic crops often lack the means to prove the value of their produce in the supply chain.

## ✨ Our Solution: AyurTrace

AyurTrace is a system designed to bring trust and transparency to this ecosystem. This repository contains the first crucial component: a backend service that registers new batches of Ayurvedic products and generates a unique QR code for each one. This QR code acts as a digital passport, allowing anyone to access the product's history.

## 🎨 UI Prototype Showcase

We designed and built a working UI prototype to demonstrate the complete user journey. It provides a clear and intuitive interface for farmers, distributors, and consumers.

> *Caption: The main dashboard providing an overview of the supply chain.*

## ✅ Core Features Implemented (Backend)

* **FastAPI Backend:** Built with a modern, high-performance Python framework.
* **Dynamic QR Code Generation:** Automatically creates and saves a unique QR code for every new batch registered.
* **RESTful API Endpoints:**
    * `POST /add_batch/`: Adds a new product batch to the system.
    * `GET /get_batch/{batch_id}`: Retrieves the details of a specific batch.
    * `GET /qr/{batch_id}`: Serves the generated QR code image directly via an endpoint.
* **In-Memory Database:** Utilizes a simple in-memory dictionary for rapid prototyping and demonstration purposes.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **QR Generation:** `qrcode` library
* **Data Validation:** Pydantic (built into FastAPI)
* **API Server:** Uvicorn
* **Frontend (UI Prototype):** HTML, CSS, JavaScript (or Figma)

## 🚀 Getting Started (Backend)

Follow these instructions to get the backend server up and running on your local machine.

### Prerequisites

* Python (3.9 or higher)
* pip & venv

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/durgesh-1801/durgesh-codes/edit/main/README.md]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd [https://github.com/durgesh-1801/durgesh-codes/edit/main/README.md]
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv
    # Activate it (Windows)
    .\venv\Scripts\activate
    # Activate it (macOS/Linux)
    source venv/bin/activate
    ```
4.  **Create a `requirements.txt` file** with the following content:
    ```txt
    fastapi
    uvicorn[standard]
    pydantic
    qrcode[pil]
    ```
5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6.  **Rename your main Python file** to `ayutrace.py` (if it's not already named that).

7.  **Start the server:**
    ```bash
    uvicorn ayutrace:app --reload
    ```
    The server will be running on `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## 💡 Vision & Future Scope

This proof-of-concept is the first step. The vision is to expand this into a full-stack, decentralized application:

* **Blockchain Integration:** Replace the in-memory database with smart contracts on a blockchain. Every batch update will become an immutable transaction, providing ultimate transparency.
* **Persistent Database:** Use a database like MongoDB or PostgreSQL for storing off-chain data (e.g., user profiles).
* **Full Frontend Integration:** Connect the working UI prototype to the FastAPI backend to create a seamless user experience.

## 🧑‍💻 Our Team
This project was made possible by the collaborative effort of our dedicated team:

* **Durgesh Sharma** - Backend & Blockchain Lead
* **Mantra Singh** - Frontend Developer 
* **Navya Sharma** - Graphic and UI designer    
* **Snehreet Kaur** - Helped in Backend and Blockchain
* **Devangini** - Helped in Frontend 
* **Gun Agarwal** - Researcher

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
 
