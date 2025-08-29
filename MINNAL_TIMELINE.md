# Development Plan: Chennai Power Alert System (Minnal)

## 1. Project Overview 🎯

The Chennai Power Alert System is a lightweight, automated service designed to solve a real-world problem: providing timely warnings about scheduled power cuts in Chennai. The system scrapes information from reliable online sources, processes it, and alerts users, helping them prepare for disruptions. This project aims to be a practical, useful tool and a demonstration of key software engineering skills, including web scraping, automation, and deployment.

---

## 2. Core Features (MVP) 📋

The Minimum Viable Product is focused on delivering a reliable, automated notification service.

-   [x] **V0.1: Intelligent Data Scraper**
    -   [x] Identify and scrape data from a reliable, non-CAPTCHA source (`livechennai.com`).
    -   [x] Intelligently handle the two-level page structure (index page -> detail page).
    -   [x] Use `datetime` to be date-aware, finding schedules for the current or next day.
    -   [x] Extract and clean the relevant text data (areas, times, dates).

-   [ ] **V0.2: Personal Notification System**
    -   [ ] Integrate with the Telegram Bot API.
    -   [ ] Send the scraped power cut information as a formatted message.
    -   [ ] Implement basic error handling (e.g., send a "No schedule found" message).

-   [ ] **V0.3: Automation Engine**
    -   [ ] Create a `requirements.txt` file for dependencies.
    -   [ ] Set up a GitHub Actions workflow to run the scraper script on a daily schedule.

-   [ ] **V0.4: Public Web Interface**
    -   [ ] Build a minimal web application using Flask or FastAPI.
    -   [ ] Create a single, clean webpage that displays the latest power cut information.
    -   [ ] Deploy the application to a free hosting service (e.g., Render).

---

## 3. Technology Stack 🛠️

* **Language:** Python 3.x
* **Core Libraries:** `requests`, `beautifulsoup4`
* **Web Framework:** Flask / FastAPI
* **Automation:** GitHub Actions
* **Notifications:** Telegram Bot API
* **Deployment:** Render (or similar PaaS)

---

## 4. Development Timeline 🗓️

This timeline is structured in phases to ensure steady progress and clear goals.

### **Phase 1: Core Automation (Target: First Week)**

* **Day 1:** Finalize and clean up the scraping script (`scraper.py`).
* **Day 2:** Create a Telegram Bot and integrate it into the script. The script should now send messages instead of printing to the terminal.
* **Day 3:** Set up the GitHub repository. Write the initial GitHub Actions workflow file to get the script running on a schedule.
* **Day 4:** Test and debug the automated workflow. Ensure notifications are being sent reliably at the scheduled time.

### **Phase 2: Web App & Deployment (Target: Second Week)**

* **Day 5-6:** Develop the basic Flask/FastAPI application. Create the main route that calls the scraper function and passes the data to a template.
* **Day 7:** Create a simple but clean HTML/CSS template to display the information.
* **Day 8:** Deploy the initial version of the web app to Render. Get a live, shareable URL.

### **Phase 3: Final Polish (Target: Third Week)**

* **Day 9:** Include a link to the live app.
* **Day 10:** Review all code, add comments where necessary, and ensure the project is ready.

---

## 5. Future Enhancements (V2.0 Ideas) 🚀

* **Area-specific subscriptions:** Allow users to subscribe to alerts only for their specific neighborhood.
* **Multiple data sources:** Add redundancy by scraping more than one news source.
* **Data persistence:** Store historical outage data in a database to analyze patterns.
* **Frontend improvements:** Add a map view to visualize the affected areas.