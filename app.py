import os
from flask import Flask, send_from_directory, jsonify, abort

app = Flask(__name__, static_folder="static")

# ---- Pages ----
@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.get("/courses")
def courses_page():
    return send_from_directory("static", "courses.html")

@app.get("/course/<slug>")
def course_detail_page(slug: str):
    # For now, serve a single template for any course slug
    return send_from_directory("static", "course.html")

# ---- API ----
COURSES = [
    {
        "slug": "eng-design-1",
        "title": "Engineering Design & Presentation I",
        "description": "A practical start-to-finish intro to the engineering design process—sketching, CAD basics, documentation, and presenting solutions.",
        "level": "Beginner",
        "time": "6–9 weeks",
        "tags": ["Design Process", "CAD", "Communication"],
        "featured": True
    },
    {
        "slug": "eng-design-2",
        "title": "Engineering Design & Presentation II",
        "description": "Go deeper with more complex constraints, iteration, prototyping, and clearer technical communication—built around projects.",
        "level": "Intermediate",
        "time": "6–9 weeks",
        "tags": ["CAD", "Prototyping", "Documentation"],
        "featured": False
    },
    {
        "slug": "practicum-stem",
        "title": "Practicum in STEM",
        "description": "Applied, real-world problem solving with labs, teamwork, and deliverables that feel like industry work.",
        "level": "Intermediate",
        "time": "4–8 weeks",
        "tags": ["Projects", "Teamwork", "Career Skills"],
        "featured": False
    },
    {
        "slug": "land-surveying-cst-1",
        "title": "Land Surveying (CST Level 1)",
        "description": "Foundations of surveying—measurements, field notes, safety, basic calculations, and CST-aligned concepts.",
        "level": "Beginner",
        "time": "4–6 weeks",
        "tags": ["Surveying", "Field Work", "CST"],
        "featured": False
    },
]

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/courses")
def api_courses():
    return jsonify(COURSES)

@app.get("/api/courses/<slug>")
def api_course(slug: str):
    for c in COURSES:
        if c["slug"] == slug:
            return jsonify(c)
    abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
