from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Edoardo_Fratus_CV_2026.pdf"
STATIC_COPY = ROOT / "static" / "files" / "Edoardo_Fratus_CV_2026.pdf"

ACCENT = colors.HexColor("#e74f3d")
GREEN = colors.HexColor("#2f8f7d")
INK = colors.HexColor("#1f1f1f")
MUTED = colors.HexColor("#555555")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "Name",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=25,
        leading=27,
        alignment=TA_CENTER,
        textColor=INK,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.2,
        leading=11,
        alignment=TA_CENTER,
        textColor=ACCENT,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.6,
        leading=9,
        alignment=TA_CENTER,
        textColor=MUTED,
        spaceAfter=9,
    )
)
styles.add(
    ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=9.1,
        leading=10.2,
        textColor=ACCENT,
        spaceBefore=5,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.55,
        leading=9.2,
        textColor=INK,
        spaceAfter=2.7,
    )
)
styles.add(
    ParagraphStyle(
        "BodyTight",
        parent=styles["Body"],
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        "JobTitle",
        parent=styles["Body"],
        fontName="Helvetica-Bold",
        fontSize=8.25,
        leading=9.5,
        textColor=INK,
        spaceBefore=1.2,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        "Meta",
        parent=styles["Body"],
        fontName="Helvetica-Bold",
        fontSize=7.2,
        leading=8.5,
        textColor=GREEN,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        "CvBullet",
        parent=styles["Body"],
        leftIndent=9,
        firstLineIndent=0,
        bulletIndent=0,
        bulletFontSize=4.8,
        spaceAfter=1.4,
    )
)
styles.add(
    ParagraphStyle(
        "Skill",
        parent=styles["Body"],
        fontSize=7.2,
        leading=8.8,
        spaceAfter=2.4,
    )
)


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def bullets(items):
    return [Paragraph(item, styles["CvBullet"], bulletText="•") for item in items]


def section(title):
    return p(title.upper(), "Section")


def job(title, period, summary, bullet_items):
    return KeepTogether(
        [
            p(title, "JobTitle"),
            p(period, "Meta"),
            p(summary, "BodyTight"),
            *bullets(bullet_items),
            Spacer(1, 1.5),
        ]
    )


