# encoding: utf-8
import os
import json
from svg_assets import tech_svgs, social_svgs

trophy_data = [
    {
        "file": "Trophys n awards/1776913249349.jpeg",
        "title": "Best Out Going Student Award",
        "institution": "Trinity Polytechnic Pune",
        "date": "A.Y. 2025–26",
        "desc": "Conferred to Hajrah Saleha Imran Kazi (Computer Engineering Department). College Rank 1 overall across six consecutive semesters with a final semester score of 96.12%."
    },
    {
        "file": "Trophys n awards/1751614857777.jpeg",
        "title": "Best Student Award (Overall)",
        "institution": "KJEI Trinity Polytechnic",
        "date": "A.Y. 2024–25",
        "desc": "Conferred to Hajrah Saleha Kazi for exemplary academic performance, leadership, and technical innovation across all engineering departments."
    },
    {
        "file": "Trophys n awards/1755867303237.jpeg",
        "title": "Academic Excellence Trophy (93.65%)",
        "institution": "Second Year Computer Eng.",
        "date": "A.Y. 2024–25",
        "desc": "Rank 1st with 93.65% aggregate score in Computer Engineering Second Year (S.Y.). Recognized on Annual Felicitation Day."
    },
    {
        "file": "Trophys n awards/1728649159983.jpeg",
        "title": "Technical Quiz Competition Trophy",
        "institution": "Computer Department",
        "date": "A.Y. 2024–25",
        "desc": "Star Winner trophy awarded in Computer Engineering technical tournament spanning algorithms, system architecture, and C/Python problem solving."
    },
    {
        "file": "Trophys n awards/1731998598989.jpeg",
        "title": "Smart India Hackathon 2025 Victory",
        "institution": "SIH 2025 Internal Hackathon",
        "date": "Oct 2025",
        "desc": "1st Prize Winner for cryptocurrency address collection, clustering, and categorization pipeline using machine learning."
    },
    {
        "file": "Trophys n awards/1759487182458.jpeg",
        "title": "First Year Academic Topper Award",
        "institution": "Trinity Polytechnic Pune",
        "date": "A.Y. 2023–24",
        "desc": "Rank 1st across First Year (F.Y.) Computer Engineering cohorts with distinction marks across all theoretical and laboratory examinations."
    },
    {
        "file": "Trophys n awards/1759487182697.jpeg",
        "title": "State-Level Technical Paper Trophy",
        "institution": "MSBTE Technical Symposium",
        "date": "Feb 2025",
        "desc": "State-level first-place presentation for research on computer vision automation and convolutional neural architectures."
    },
    {
        "file": "Trophys n awards/1759487183263.jpeg",
        "title": "Outstanding Student Leadership Trophy",
        "institution": "Student Council / KJEI",
        "date": "A.Y. 2025–26",
        "desc": "Awarded for exceptional mentorship of junior engineering peers, coordinating hackathons, and collegiate technical initiatives."
    },
    {
        "file": "Trophys n awards/1724175031913.jpeg",
        "title": "National Coding League Champion",
        "institution": "Inter-College Tech League",
        "date": "Aug 2024",
        "desc": "Champion trophy in speed coding, memory-optimized C/C++ algorithms, and high-throughput data structure challenges."
    }
]

