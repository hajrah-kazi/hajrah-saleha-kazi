# encoding: utf-8
import os, re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check for bad unicode artifacts
bad_patterns = ['Â·', 'â€"', 'â€"', 'Â©', 'â€œ', 'â€', 'â€™']
found_bad = [p for p in bad_patterns if p in text]
print("Corrupted sequences found:", found_bad)

# 2. Check all local media paths exist
img_matches = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:png|jpg|jpeg|pdf))["\']', text)
missing = []
for path in set(img_matches):
    clean = path.split('#')[0].replace('./', '')
    if not os.path.exists(clean):
        missing.append(path)
print(f"Total linked media files: {len(set(img_matches))}")
print(f"Missing media files: {missing}")

# 3. Check 10 key projects
projects = ["NeuroCalm 2.0", "Right-Fit AI-CV", "GoatAI", "RecapBot", "Focus Pulse Elite",
            "Adaptive Bloom Filter", "CivicAI", "ClinCase", "TeamMatch", "NEXUS-X"]
missing_proj = [p for p in projects if p not in text]
print("Missing projects:", missing_proj)

# 4. Check tech stack presence
techs = ["C++", "Java", "Python", "React", "Next.js 15", "Node.js", "Claude 3.5 Sonnet", "Gemini 2.x", "GPT-4o", "DeepSeek", "LangChain", "ESP32"]
missing_techs = [t for t in techs if t not in text]
print("Missing tech stack items:", missing_techs)

# 5. Check social links
socials = ["linkedin.com/in/hajrah-saleha-kazi", "github.com/hajrah-kazi", "hajrahsalehak@gmail.com", "wa.me/919860336250", "visionarydesignersco.com"]
missing_social = [s for s in socials if s not in text]
print("Missing social links:", missing_social)

# 6. Check terminal prompt is clean (no vit-pune)
if "hajrah@vit-pune" in text or "hajrah@vit" in text:
    print("WARNING: Old vit-pune terminal prompt still present!")
else:
    print("Terminal prompt: OK (hajrah-saleha-kazi)")

# 7. Check confetti
if "triggerConfetti" in text and "triggerResumeWithConfetti" in text:
    print("Confetti: OK")
else:
    print("Confetti: MISSING")

print("\nAll checks complete.")