def build_story():
    left = [
        section("Selected Impact"),
        *bullets(
            [
                "Led end-to-end delivery of a major Welfare/Flexben feature across a six-month lifecycle, coordinating Product, frontend, mobile, and backend teams.",
                "Co-built Satispay Fringe Benefits backend from scratch, supporting EUR 30M in transactions during the first three months.",
                "Designed event-driven fan-out processing for simultaneous year-end order closing in Flexben, improving scalability under bursty workloads.",
                "Created Claude subagents adopted internally to automate repetitive coding tasks, turning AI experimentation into practical engineering workflow.",
            ]
        ),
        section("Experience"),
        job(
            "Software Engineer III (L5) - Satispay",
            "Mar 2026 - Present | Milan, Italy",
            "Technical owner and hands-on backend engineer for major Welfare and Flexben initiatives.",
            [
                "Lead feature delivery end to end, from technical analysis and scope shaping to development, launch, and follow-up.",
                "Partner with Product to translate business needs into robust technical specifications and implementation plans.",
                "Coordinate frontend, mobile, and backend teams to keep integration clean and delivery aligned.",
                "Balance technical leadership with direct contribution to backend design, implementation, review, and production readiness.",
            ],
        ),
        job(
            "Software Engineer II (L4) - Satispay",
            "Feb 2025 - Mar 2026 | Milan, Italy",
            "Designed and delivered high-impact backend capabilities for Satispay Welfare Flexben.",
            [
                "Built core payment platform and report reconciliation features for Welfare/Flexben products.",
                "Designed high-performance event-driven fan-out for simultaneous closing of Flexben year orders.",
                "Engineered circuit breaker mechanisms to prevent cascading failures during peak load.",
                "Pioneered Virtual Threads adoption for I/O-bound services, improving throughput while keeping concurrency simpler.",
                "Created Claude subagents used across the company to automate low-level and boilerplate engineering tasks.",
            ],
        ),
        job(
            "Junior Software Engineer (L3) - Satispay",
            "2023 - Feb 2025 | Milan, Italy",
            "Backend engineer in the Welfare team, building Java Spring services and AWS-backed products.",
            [
                "Co-built the Satispay Fringe Benefits backend from scratch, focusing on Order and Purchase flows.",
                "Designed scalable service flows using Java, Spring Boot, PostgreSQL, MySQL, DynamoDB, and AWS services.",
            ],
        ),
        job(
            "Software Engineer Intern - Accenture",
            "2023 | Milan, Italy",
            "Built a Python microservice for automated document defect detection using YOLO and deep learning.",
            [],
        ),
    ]

    right = [
        section("Competencies"),
        p("<b>Backend:</b> Java 8/11/17/21/25, Spring Boot, REST APIs, microservices, JPA, MyBatis, Jersey, SQL", "Skill"),
        p("<b>Distributed Systems:</b> event-driven architecture, fan-out processing, high availability, circuit breakers, fault isolation, performance under load", "Skill"),
        p("<b>Cloud and Data:</b> AWS Lambda, EC2, ECS, S3, Kinesis, SQS, SNS, Docker, PostgreSQL, MySQL, Redshift, DynamoDB", "Skill"),
        p("<b>AI Engineering:</b> LLMs, AI agents, Claude subagents, prompt/workflow design, local AI experimentation, GenAI automation, Python, TensorFlow, PyTorch, YOLO", "Skill"),
        p("<b>Leadership:</b> end-to-end project ownership, technical analysis, product collaboration, cross-functional alignment, mentoring through code review", "Skill"),
        section("AI Work"),
        *bullets(
            [
                "Built Claude subagents for repetitive engineering tasks and internal code generation workflows.",
                "Use LLMs concretely for analysis, boilerplate removal, test scaffolding, migration support, and local-first experimentation.",
                "Interested in AI agents that improve engineering throughput without bypassing design judgement.",
            ]
        ),
        section("How I Work"),
        *bullets(
            [
                "Turn ambiguous product needs into technical plans.",
                "Keep backend design simple under pressure.",
                "Lead cross-team delivery while staying hands-on.",
                "Treat reliability and observability as product quality.",
            ]
        ),
        section("Education"),
        p("<b>M.Sc. Computer Engineering</b><br/>Universita degli Studi di Brescia, 2023<br/>Final grade: 108/110", "Skill"),
        section("Languages"),
        p("Italian and English", "Skill"),
        section("Links"),
        p("linkedin.com/in/edoardofratus<br/>github.com/edoofra<br/>edoofra.github.io/personal_portfolio", "Skill"),
    ]

    return [
        p("Edoardo Fratus", "Name"),
        p("SOFTWARE ENGINEER III (L5) - DISTRIBUTED SYSTEMS, FINTECH, AI ENGINEERING", "Role"),
        p(
            "Milan, Italy | edoardo.fra.ef@gmail.com | (+39) 3343410122 | "
            "linkedin.com/in/edoardofratus | github.com/edoofra",
            "Contact",
        ),
        section("Profile"),
        p(
            "Software Engineer III with 3+ years building high-scale fintech platforms at Satispay. "
            "Known for leading projects end to end: from product discovery and technical analysis to "
            "cross-team delivery, implementation, launch, and operational resilience. Strong backend foundation "
            "in Java, Spring, AWS, event-driven systems, and payment workflows, with concrete hands-on adoption "
            "of LLMs and AI agents to accelerate engineering work.",
            "Body",
        ),
        FrameBreak(),
        *left,
        FrameBreak(),
        *right,
    ]


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(0.7)
    canvas.line(90 * mm, 15 * mm, 120 * mm, 15 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 9 * mm, "Edoardo Fratus - CV 2026")
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    STATIC_COPY.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=11 * mm,
        bottomMargin=16 * mm,
        title="Edoardo Fratus CV 2026",
        author="Edoardo Fratus",
    )
    header_height = 45 * mm
    gap = 4 * mm
    header_y = A4[1] - doc.topMargin - header_height
    column_height = header_y - doc.bottomMargin - gap
    column_y = doc.bottomMargin
    left_width = 126 * mm
    column_gap = 5 * mm
    right_width = doc.width - left_width - column_gap
    frames = [
        Frame(doc.leftMargin, header_y, doc.width, header_height, id="header", showBoundary=0),
        Frame(doc.leftMargin, column_y, left_width, column_height, id="left", showBoundary=0),
        Frame(doc.leftMargin + left_width + column_gap, column_y, right_width, column_height, id="right", showBoundary=0),
    ]
    doc.addPageTemplates([PageTemplate(id="cv", frames=frames, onPage=draw_footer)])
    doc.build(build_story())
    shutil.copyfile(OUTPUT, STATIC_COPY)
    print(OUTPUT)
    print(STATIC_COPY)


if __name__ == "__main__":
    main()
