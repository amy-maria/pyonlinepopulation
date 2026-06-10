# 📊 Global Population Analytics SPA

A responsive, dynamic Single Page Application (SPA) designed to parse global census datasets and render interactive demographic analytics seamlessly in the browser. 

This portfolio piece demonstrates asynchronous frontend-backend communication, structural file parsing, and server-side memory optimization using Python and Flask.

## 🚀 Live Demo
Experience the live application on my Portolio site: amyrowell.dev

---

## 💡 Key Technical Competencies 

* **Single Page Application Architecture:** 
The application requests and receives structured image resources directly via the JavaScript Fetch API.
* **Server-Side Visual Compiling:** Implemented a non-GUI headless plotting engine (`matplotlib.use('Agg')`) to safely render complex multi-variable line graphs inside an isolated server environment.
* **In-Memory Stream Optimization:** Utilized standard byte streams (`io.BytesIO`) to process and encode binary graph files directly into Base64 formats. 
* **Production Deployment Readiness:** Maintained clean modular isolation between business parsing logic, routing endpoints, and external styling assets using Flask's native asset management (`/static/` and `/templates/`).

---

## 🛠️ Tech Stack & Dependencies

* **Backend Ecosystem:** Python 3+, Flask (Routing & Micro-API Structure)
* **Data Science Tools:** Matplotlib (Data Visualization), Native CSV Library (Parsing Engine)
* **Frontend Interface:** Modern HTML5, Semantic CSS3 (Clean Responsive Layout), Vanilla JavaScript (Fetch API Engine)
* **Production Hosting:** Gunicorn (WSGI HTTP Server), Render Cloud Infrastructure


📝 Contact & Portfolio Links
Developer: Amy Rowell
GitHub Profile: github.com/amy-maria
Portfolio: amyrowell.dev