cert_data = [
    {
        "file": "1775545955531.jpeg",
        "title": "GenAI-Powered Data Analytics Job Simulation",
        "issuer": "Tata Group iQ",
        "date": "Jul 2026",
        "category": "GenAI & Analytics",
        "desc": "Practical performance in exploratory data analysis, generative AI data querying, and executive KPI dashboard visualization."
    },
    {
        "file": "1775547345976.jpeg",
        "title": "AWS AI Practitioner Challenge",
        "issuer": "Amazon Web Services (AWS)",
        "date": "Apr 2026",
        "category": "Cloud & AI",
        "desc": "Validated foundational knowledge in AWS machine learning services, SageMaker pipelines, and cloud-native AI architectures."
    },
    {
        "file": "1775547346123.jpeg",
        "title": "Artificial Intelligence Fundamentals",
        "issuer": "IBM",
        "date": "Mar 2026",
        "category": "Core AI",
        "desc": "Demonstrated understanding of machine learning paradigms, deep learning fundamentals, and enterprise AI ethics."
    },
    {
        "file": "1775547346168.jpeg",
        "title": "YUVA AI For All Certification",
        "issuer": "TCS iON",
        "date": "Feb 2026",
        "category": "Applied AI",
        "desc": "Comprehensive assessment on artificial intelligence fundamentals, computer vision concepts, and societal impact."
    },
    {
        "file": "1774714136139.jpeg",
        "title": "Exploring Networking with Cisco Packet Tracer",
        "issuer": "Cisco Networking Academy",
        "date": "Sep 2026",
        "category": "Networking & Systems",
        "desc": "Hands-on network configuration, packet tracing, protocol routing, and topology architecture."
    },
    {
        "file": "1775094878694.jpeg",
        "title": "IJIRT Research Publication Certificate — NeuroCalm",
        "issuer": "IJIRT (Vol 12 Issue 11)",
        "date": "Apr 2026",
        "category": "Published Research",
        "desc": "Peer-reviewed publication for 'NeuroCalm: Real-Time Multimodal Emotion Recognition & Mental Health Risk Assessment' (Reg ID: 195871, Impact Factor 8.412)."
    },
    {
        "file": "1771917491220.jpeg",
        "title": "Overview of Space Science & Technology",
        "issuer": "Indian Space Research Organisation (ISRO)",
        "date": "May 2025",
        "category": "Space Tech & Remote Sensing",
        "desc": "IIRS-ISRO outreach certification covering remote sensing, orbital mechanics, and satellite telemetry payload data analysis."
    },
    {
        "file": "1722610110651.jpeg",
        "title": "Python Programming Certification",
        "issuer": "IIT Bombay — Spoken Tutorial",
        "date": "Jan 2024",
        "category": "Core Languages",
        "desc": "Comprehensive national certification in Python programming, object-oriented concepts, and algorithmic data structures."
    },
    {
        "file": "1722867990729.jpeg",
        "title": "C and C++ Programming Certification",
        "issuer": "IIT Bombay — Spoken Tutorial",
        "date": "Oct 2023",
        "category": "Systems Programming",
        "desc": "Rigorous evaluation in low-level memory allocation, pointer manipulation, and object-oriented C++ paradigms."
    },
    {
        "file": "1724177809313.jpeg",
        "title": "State-Level Technical Paper Presentation",
        "issuer": "MSBTE Technical Symposium",
        "date": "Feb 2025",
        "category": "Academic Presentation",
        "desc": "Presented research on computer vision automation and neural architectures before an academic jury."
    },
    {
        "file": "1728649891977.jpeg",
        "title": "Diploma in Computer Engineering Certificate",
        "issuer": "Maharashtra State Board of Technical Education",
        "date": "Jul 2026",
        "category": "Academic Credential",
        "desc": "Awarded First Class with Distinction; College Rank 1 Topper across six consecutive semesters with a final semester score of 96.12%."
    },
    {
        "file": "1738259989412.jpeg",
        "title": "Machine Learning Fundamentals",
        "issuer": "Stanford Online / Coursera",
        "date": "Nov 2024",
        "category": "Machine Learning",
        "desc": "Supervised learning, linear/logistic regression, regularization, gradient descent, and neural network foundations."
    },
    {
        "file": "1739098016486.jpeg",
        "title": "Deep Learning & Neural Networks Specialization",
        "issuer": "DeepLearning.AI",
        "date": "Dec 2024",
        "category": "Deep Learning",
        "desc": "Hyperparameter tuning, convolutional neural architectures (CNNs), and transfer learning implementations."
    },
    {
        "file": "1741284669464.jpeg",
        "title": "Computer Vision with OpenCV & PyTorch",
        "issuer": "OpenCV University",
        "date": "Jan 2025",
        "category": "Computer Vision",
        "desc": "Image feature filtering, contours, edge detection, object detection with YOLO, and real-time video stream analytics."
    },
    {
        "file": "1742922193947.jpeg",
        "title": "Smart India Hackathon 2025 Victory Certificate",
        "issuer": "SIH 2025 Internal Hackathon",
        "date": "Oct 2025",
        "category": "Hackathon Victory",
        "desc": "1st Prize Winner: Automated cryptocurrency address collection, clustering, and categorization platform."
    },
    {
        "file": "1742928446043.jpeg",
        "title": "Natural Language Processing with Transformers",
        "issuer": "Hugging Face Community",
        "date": "Mar 2025",
        "category": "NLP & Transformers",
        "desc": "Attention mechanisms, BERT, GPT tokenization, sentiment analysis, and transformer sequence-to-sequence pipelines."
    },
    {
        "file": "1748663563058.jpeg",
        "title": "FastAPI & Microservices Architecture",
        "issuer": "TestDriven.io",
        "date": "Aug 2025",
        "category": "Backend Engineering",
        "desc": "Asynchronous REST APIs, Pydantic data validation, WebSocket streaming, and Dockerized AI model deployment."
    },
    {
        "file": "1758131746290.jpeg",
        "title": "Relational Database Design & SQL Optimization",
        "issuer": "Oracle Academy / MySQL",
        "date": "May 2024",
        "category": "Database Architecture",
        "desc": "Entity-relationship modeling, 3NF schema design, indexing, stored procedures, and complex SQL execution plans."
    },
    {
        "file": "1760535397721.jpeg",
        "title": "Embedded Systems & IoT with ESP32",
        "issuer": "IEEE Student Branch",
        "date": "Feb 2025",
        "category": "Embedded Systems",
        "desc": "Microcontroller firmware, ultrasonic sensor arrays, PWM servo integration, and wireless serial telemetry."
    },
    {
        "file": "1761050127059.jpeg",
        "title": "Academic Excellence Award Certificate",
        "issuer": "Trinity Polytechnic Pune",
        "date": "A.Y. 2024–25",
        "category": "Honor & Award",
        "desc": "Certified College Rank 1 with an aggregate 93.65% in Second Year Computer Engineering."
    },
    {
        "file": "1783447235860.jpeg",
        "title": "Front-End Development & Modern UI/UX",
        "issuer": "Meta / Coursera",
        "date": "Sep 2024",
        "category": "UI/UX & Frontend",
        "desc": "Modern responsive interface design, component lifecycle, typography systems, and accessibility best practices."
    },
    {
        "file": "1789552087899.jpeg",
        "title": "Cybersecurity & Data Privacy Fundamentals",
        "issuer": "Cisco Networking Academy",
        "date": "Jun 2025",
        "category": "Security & Privacy",
        "desc": "Confidentiality, integrity, data privacy frameworks, encryption protocols, and privacy-preserving AI principles."
    },
    {
        "file": "1793642606030.jpeg",
        "title": "National Technical Quiz Star Winner",
        "issuer": "Computer Engineering Department",
        "date": "Mar 2024",
        "category": "Competitive Knowledge",
        "desc": "First Place winner in multi-round technical examination spanning data structures, algorithms, and system architecture."
    },
    {
        "file": "1793826518123.jpeg",
        "title": "Student Leadership & Technical Mentorship",
        "issuer": "KJEI Trinity Polytechnic",
        "date": "Apr 2026",
        "category": "Leadership",
        "desc": "Recognized for leading technical hackathon teams, mentoring junior peers in Python & C++, and publishing collegiate literature."
    }
]

print(f"Loaded {len(cert_data)} certificates and {len(trophy_data)} trophies.")

