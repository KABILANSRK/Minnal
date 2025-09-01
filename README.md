# Minnal

# Development Plan: Chennai Power Alert System (Minnal)

## 1. Project Overview 

The Chennai Power Alert System is a lightweight, automated service designed to solve a real-world problem: providing timely warnings about scheduled power cuts in Chennai. The system scrapes information from reliable online sources, processes it, and alerts users, helping them prepare for disruptions. This project aims to be a practical, useful tool and a demonstration of key software engineering skills, including web scraping, automation, and deployment.

---

## 2. Core Features (MVP) 

The Minimum Viable Product is focused on delivering a reliable, automated notification service.

-   [x] **V0.1: Intelligent Data Scraper**
    -   [x] Identify and scrape data from a reliable, non-CAPTCHA source (`livechennai.com`).
    -   [x] Intelligently handle the two-level page structure (index page -> detail page).
    -   [x] Use `datetime` to be date-aware, finding schedules for the current or next day.
    -   [x] Extract and clean the relevant text data (areas, times, dates).

-   [x] **V0.2: Personal Notification System**
    -   [x] Integrate with the Telegram Bot API.
    -   [x] Send the scraped power cut information as a formatted message.
    -   [x] Implement basic error handling (e.g., send a "No schedule found" message).

-   [ ] **V0.3: Automation Engine**
    -   [ ] Create a `requirements.txt` file for dependencies.
    -   [ ] Set up a GitHub Actions workflow to run the scraper script on a daily schedule.

-   [ ] **V0.4: Public Web Interface**
    -   [ ] Build a minimal web application using Flask or FastAPI.
    -   [ ] Create a single, clean webpage that displays the latest power cut information.
    -   [ ] Deploy the application to a free hosting service (e.g., Render).

---

## 3. Technology Stack 

* **Language:** Python 3.x
* **Core Libraries:** `requests`, `beautifulsoup4`
* **Web Framework:** Flask / FastAPI
* **Automation:** GitHub Actions
* **Notifications:** Telegram Bot API
* **Deployment:** Render (or similar PaaS)

---

## 4. Future Enhancements (V2.0 Ideas) 

* **Area-specific subscriptions:** Allow users to subscribe to alerts only for their specific neighborhood.
* **Multiple data sources:** Add redundancy by scraping more than one news source.
* **Data persistence:** Store historical outage data in a database to analyze patterns.
* **Frontend improvements:** Add a map view to visualize the affected areas.