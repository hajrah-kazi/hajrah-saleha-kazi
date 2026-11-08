# encoding: utf-8
import os
import json
from svg_assets import tech_svgs, social_svgs
from data_store import cert_data, trophy_data

def build_elite_html():
    cert_json_str = json.dumps(cert_data)
    trophy_json_str = json.dumps(trophy_data)

    track1_certs = cert_data[:12]
    track2_certs = cert_data[12:]

    def render_cert_card(c, idx):
        return f'''
        <div onclick="openCertificateModal('certificates/{c['file']}', '{c['title']}', '{c['issuer']} &bull; {c['date']}')" 
             class="group relative flex-shrink-0 w-72 sm:w-80 p-3 rounded-2xl border transition-all duration-300 hover:scale-[1.03] hover:shadow-xl cursor-pointer"
             style="background: var(--bg-surface); border-color: var(--border-line);">
          <div class="relative h-44 rounded-xl overflow-hidden bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 mb-3">
            <img src="certificates/{c['file']}" alt="{c['title']}" loading="lazy" class="w-full h-full object-cover object-top transition-transform duration-500 group-hover:scale-105">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-3">
              <span class="text-xs font-mono font-bold text-white flex items-center gap-1">
                <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i> Expand Credential
              </span>
            </div>
            <span class="absolute top-2 right-2 px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-black/60 backdrop-blur-md text-amber-400 border border-amber-400/30">
              {c['category']}
            </span>
          </div>
          <div class="space-y-1">
            <h4 class="text-sm font-bold text-appText line-clamp-1 group-hover:text-sky-600 dark:group-hover:text-sky-400 transition-colors">
              {c['title']}
            </h4>
            <div class="flex items-center justify-between text-xs text-appMuted">
              <span class="font-medium truncate max-w-[170px]">{c['issuer']}</span>
              <span class="font-mono text-[10px]">{c['date']}</span>
            </div>
          </div>
        </div>
        '''

    track1_html = "".join([render_cert_card(c, i) for i, c in enumerate(track1_certs)]) * 2
    track2_html = "".join([render_cert_card(c, i+12) for i, c in enumerate(track2_certs)]) * 2

    html = f'''<!DOCTYPE html>
<html lang="en" class="light scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hajrah Saleha Kazi | AI/ML Engineer & Applied Computer Vision Specialist</title>
  
  <!-- Open Graph & Social Sharing Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Hajrah Saleha Kazi | AI/ML Engineer & Computer Vision Specialist">
  <meta property="og:description" content="Portfolio of Hajrah Saleha Kazi - AI/ML Engineer, B.Tech CSE (AI & ML) at VIT Pune, Published Researcher in IJIRT, 6-semester College Rank 1 Topper. Open for paid roles, internships, and freelance projects.">
  <meta property="og:image" content="./HSK.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Hajrah Saleha Kazi | AI/ML Engineer & Computer Vision Specialist">
  <meta name="twitter:description" content="AI/ML Engineer & Computer Vision Specialist at VIT Pune. Published researcher in multimodal deep learning (IJIRT), 6-semester College Rank 1 Topper.">
  <meta name="twitter:image" content="./HSK.png">
  <meta name="description" content="Portfolio of Hajrah Saleha Kazi - AI/ML Engineer, Computer Vision Specialist, B.Tech CSE (AI & ML) at VIT Pune, Published Researcher & Author. Open for paid roles, internships, and freelance projects.">
  <link rel="icon" type="image/png" href="./HSK.png">

  <!-- Typography: Plus Jakarta Sans, Inter, JetBrains Mono, Playfair Display -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            appBg: 'var(--bg-canvas)',
            appCard: 'var(--bg-surface)',
            appText: 'var(--text-primary)',
            appMuted: 'var(--text-secondary)',
            appBorder: 'var(--border-line)',
            brandGold: '#b45309',
            brandGoldLight: '#d97706',
            brandCyan: '#0284c7',
            brandCyanLight: '#0ea5e9',
            brandPurple: '#7c3aed'
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', '"Inter"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
            serif: ['"Playfair Display"', 'serif']
          }},
          animation: {{
            'marquee': 'marquee 45s linear infinite',
            'marquee-reverse': 'marqueeReverse 45s linear infinite',
            'story-ring': 'storyRing 3.5s ease infinite',
            'blink': 'blink 1s step-end infinite',
            'float-subtle': 'floatSubtle 6s ease-in-out infinite'
          }},
          keyframes: {{
            marquee: {{
              '0%': {{ transform: 'translateX(0%)' }},
              '100%': {{ transform: 'translateX(-50%)' }}
            }},
            marqueeReverse: {{
              '0%': {{ transform: 'translateX(-50%)' }},
              '100%': {{ transform: 'translateX(0%)' }}
            }},
            storyRing: {{
              '0%': {{ backgroundPosition: '0% 50%' }},
              '50%': {{ backgroundPosition: '100% 50%' }},
              '100%': {{ backgroundPosition: '0% 50%' }}
            }},
            blink: {{
              '0%, 100%': {{ opacity: '1' }},
              '50%': {{ opacity: '0' }}
            }},
            floatSubtle: {{
              '0%, 100%': {{ transform: 'translateY(0px)' }},
              '50%': {{ transform: 'translateY(-6px)' }}
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons, Three.js, Canvas Confetti -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <style>
    /* ==================== NEO-SKEUOMORPHIC / SOFT-GLASS VARIABLES ==================== */
    :root {{
      --bg-canvas: #f4f6f9;
      --bg-canvas-subtle: #ebedf2;
      --bg-surface: rgba(255, 255, 255, 0.88);
      --bg-surface-solid: #ffffff;
      --bg-surface-hover: #ffffff;
      --text-primary: #111111;
      --text-secondary: #4a4a4a;
      --text-tertiary: #666666;
      --border-line: rgba(0, 0, 0, 0.08);
      --border-line-strong: rgba(0, 0, 0, 0.14);
      --nav-glass: rgba(255, 255, 255, 0.82);
      --pill-active-bg: #111111;
      --pill-active-text: #ffffff;
      --cta-btn-bg: #111111;
      --cta-btn-text: #ffffff;
      
      --neo-shadow: 0 10px 30px rgba(0, 0, 0, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02);
      --neo-card-shadow: 0 12px 36px -4px rgba(0, 0, 0, 0.05), inset 0 1px 1px rgba(255, 255, 255, 0.95);
      --neo-inset: inset 0 2px 4px rgba(0, 0, 0, 0.03);
    }}

    .dark {{
      --bg-canvas: #090c13;
      --bg-canvas-subtle: #0f1522;
      --bg-surface: rgba(18, 24, 38, 0.82);
      --bg-surface-solid: #121826;
      --bg-surface-hover: rgba(26, 34, 52, 0.9);
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-tertiary: #64748b;
      --border-line: rgba(255, 255, 255, 0.08);
      --border-line-strong: rgba(255, 255, 255, 0.16);
      --nav-glass: rgba(14, 19, 30, 0.82);
      --pill-active-bg: #ffffff;
      --pill-active-text: #090c13;
      --cta-btn-bg: #ffffff;
      --cta-btn-text: #090c13;
      
      --neo-shadow: 0 16px 40px rgba(0, 0, 0, 0.5), 0 1px 2px rgba(255, 255, 255, 0.05);
      --neo-card-shadow: 0 16px 40px -8px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.08);
      --neo-inset: inset 0 2px 4px rgba(0, 0, 0, 0.4);
    }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-primary);
      transition: background-color 0.3s ease, color 0.3s ease;
      overflow-x: hidden;
    }}

    /* Diffuse Atmospheric Glow Background Hotspots */
    .glow-canvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}
    .glow-blob {{
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.18;
      transition: opacity 0.5s ease;
    }}
    .dark .glow-blob {{
      opacity: 0.24;
      filter: blur(120px);
    }}

    /* Frosted glass card utility */
    .glass-card {{
      background: var(--bg-surface);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-line);
      box-shadow: var(--neo-card-shadow);
      transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }}
    .glass-card:hover {{
      border-color: var(--border-line-strong);
    }}

    /* Pause marquee on hover */
    .marquee-track:hover {{
      animation-play-state: paused !important;
    }}

    /* Custom scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: var(--bg-canvas);
    }}
    ::-webkit-scrollbar-thumb {{
      background: var(--border-line-strong);
      border-radius: 9999px;
    }}

    /* Instagram-story gradient ring */
    .story-gradient-ring {{
      background: linear-gradient(45deg, #f59e0b, #ec4899, #8b5cf6, #06b6d4, #10b981);
      background-size: 300% 300%;
      animation: storyRing 3.5s ease infinite;
    }}
  </style>
</head>
<body class="font-sans antialiased selection:bg-amber-500/20 selection:text-amber-800 dark:selection:text-amber-200">

  <!-- Diffuse Atmospheric Glows -->
  <div class="glow-canvas">
    <div class="glow-blob w-[520px] h-[520px] -top-40 -left-20 bg-purple-400 dark:bg-purple-600"></div>
    <div class="glow-blob w-[580px] h-[580px] top-[30%] -right-40 bg-sky-400 dark:bg-sky-600"></div>
    <div class="glow-blob w-[500px] h-[500px] bottom-[15%] left-[10%] bg-amber-400 dark:bg-amber-600"></div>
  </div>

  <!-- ==================== STREAMLINED FLOATING CAPSULE NAVBAR ==================== -->
  <header class="fixed top-4 sm:top-5 left-0 right-0 z-50 px-4 transition-all duration-300" id="main-nav">
    <nav class="max-w-5xl mx-auto flex items-center justify-between rounded-full px-5 py-2.5 border shadow-lg backdrop-blur-xl transition-all"
         style="background: var(--nav-glass); border-color: var(--border-line); box-shadow: var(--neo-shadow);">
      
      <!-- Brand & Monogram -->
      <a href="#hero" class="flex items-center gap-2.5 group">
        <div class="w-8 h-8 rounded-full overflow-hidden border border-amber-500/40 shadow-sm transition-transform duration-300 group-hover:scale-105">
          <img src="./HSK.png" alt="HSK Monogram" class="w-full h-full object-cover">
        </div>
        <div class="flex flex-col">
          <span class="font-serif font-bold text-sm tracking-tight text-appText group-hover:text-amber-600 dark:group-hover:text-amber-400 transition-colors">
            Hajrah Saleha Kazi
          </span>
          <span class="text-[9px] font-mono tracking-wider uppercase text-appMuted hidden sm:block">
            AI/ML Engineer &bull; VIT Pune
          </span>
        </div>
      </a>

      <!-- Desktop Clean Navigation Links (Uncluttered) -->
      <div class="hidden md:flex items-center gap-1 text-xs font-medium text-appMuted" id="nav-desktop-links">
        <a href="#about" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">About</a>
        <a href="#projects" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Projects</a>
        <a href="#skills" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Tech Stack</a>
        <a href="#experience" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Experience</a>
        <a href="#trophies" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Awards</a>
        <a href="#certificates" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Credentials</a>
        <a href="#contact" class="px-3 py-1.5 rounded-full hover:text-appText hover:bg-black/5 dark:hover:bg-white/5 transition-colors">Contact</a>
      </div>

      <!-- Action Pill & Toggles -->
      <div class="flex items-center gap-2">
        <!-- Sound Effect Toggle -->
        <button id="sound-toggle-btn" title="Toggle UI Sound Effects" class="p-2 rounded-full border text-appMuted hover:text-appText transition-colors"
                style="border-color: var(--border-line); background: var(--bg-surface);">
          <i data-lucide="volume-2" class="w-4 h-4" id="sound-icon"></i>
        </button>

        <!-- Light / Dark Mode Toggle -->
        <button id="theme-toggle-btn" title="Toggle Light / Dark Mode" class="p-2 rounded-full border text-appMuted hover:text-appText transition-colors"
                style="border-color: var(--border-line); background: var(--bg-surface);">
          <i data-lucide="sun" class="w-4 h-4 hidden dark:block text-amber-400"></i>
          <i data-lucide="moon" class="w-4 h-4 block dark:hidden text-slate-700"></i>
        </button>

        <!-- Verified Resume CTA with Confetti Trigger -->
        <button onclick="triggerResumeWithConfetti()" class="px-4 py-1.5 rounded-full text-xs font-semibold flex items-center gap-1.5 shadow-sm transition-all duration-200 hover:scale-105 active:scale-95"
                style="background: var(--cta-btn-bg); color: var(--cta-btn-text);">
          <i data-lucide="file-text" class="w-3.5 h-3.5"></i>
          <span>Resume</span>
        </button>

        <!-- Mobile Menu Trigger -->
        <button id="mobile-menu-btn" class="md:hidden p-2 rounded-full border text-appMuted hover:text-appText"
                style="border-color: var(--border-line); background: var(--bg-surface);">
          <i data-lucide="menu" class="w-4 h-4"></i>
        </button>
      </div>
    </nav>

    <!-- Mobile Dropdown Menu -->
    <div id="mobile-menu" class="hidden md:hidden max-w-5xl mx-auto mt-2 p-4 rounded-3xl border shadow-xl backdrop-blur-2xl transition-all"
         style="background: var(--bg-surface); border-color: var(--border-line);">
      <div class="flex flex-col gap-2 text-sm font-medium text-appText">
        <a href="#about" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">About</a>
        <a href="#projects" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Projects</a>
        <a href="#skills" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Tech Stack</a>
        <a href="#experience" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Experience</a>
        <a href="#trophies" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Awards</a>
        <a href="#certificates" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Credentials</a>
        <a href="#contact" onclick="closeMobileMenu()" class="px-3 py-2 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">Contact</a>
      </div>
    </div>
  </header>

  <!-- ==================== HERO SECTION & 3D INTERACTIVE CANVAS ==================== -->
  <section id="hero" class="relative pt-28 sm:pt-36 pb-16 px-4 md:px-8 overflow-hidden z-10">
    <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
      
      <!-- Left Column: Name First -> Then Dynamic "I..." -> Then Subtitle -->
      <div class="lg:col-span-7 space-y-4 text-left">
        
        <!-- Status Pill -->
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border text-xs font-mono tracking-wide"
             style="background: var(--bg-surface); border-color: var(--border-line);">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span class="text-appMuted font-medium">Available for Opportunities &bull; Open for Paid Roles</span>
        </div>

        <!-- 1. AUTHORITATIVE UNIFIED HEADLINE FIRST -->
        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-appText leading-[1.1]">
          Hajrah Saleha Kazi
        </h1>

        <!-- 2. DYNAMIC "I..." LINE IMMEDIATELY AFTER NAME -->
        <div class="h-10 sm:h-12 flex items-center text-xl sm:text-2xl lg:text-3xl font-mono font-semibold text-appText">
          <span>I&nbsp;</span>
          <span id="dynamic-typewriter" class="text-sky-600 dark:text-sky-400"></span>
          <span class="animate-blink text-amber-500">_</span>
        </div>

        <!-- 3. SUBTITLE & CREDENTIALS -->
        <p class="text-base sm:text-lg text-appMuted font-normal leading-relaxed max-w-2xl">
          <strong class="text-appText font-semibold">B.Tech CSE (AI & ML) Student at Vishwakarma Institute of Technology (VIT), Pune</strong>. AI Lead Developer, published researcher in multimodal deep learning (IJIRT), and 6-semester College Rank 1 Topper across engineering departments.
        </p>

        <!-- Quick Stats Grid -->
        <div class="grid grid-cols-3 gap-3 pt-2 max-w-lg">
          <div class="p-3 rounded-2xl border" style="background: var(--bg-surface); border-color: var(--border-line);">
            <div class="text-xl sm:text-2xl font-extrabold font-mono text-amber-600 dark:text-amber-400">#1</div>
            <div class="text-[11px] text-appMuted font-medium">College Rank (6 Sems)</div>
          </div>
          <div class="p-3 rounded-2xl border" style="background: var(--bg-surface); border-color: var(--border-line);">
            <div class="text-xl sm:text-2xl font-extrabold font-mono text-sky-600 dark:text-sky-400">96.12%</div>
            <div class="text-[11px] text-appMuted font-medium">Final Diploma Sem</div>
          </div>
          <div class="p-3 rounded-2xl border" style="background: var(--bg-surface); border-color: var(--border-line);">
            <div class="text-xl sm:text-2xl font-extrabold font-mono text-purple-600 dark:text-purple-400">10+</div>
            <div class="text-[11px] text-appMuted font-medium">AI & Core Systems</div>
          </div>
        </div>

        <!-- CTAs -->
        <div class="flex flex-wrap items-center gap-3 pt-2">
          <a href="#projects" class="px-6 py-3 rounded-full text-xs sm:text-sm font-semibold flex items-center gap-2 shadow-md hover:scale-[1.02] active:scale-95 transition-all"
             style="background: var(--cta-btn-bg); color: var(--cta-btn-text);">
            <span>Explore Engineering Work</span>
            <i data-lucide="arrow-down" class="w-4 h-4"></i>
          </a>
          <button onclick="triggerResumeWithConfetti()" class="px-5 py-3 rounded-full text-xs sm:text-sm font-semibold flex items-center gap-2 border hover:border-appText transition-all"
                  style="background: var(--bg-surface); border-color: var(--border-line); color: var(--text-primary);">
            <i data-lucide="download" class="w-4 h-4 text-sky-600 dark:text-sky-400"></i>
            <span>Verified Resume</span>
          </button>
          <a href="#contact" class="px-5 py-3 rounded-full text-xs sm:text-sm font-semibold flex items-center gap-2 text-appMuted hover:text-appText transition-colors">
            <span>Get in Touch</span>
            <i data-lucide="mail" class="w-4 h-4"></i>
          </a>
        </div>
      </div>

      <!-- Right Column: Mesmerizing 3D Interactive Three.js Neural Sphere -->
      <div class="lg:col-span-5 flex justify-center">
        <div class="relative w-72 h-72 sm:w-88 sm:h-88 lg:w-96 lg:h-96 rounded-3xl p-2 glass-card flex items-center justify-center">
          <div id="hero-orb-canvas" class="w-full h-full rounded-2xl cursor-grab active:cursor-grabbing overflow-hidden"></div>
          <div class="absolute bottom-4 left-0 right-0 text-center pointer-events-none">
            <span class="px-3 py-1 rounded-full text-[10px] font-mono tracking-wider uppercase bg-black/40 dark:bg-black/60 text-white/80 backdrop-blur-md border border-white/10">
              Interactive 3D Neural Crystal &bull; Drag to Rotate
            </span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== EXECUTIVE DOSSIER: WHO I AM & PAID ROLES ==================== -->
  <section id="about" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-10">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Executive Dossier</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Identity, Focus & Availability</h2>
        <p class="text-sm text-appMuted">A direct, transparent overview of who I am, what I build, and what roles I am ready to undertake.</p>
      </div>

      <!-- 3-Pillar Clean SaaS Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Pillar 1: Who I Am -->
        <div class="glass-card p-6 sm:p-7 rounded-3xl space-y-4">
          <div class="w-12 h-12 rounded-2xl flex items-center justify-center bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">
            <i data-lucide="user-check" class="w-6 h-6"></i>
          </div>
          <h3 class="text-lg font-bold text-appText">Who I Am</h3>
          <p class="text-xs sm:text-sm text-appMuted leading-relaxed">
            I am <strong class="text-appText">Hajrah Saleha Kazi</strong>, a B.Tech CSE (AI & ML) student at <strong class="text-appText">Vishwakarma Institute of Technology (VIT), Pune</strong>. Previously graduated with First Class with Distinction from Trinity Polytechnic, maintaining <strong class="text-amber-600 dark:text-amber-400 font-semibold">College Rank 1 Topper across all six consecutive semesters</strong> (96.12% final semester).
          </p>
          <div class="pt-2 text-xs font-mono text-appMuted flex items-center gap-1.5">
            <i data-lucide="award" class="w-4 h-4 text-amber-500"></i>
            <span>Best Student Award recipient across depts.</span>
          </div>
        </div>

        <!-- Pillar 2: What I Do -->
        <div class="glass-card p-6 sm:p-7 rounded-3xl space-y-4">
          <div class="w-12 h-12 rounded-2xl flex items-center justify-center bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/20">
            <i data-lucide="cpu" class="w-6 h-6"></i>
          </div>
          <h3 class="text-lg font-bold text-appText">What I Do</h3>
          <p class="text-xs sm:text-sm text-appMuted leading-relaxed">
            I engineer <strong class="text-appText">real-time Computer Vision pipelines and multimodal Deep Learning architectures</strong>. Specializing in YOLOv11 edge inference (&lt;100ms latency), OpenCV video telemetry, audio acoustic feature analysis (MFCC), and privacy-preserving multimodal frameworks published in peer-reviewed journals.
          </p>
          <div class="pt-2 text-xs font-mono text-appMuted flex items-center gap-1.5">
            <i data-lucide="check-circle-2" class="w-4 h-4 text-sky-500"></i>
            <span>Published IJIRT Author &bull; 90% mAP@50 systems</span>
          </div>
        </div>

        <!-- Pillar 3: Open for Paid Roles (Clear & Explicit) -->
        <div class="glass-card p-6 sm:p-7 rounded-3xl space-y-4 border-2 border-sky-500/30 dark:border-sky-500/30">
          <div class="w-12 h-12 rounded-2xl flex items-center justify-center bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
            <i data-lucide="briefcase" class="w-6 h-6"></i>
          </div>
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-bold text-appText">Open for Paid Roles</h3>
            <span class="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 uppercase">
              Immediate
            </span>
          </div>
          <p class="text-xs sm:text-sm text-appMuted leading-relaxed">
            Actively looking for and open to <strong class="text-appText">Paid Internships, Part-Time Engineering Roles, Project-Based Contracts, and Freelance Consulting</strong> in AI/ML, Computer Vision, Full-Stack AI Integration, and Applied Data Science.
          </p>
          <div class="pt-2 space-y-1.5 text-xs text-appMuted">
            <div class="flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>Paid AI/ML Internships (In-Person / Remote)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>Part-Time Computer Vision / Backend Developer</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
              <span>Freelance Architecture & Research Prototyping</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== ANIMATED INTERACTIVE TERMINAL (HAJRAH-SALEHA-KAZI) ==================== -->
  <section id="terminal-section" class="py-12 px-4 md:px-8 relative z-10">
    <div class="max-w-4xl mx-auto">
      <div class="glass-card rounded-3xl overflow-hidden border shadow-xl" style="border-color: var(--border-line);">
        
        <!-- Terminal Header Bar (Clean, no vit-pune) -->
        <div class="px-5 py-3.5 border-b flex items-center justify-between" style="border-color: var(--border-line); background: rgba(0,0,0,0.03);">
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 rounded-full bg-rose-500/80"></div>
            <div class="w-3 h-3 rounded-full bg-amber-500/80"></div>
            <div class="w-3 h-3 rounded-full bg-emerald-500/80"></div>
            <span class="ml-2 font-mono text-xs text-appMuted flex items-center gap-1.5">
              <i data-lucide="terminal" class="w-3.5 h-3.5"></i>
              <span>hajrah-saleha-kazi:~ (zsh)</span>
            </span>
          </div>
          <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">
            INTERACTIVE SHELL
          </span>
        </div>

        <!-- Terminal Screen Output -->
        <div id="terminal-screen" class="p-5 font-mono text-xs sm:text-sm h-64 overflow-y-auto space-y-2 select-text"
             style="background: var(--bg-surface-solid); color: var(--text-primary);">
          <div id="terminal-history"></div>
          <div class="flex items-center gap-2 pt-1 text-appMuted">
            <span class="text-emerald-500 font-bold">hajrah-saleha-kazi:~$</span>
            <input type="text" id="terminal-input" autocomplete="off" spellcheck="false" placeholder="type 'roles', 'projects', 'stack', or 'help'..."
                   class="flex-1 bg-transparent border-none outline-none font-mono text-xs sm:text-sm text-appText focus:ring-0 p-0">
          </div>
        </div>

        <!-- Interactive Quick Action Chips -->
        <div class="p-3.5 border-t flex flex-wrap items-center gap-2" style="border-color: var(--border-line); background: rgba(0,0,0,0.02);">
          <span class="text-[10px] font-mono uppercase tracking-wider text-appMuted mr-1">Quick Run:</span>
          <button onclick="executeTerminalCommand('roles')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-emerald-600 dark:text-emerald-400 hover:bg-emerald-500/10 border-emerald-500/30 transition-colors">roles</button>
          <button onclick="executeTerminalCommand('projects')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-sky-600 dark:text-sky-400 hover:bg-sky-500/10 border-sky-500/30 transition-colors">projects</button>
          <button onclick="executeTerminalCommand('stack')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-purple-600 dark:text-purple-400 hover:bg-purple-500/10 border-purple-500/30 transition-colors">stack</button>
          <button onclick="executeTerminalCommand('education')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-amber-600 dark:text-amber-400 hover:bg-amber-500/10 border-amber-500/30 transition-colors">education</button>
          <button onclick="executeTerminalCommand('awards')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-amber-600 dark:text-amber-400 hover:bg-amber-500/10 border-amber-500/30 transition-colors">awards</button>
          <button onclick="executeTerminalCommand('certs')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-sky-600 dark:text-sky-400 hover:bg-sky-500/10 border-sky-500/30 transition-colors">certs</button>
          <button onclick="executeTerminalCommand('resume')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-appText hover:bg-black/5 dark:hover:bg-white/5 border-appBorder transition-colors">resume</button>
          <button onclick="executeTerminalCommand('clear')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-medium border text-rose-500 hover:bg-rose-500/10 border-rose-500/30 transition-colors ml-auto">clear</button>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== FLAGSHIP PROJECTS & RESEARCH SHOWCASE (PRIMARY SECTION) ==================== -->
  <section id="projects" class="py-20 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-12">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Primary Engineering Showcase</span>
          <h2 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-appText mt-1">Featured Projects & Research Hub</h2>
          <p class="text-sm text-appMuted mt-1.5 max-w-2xl">
            Real-world industrial computer vision, distributed algorithms in C, relational DBMS, explainable medical systems, and embedded robotics.
          </p>
        </div>
        <div class="flex items-center gap-2 self-start sm:self-auto">
          <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/20">
            10 Proven Systems
          </span>
        </div>
      </div>

      <!-- Category Filter Tabs -->
      <div class="flex flex-wrap items-center gap-2 border-b pb-4" style="border-color: var(--border-line);" id="project-filters">
        <button onclick="filterProjects('all', this)" class="project-filter-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all bg-appText text-appBg shadow-sm">All Projects (10)</button>
        <button onclick="filterProjects('cv', this)" class="project-filter-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all border text-appMuted hover:text-appText hover:border-sky-500" style="border-color: var(--border-line);">AI & Computer Vision (4)</button>
        <button onclick="filterProjects('systems', this)" class="project-filter-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all border text-appMuted hover:text-appText hover:border-sky-500" style="border-color: var(--border-line);">Systems, DBMS & Algorithmic (4)</button>
        <button onclick="filterProjects('research', this)" class="project-filter-btn px-4 py-2 rounded-full text-xs font-mono font-bold transition-all border text-appMuted hover:text-appText hover:border-sky-500" style="border-color: var(--border-line);">Research & Robotics (2)</button>
      </div>

      <!-- EXPANSIVE CASE-STUDY PROJECT LAYOUT -->
      <div class="space-y-8" id="projects-container">

        <!-- 1. NeuroCalm 2.0 (Flagship Published Research) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl border-2 border-amber-500/30 space-y-6" data-category="cv research">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <div class="lg:col-span-8 space-y-3">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/30 uppercase">
                  Published Research &bull; IJIRT
                </span>
                <span class="text-xs font-mono text-appMuted">Vol 12 Issue 11 &bull; Reg ID: 195871</span>
                <span class="text-xs font-mono text-emerald-600 dark:text-emerald-400 font-bold">&bull; Impact Factor 8.412</span>
              </div>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-appText">NeuroCalm 2.0 &mdash; Multimodal Risk Assessment</h3>
              <p class="text-sm text-appMuted leading-relaxed">
                Privacy-preserving multimodal mental health framework combining facial micro-expression analysis (fine-tuned YOLOv11 on the MEFC dataset), acoustic vocal tone cues (18-feature MFCC acoustic MLP), and conversational text sentiment (VADER + Google Gemini 2.x API) to compute real-time psychiatric risk scoring.
              </p>
              <div class="flex flex-wrap gap-2 pt-2">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['pytorch']} <span>PyTorch</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['yolo']} <span>YOLOv11</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['gemini']} <span>Google Gemini 2.x</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['opencv']} <span>OpenCV</span>
                </span>
              </div>
            </div>

            <!-- Live Telemetry Scorecard -->
            <div class="lg:col-span-4 grid grid-cols-2 gap-3 p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
              <div class="p-3 rounded-xl bg-white/60 dark:bg-black/40 text-center">
                <span class="text-[10px] font-mono text-appMuted uppercase block">Accuracy</span>
                <span class="text-2xl font-mono font-extrabold text-emerald-600 dark:text-emerald-400">94.2%</span>
                <span class="text-[9px] font-mono text-appMuted block mt-0.5">Multimodal Fused</span>
              </div>
              <div class="p-3 rounded-xl bg-white/60 dark:bg-black/40 text-center">
                <span class="text-[10px] font-mono text-appMuted uppercase block">Inference</span>
                <span class="text-2xl font-mono font-extrabold text-sky-600 dark:text-sky-400">&lt;120ms</span>
                <span class="text-[9px] font-mono text-appMuted block mt-0.5">End-to-End</span>
              </div>
              <div class="col-span-2 pt-1 flex items-center justify-between">
                <button onclick="openCertificateModal('certificates/1775094878694.jpeg', 'IJIRT Certificate &mdash; NeuroCalm', 'Registration ID: 195871 &bull; Impact Factor 8.412')" class="w-full py-2 rounded-xl text-xs font-mono font-bold text-amber-600 dark:text-amber-400 border border-amber-500/40 hover:bg-amber-500 hover:text-black transition-all flex items-center justify-center gap-1.5">
                  <i data-lucide="file-check-2" class="w-3.5 h-3.5"></i>
                  <span>Inspect IJIRT Publication Certificate</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. Right-Fit AI-CV (MESAKI Industry-Sponsored) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl border-2 border-sky-500/30 space-y-6" data-category="cv">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <div class="lg:col-span-8 space-y-3">
              <div class="flex flex-wrap items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/30 uppercase">
                  Industry-Sponsored &bull; MESAKI
                </span>
                <span class="text-xs font-mono text-emerald-600 dark:text-emerald-400 font-bold">● Active Production System</span>
                <span class="text-xs font-mono text-appMuted">6-Member Team Lead</span>
              </div>
              <h3 class="text-2xl sm:text-3xl font-extrabold text-appText">Right-Fit AI-CV &mdash; Industrial Defect Detection</h3>
              <p class="text-sm text-appMuted leading-relaxed">
                Production-grade computer vision suite developed for automated footwear manufacturing quality inspection. Processes live high-speed factory conveyor camera streams to detect adhesive inconsistencies, surface voids, and dimensional anomalies with sub-100ms response time.
              </p>
              <div class="flex flex-wrap gap-2 pt-2">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['yolo']} <span>YOLOv11</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['opencv']} <span>OpenCV</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['fastapi']} <span>FastAPI</span>
                </span>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  {tech_svgs['python']} <span>Python Edge</span>
                </span>
              </div>
            </div>

            <div class="lg:col-span-4 grid grid-cols-2 gap-3 p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
              <div class="p-3 rounded-xl bg-white/60 dark:bg-black/40 text-center">
                <span class="text-[10px] font-mono text-appMuted uppercase block">mAP@50</span>
                <span class="text-2xl font-mono font-extrabold text-appText">90%</span>
                <span class="text-[9px] font-mono text-appMuted block mt-0.5">High Precision</span>
              </div>
              <div class="p-3 rounded-xl bg-white/60 dark:bg-black/40 text-center">
                <span class="text-[10px] font-mono text-appMuted uppercase block">Latency</span>
                <span class="text-2xl font-mono font-extrabold text-emerald-600 dark:text-emerald-400">&lt;100ms</span>
                <span class="text-[9px] font-mono text-appMuted block mt-0.5">Real-Time Fluid</span>
              </div>
              <div class="col-span-2 text-center py-1">
                <span class="text-[11px] font-mono text-sky-600 dark:text-sky-400 font-bold">Deployed on Edge Docker Container</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. GoatAI (MESAKI) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="cv">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-purple-600 dark:text-purple-400">AI Research Project &bull; MESAKI</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">GoatAI &mdash; Multi-Class CCTV Livestock Surveillance</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Feb 2026 &ndash; Apr 2026</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Automated computer vision surveillance pipeline monitoring 20+ hours of continuous CCTV livestock footage across 4 behavioral classes at 15 FPS. Features automated behavioral anomaly triggers to notify farm veterinary supervisors of distress patterns.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Video Dataset</span>
              <span class="font-mono text-sm font-bold text-appText">20+ Hours</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Throughput</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">15 FPS Continuous</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">States Tracked</span>
              <span class="font-mono text-sm font-bold text-purple-600 dark:text-purple-400">4 Classes</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>YOLO, OpenCV, PyTorch, Video Telemetry Pipelines</span>
          </div>
        </div>

        <!-- 4. RecapBot (Cognizeal AI) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="cv">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-sky-600 dark:text-sky-400">AI Video Pipeline &bull; Cognizeal</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">RecapBot &mdash; 3-Stage AI Video Intelligence</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Jun 2025 &ndash; Dec 2025</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Automated video understanding pipeline executing speech-to-text transcription via Whisper, CV semantic keyframe extraction, and transformer-based extractive summarization. Condenses a 10-minute high-definition video into an actionable executive brief in under 2 minutes.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">10-Min Video</span>
              <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">&lt;2 Minutes</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Compression</span>
              <span class="font-mono text-sm font-bold text-appText">82% Volume</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">ASR Accuracy</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">96% Precision</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>Python, Whisper, Transformers, OpenCV, MoviePy, FastAPI</span>
          </div>
        </div>

        <!-- 5. Focus Pulse Elite (Rajavi Technologies) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="systems">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-amber-600 dark:text-amber-400">Analytics Engine &bull; Rajavi Tech</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">Focus Pulse Elite &mdash; Real-Time Telemetry Analytics</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Jun 2025 &ndash; Aug 2025</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Productivity telemetry analytics platform capturing 8 quantitative workflow indicators across active application focus time, input rates, and task completion metrics with 95% telemetry tracking reliability.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Indicators</span>
              <span class="font-mono text-sm font-bold text-appText">8 Quantitative</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Reliability</span>
              <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">95% Tracking</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Refresh</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">&lt;500ms</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>Python, Pandas, NumPy, Scikit-Learn, Streamlit, WebSockets</span>
          </div>
        </div>

        <!-- 6. Adaptive Bloom Filter (C Language Systems) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="systems research">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-rose-500">Core Systems &bull; C Language &bull; Algorithmic Optimization</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">Adaptive Bloom Filter for Dynamic Workloads</h3>
            </div>
            <span class="text-xs font-mono text-rose-500 font-bold">Research Prototype</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            High-performance memory-efficient data retrieval architecture implemented in pure C. Unlike standard static Bloom Filters, dynamically adapts filter capacity and reconfigures hash functions under shifting query workloads, reducing RAM overhead by ~38% while maintaining a false-positive rate under 1.2%. Includes interactive benchmark performance GUI.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Memory Saved</span>
              <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">~38% RAM</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">False Positive</span>
              <span class="font-mono text-sm font-bold text-appText">&lt;1.2% Rate</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Lookup Time</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">O(k) Deterministic</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>C, MurmurHash3, FNV-1a, GCC/MinGW, Performance Visualizer</span>
          </div>
        </div>

        <!-- 7. CivicAI (DBMS ML2302) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="systems">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-emerald-600 dark:text-emerald-400">DBMS Course ML2302 &bull; Relational Architecture</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">CivicAI &mdash; Smart Civic Complaint Management DBMS</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Enterprise DBMS</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Enterprise relational database system managing municipal complaint lifecycles (potholes, garbage, water leaks, streetlight failures). Architected with 11 normalized entities, 17 foreign key relationships (3NF), complex SQL queries, and PL/SQL triggers. Includes a machine learning priority scoring engine to optimize municipal resource dispatch.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Schema Entities</span>
              <span class="font-mono text-sm font-bold text-appText">11 Tables (3NF)</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Relationships</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">17 Foreign Keys</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">ML Alignment</span>
              <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">88% Urgency</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>MySQL Workbench, PL/SQL, Python, Scikit-Learn, FastAPI</span>
          </div>
        </div>

        <!-- 8. ClinCase (Java OOP ML2303) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="systems">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-amber-600 dark:text-amber-400">OOP Course ML2303 &bull; Medical Informatics</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">ClinCase &mdash; Clinical Case Modeling & Explainable Decision Support</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Java Enterprise</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Java-based clinical decision-support system for physicians. Encapsulates longitudinal patient histories into robust OOP domain models (Patient, Visit, LabResult, Medication, ClinicalEvent). Evaluates diagnostic parameters to detect contradictory treatments and issues explainable alerts via a Java Swing interface.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Domain Classes</span>
              <span class="font-mono text-sm font-bold text-appText">5 Core Abstractions</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">GUI Interface</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">Java Swing</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Contraindications</span>
              <span class="font-mono text-sm font-bold text-amber-600 dark:text-amber-400">100% Explainable</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>Java, OOP Design Patterns, Swing, Medical Rule Engine</span>
          </div>
        </div>

        <!-- 9. TeamMatch (Discrete Mathematics & Graph Combinatorics) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="systems">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-indigo-500">Discrete Mathematics &bull; Graph Theory &bull; Combinatorics</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">TeamMatch &mdash; Graph-Based Student Project Team Formation</h3>
            </div>
            <span class="text-xs font-mono text-appMuted">Combinatorial Solver</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Automated team formation engine applying Discrete Mathematics principles (sets, relations, combinatorics, and weighted graph matching). Builds a weighted compatibility graph between students based on skills and availability, evaluating potential teams with combinatorial set coverage and interactive relationship visualizations.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Matching Graph</span>
              <span class="font-mono text-sm font-bold text-appText">Weighted Bipartite</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Constraint Solver</span>
              <span class="font-mono text-sm font-bold text-indigo-500">Combinatorial</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Visualization</span>
              <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">Interactive D3/Canvas</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>TypeScript, Graph Theory, Combinatorics, Next.js</span>
          </div>
        </div>

        <!-- 10. NEXUS-X (Embedded Robotics & Spatial Intelligence) -->
        <div class="project-card glass-card p-6 sm:p-8 rounded-3xl space-y-4" data-category="cv research">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
            <div>
              <span class="text-[10px] font-mono font-bold uppercase text-amber-500">Hardware & AI Prototype &bull; Embedded Spatial Intelligence</span>
              <h3 class="text-xl sm:text-2xl font-bold text-appText">NEXUS-X &mdash; Adaptive Spatial Intelligence & Predictive Robotics</h3>
            </div>
            <span class="text-xs font-mono text-amber-500 font-bold">Work in Progress</span>
          </div>
          <p class="text-sm text-appMuted leading-relaxed">
            Tabletop experimental robotic prototype integrating ultrasonic sensing, servo-assisted directional scanning, and machine learning. An ESP32 collects distance measurements and telemeters wirelessly to a laptop AI core that constructs real-time occupancy grid mapping, builds spatial memory, and predicts approaching obstacle vectors.
          </p>
          <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Microcontroller</span>
              <span class="font-mono text-sm font-bold text-appText">ESP32 Dual-Core</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">Scan Range</span>
              <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">180&deg; Servo Sweep</span>
            </div>
            <div>
              <span class="text-[10px] font-mono text-appMuted block">AI Core</span>
              <span class="font-mono text-sm font-bold text-purple-600 dark:text-purple-400">Wireless Laptop AI</span>
            </div>
          </div>
          <div class="flex items-center gap-2 pt-1 text-xs font-mono text-appMuted">
            <span class="font-semibold text-appText">Tech:</span>
            <span>ESP32, C++ Firmware, Ultrasonic Sensors, Python AI, Spatial Grid Mapping</span>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- ==================== BIG TECH STACK & LOGOS MATRIX ==================== -->
  <section id="skills" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Technical Arsenal</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Big Tech Stack & Knowledge Matrix</h2>
        <p class="text-sm text-appMuted">Comprehensive mastery across core languages, deep learning frameworks, frontier LLMs, and embedded hardware.</p>
      </div>

      <!-- Categorized Tech Stack Cards with Authentic Logos -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Category 1: Programming Languages -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
            <div class="flex items-center gap-2.5">
              <div class="p-2 rounded-xl bg-amber-500/10 text-amber-600 dark:text-amber-400">
                <i data-lucide="code-2" class="w-5 h-5"></i>
              </div>
              <div>
                <h3 class="text-base font-bold text-appText">Languages</h3>
                <span class="text-[10px] font-mono text-appMuted">Core & Systems</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-appMuted">7 Core</span>
          </div>

          <div class="space-y-2.5">
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-amber-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['python']}
                <span class="text-xs font-bold text-appText">Python</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Advanced ML &bull; NumPy/Pandas</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-blue-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['cpp']}
                <span class="text-xs font-bold text-appText">C++</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Algorithms &bull; High Performance</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-slate-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['c']}
                <span class="text-xs font-bold text-appText">C</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Low-Level Memory &bull; Bloom Filter</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-rose-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['java']}
                <span class="text-xs font-bold text-appText">Java</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">OOP Patterns &bull; Swing GUI</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-yellow-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['js']}
                <span class="text-xs font-bold text-appText">JavaScript</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">ES6+ &bull; Async &bull; Web</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-blue-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['ts']}
                <span class="text-xs font-bold text-appText">TypeScript</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Strict Types &bull; Next.js</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-cyan-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['sql']}
                <span class="text-xs font-bold text-appText">SQL &bull; PL/SQL</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Relational 3NF &bull; Stored Procs</span>
            </div>
          </div>
        </div>

        <!-- Category 2: AI, Deep Learning & Vision -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
            <div class="flex items-center gap-2.5">
              <div class="p-2 rounded-xl bg-sky-500/10 text-sky-600 dark:text-sky-400">
                <i data-lucide="eye" class="w-5 h-5"></i>
              </div>
              <div>
                <h3 class="text-base font-bold text-appText">Computer Vision & ML</h3>
                <span class="text-[10px] font-mono text-appMuted">Neural Architectures</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-appMuted">6 Frameworks</span>
          </div>

          <div class="space-y-2.5">
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-amber-600/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['pytorch']}
                <span class="text-xs font-bold text-appText">PyTorch</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">CNNs, MLPs & Tensors</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-sky-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['yolo']}
                <span class="text-xs font-bold text-appText">YOLOv11 &bull; YOLOv26</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Real-Time Object Detection</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-emerald-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['opencv']}
                <span class="text-xs font-bold text-appText">OpenCV</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Frame Filtering & Stream</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-orange-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['tensorflow']}
                <span class="text-xs font-bold text-appText">TensorFlow</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Deep Models & Inference</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-yellow-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['huggingface']}
                <span class="text-xs font-bold text-appText">Hugging Face</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Transformers, Tokenizers</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-teal-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['fastapi']}
                <span class="text-xs font-bold text-appText">FastAPI</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Async Inference Endpoints</span>
            </div>
          </div>
        </div>

        <!-- Category 3: Frontier LLMs & Generative AI -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
            <div class="flex items-center gap-2.5">
              <div class="p-2 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400">
                <i data-lucide="sparkles" class="w-5 h-5"></i>
              </div>
              <div>
                <h3 class="text-base font-bold text-appText">Frontier LLMs & GenAI</h3>
                <span class="text-[10px] font-mono text-appMuted">Multimodal & Reasoning</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-appMuted">Top Tier</span>
          </div>

          <div class="space-y-2.5">
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-sky-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['gemini']}
                <span class="text-xs font-bold text-appText">Google Gemini 2.x</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Multimodal Vision & Audio</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-amber-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['claude']}
                <span class="text-xs font-bold text-appText">Claude 3.5 Sonnet</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Architectural Synthesis</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-emerald-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['openai']}
                <span class="text-xs font-bold text-appText">OpenAI GPT-4o</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Function Calling & Text</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-blue-600/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['deepseek']}
                <span class="text-xs font-bold text-appText">DeepSeek-V3 / R1</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Mathematical CoT</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-purple-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                <i data-lucide="link" class="w-5 h-5 text-purple-500"></i>
                <span class="text-xs font-bold text-appText">LangChain & RAG</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Vector Retrieval</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-rose-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                <i data-lucide="mic" class="w-5 h-5 text-rose-500"></i>
                <span class="text-xs font-bold text-appText">VADER & Whisper</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Speech & Sentiment</span>
            </div>
          </div>
        </div>

        <!-- Category 4: Web, Full-Stack & APIs -->
        <div class="glass-card p-6 rounded-3xl space-y-4">
          <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
            <div class="flex items-center gap-2.5">
              <div class="p-2 rounded-xl bg-emerald-500/10 text-emerald-600 dark:text-emerald-400">
                <i data-lucide="layers" class="w-5 h-5"></i>
              </div>
              <div>
                <h3 class="text-base font-bold text-appText">Full-Stack & APIs</h3>
                <span class="text-[10px] font-mono text-appMuted">Web & Endpoints</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-appMuted">Production</span>
          </div>

          <div class="space-y-2.5">
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-cyan-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['react']}
                <span class="text-xs font-bold text-appText">React 19</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Reactive Interfaces</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-slate-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['nextjs']}
                <span class="text-xs font-bold text-appText">Next.js 15</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">App Router & SSR</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-emerald-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['nodejs']}
                <span class="text-xs font-bold text-appText">Node.js</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Asynchronous Services</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-amber-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                <i data-lucide="activity" class="w-5 h-5 text-amber-500"></i>
                <span class="text-xs font-bold text-appText">WebSockets</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Bi-Directional Telemetry</span>
            </div>
            <div class="flex items-center justify-between p-2.5 rounded-xl bg-black/5 dark:bg-white/5 hover:border-orange-500/40 border border-transparent transition-all">
              <div class="flex items-center gap-2.5">
                {tech_svgs['git']}
                <span class="text-xs font-bold text-appText">Git & GitHub</span>
              </div>
              <span class="text-[10px] font-mono text-appMuted">Version Control & CI/CD</span>
            </div>
          </div>
        </div>

        <!-- Category 5: Embedded Systems & Hardware Rig -->
        <div class="glass-card p-6 rounded-3xl space-y-4 md:col-span-2 lg:col-span-2">
          <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
            <div class="flex items-center gap-2.5">
              <div class="p-2 rounded-xl bg-indigo-500/10 text-indigo-600 dark:text-indigo-400">
                <i data-lucide="cpu" class="w-5 h-5"></i>
              </div>
              <div>
                <h3 class="text-base font-bold text-appText">Robotics, Embedded Systems & Hardware Setup</h3>
                <span class="text-[10px] font-mono text-appMuted">Microcontrollers, Sensors & Engineering Workstation</span>
              </div>
            </div>
            <span class="text-xs font-mono font-bold text-appMuted">Setup</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3.5 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 space-y-1">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  {tech_svgs['esp32']}
                  <span class="text-xs font-bold text-appText">ESP32 &bull; Arduino</span>
                </div>
                <span class="text-[10px] font-mono text-sky-600 dark:text-sky-400 font-bold">Dual-Core</span>
              </div>
              <p class="text-[11px] text-appMuted">Ultrasonic sensors, PWM servo actuators, wireless spatial telemetry for NEXUS-X.</p>
            </div>

            <div class="p-3.5 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 space-y-1">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <i data-lucide="laptop" class="w-5 h-5 text-emerald-500"></i>
                  <span class="text-xs font-bold text-appText">Lenovo IdeaPad Slim 3</span>
                </div>
                <span class="text-[10px] font-mono text-emerald-600 dark:text-emerald-400 font-bold">24GB RAM</span>
              </div>
              <p class="text-[11px] text-appMuted">Intel Core i5 &bull; 24GB High-Bandwidth RAM &bull; 1TB NVMe SSD for fast local neural training.</p>
            </div>

            <div class="p-3.5 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 space-y-1">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <i data-lucide="tablet" class="w-5 h-5 text-purple-500"></i>
                  <span class="text-xs font-bold text-appText">Apple iPad Pro + Apple Pencil</span>
                </div>
                <span class="text-[10px] font-mono text-purple-600 dark:text-purple-400 font-bold">Prototyping</span>
              </div>
              <p class="text-[11px] text-appMuted">System schematics, UI/UX interaction wireframing, and mathematical derivation notes.</p>
            </div>

            <div class="p-3.5 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 space-y-1">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <i data-lucide="terminal" class="w-5 h-5 text-amber-500"></i>
                  <span class="text-xs font-bold text-appText">VS Code &bull; GCC/MinGW</span>
                </div>
                <span class="text-[10px] font-mono text-amber-600 dark:text-amber-400 font-bold">Toolchain</span>
              </div>
              <p class="text-[11px] text-appMuted">MSYS2 GCC/MinGW, Casio FX-991CW Classwiz for numerical algorithm verification.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Live Interactive Edge Inference Benchmark Simulator -->
      <div class="glass-card p-6 sm:p-8 rounded-3xl border space-y-6" style="border-color: var(--border-line);">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-4" style="border-color: var(--border-line);">
          <div>
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <h3 class="text-lg font-bold text-appText">YOLOv11 Edge Inference Benchmark Simulator</h3>
            </div>
            <p class="text-xs text-appMuted mt-0.5">Simulate real-time computer vision latency, framerate, and mAP across hardware configurations.</p>
          </div>
          <span class="text-xs font-mono font-bold text-sky-600 dark:text-sky-400 bg-sky-500/10 px-3 py-1 rounded-full border border-sky-500/20 self-start sm:self-auto">
            Interactive Testbed
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
          <div class="md:col-span-6 space-y-4">
            <div>
              <div class="flex justify-between text-xs font-mono mb-1.5">
                <span class="text-appMuted">Hardware Target:</span>
                <span id="benchmark-hw-name" class="font-bold text-appText">Edge CPU (Lenovo i5)</span>
              </div>
              <input type="range" id="benchmark-slider" min="1" max="4" value="2" step="1"
                     class="w-full h-2 bg-black/10 dark:bg-white/10 rounded-lg appearance-none cursor-pointer accent-sky-500">
              <div class="flex justify-between text-[10px] font-mono text-appMuted mt-1">
                <span>ESP32 / MCU</span>
                <span>Edge CPU</span>
                <span>GPU Workstation</span>
                <span>TensorRT Cluster</span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2 pt-2">
              <button onclick="setBenchmarkPreset(1)" class="p-2 rounded-xl text-xs font-mono border text-center hover:border-sky-500 transition-colors" style="border-color: var(--border-line);">
                YOLOv11-Nano (MESAKI)
              </button>
              <button onclick="setBenchmarkPreset(3)" class="p-2 rounded-xl text-xs font-mono border text-center hover:border-sky-500 transition-colors" style="border-color: var(--border-line);">
                NeuroCalm Multimodal
              </button>
            </div>
          </div>

          <div class="md:col-span-6 grid grid-cols-3 gap-3">
            <div class="p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">Latency</span>
              <span id="metric-latency" class="text-2xl font-mono font-extrabold text-emerald-600 dark:text-emerald-400">42ms</span>
              <span class="text-[9px] font-mono text-appMuted block mt-1">Sub-100ms Cap</span>
            </div>
            <div class="p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">Throughput</span>
              <span id="metric-fps" class="text-2xl font-mono font-extrabold text-sky-600 dark:text-sky-400">24 FPS</span>
              <span class="text-[9px] font-mono text-appMuted block mt-1">Real-Time Fluid</span>
            </div>
            <div class="p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">Detection</span>
              <span id="metric-map" class="text-2xl font-mono font-extrabold text-amber-600 dark:text-amber-400">90.2%</span>
              <span class="text-[9px] font-mono text-appMuted block mt-1">mAP@50 Metric</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== PROFESSIONAL EXPERIENCE TIMELINE ==================== -->
  <section id="experience" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-5xl mx-auto space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Career Progression & Impact</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Professional Experience Timeline</h2>
        <p class="text-sm text-appMuted">Proven track record of shipping production computer vision systems and leading technical teams.</p>
      </div>

      <!-- Vertical Timeline Container -->
      <div class="relative pl-6 sm:pl-10 space-y-10">
        
        <!-- Continuous Vertical Timeline Spine -->
        <div class="absolute left-3 sm:left-5 top-4 bottom-4 w-0.5 bg-gradient-to-b from-emerald-500 via-sky-500 via-purple-500 to-amber-500/40"></div>

        <!-- Timeline Item 1: MESAKI Lead Developer (Sep 2026 - Present) -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-emerald-500 text-white ring-4 ring-emerald-500/20 transition-transform group-hover:scale-110">
            <i data-lucide="zap" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl border-2 border-emerald-500/30 relative overflow-hidden space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <span class="font-mono text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wide">Industry-Sponsored Project &bull; MESAKI</span>
                <h3 class="text-xl sm:text-2xl font-bold text-appText">AI/ML Lead Developer &mdash; Right-Fit AI-CV</h3>
              </div>
              <div class="text-left sm:text-right">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                  <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                  <span>Sep 2026 &ndash; Present</span>
                </span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Leading a 6-member engineering team developing an automated real-time Computer Vision quality assurance suite for footwear manufacturing. Designed a low-latency YOLOv11 defect detection architecture analyzing surface adhesive consistency on factory conveyor lines.
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-1">
              <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                <span class="text-[10px] font-mono text-appMuted block">Accuracy Metric</span>
                <span class="text-lg font-mono font-bold text-appText">90% mAP@50</span>
              </div>
              <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                <span class="text-[10px] font-mono text-appMuted block">Inference Speed</span>
                <span class="text-lg font-mono font-bold text-emerald-600 dark:text-emerald-400">&lt;100ms</span>
              </div>
              <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                <span class="text-[10px] font-mono text-appMuted block">Team Scale</span>
                <span class="text-lg font-mono font-bold text-appText">6 Engineers</span>
              </div>
              <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                <span class="text-[10px] font-mono text-appMuted block">Stack</span>
                <span class="text-xs font-mono font-bold text-sky-600 dark:text-sky-400">YOLO, OpenCV, FastAPI</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Timeline Item 2: MESAKI AI Research Intern (Feb 2026 - Apr 2026) -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-sky-500/10 text-sky-600 dark:text-sky-400 border-sky-500/30 transition-transform group-hover:scale-110" style="background: var(--bg-surface);">
            <i data-lucide="scan" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <span class="font-mono text-xs font-bold text-sky-600 dark:text-sky-400 uppercase tracking-wide">AI Research / Project Lead &bull; MESAKI</span>
                <h3 class="text-xl font-bold text-appText">AI Research Intern &mdash; GoatAI</h3>
              </div>
              <div class="text-left sm:text-right">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-medium text-appMuted bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                  <i data-lucide="calendar" class="w-3 h-3"></i>
                  <span>Feb 2026 &ndash; Apr 2026</span>
                </span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Spearheaded development of an automated livestock computer vision surveillance framework. Processed 20+ hours of continuous CCTV footage across 4 behavioral classes at 15 FPS, engineering an anomaly trigger pipeline for veterinary health alerts.
            </p>
            <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Video Dataset</span>
                <span class="font-mono text-sm font-bold text-appText">20+ Hours</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Throughput</span>
                <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">15 FPS Continuous</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">States Tracked</span>
                <span class="font-mono text-sm font-bold text-purple-600 dark:text-purple-400">4 Classes</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Timeline Item 3: Cognizeal AI Intern (Jun 2025 - Dec 2025) -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-purple-500/10 text-purple-600 dark:text-purple-400 border-purple-500/30 transition-transform group-hover:scale-110" style="background: var(--bg-surface);">
            <i data-lucide="video" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <span class="font-mono text-xs font-bold text-purple-600 dark:text-purple-400 uppercase tracking-wide">Cognizeal</span>
                <h3 class="text-xl font-bold text-appText">AI Intern / Lead Developer &mdash; RecapBot</h3>
              </div>
              <div class="text-left sm:text-right">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-medium text-appMuted bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                  <i data-lucide="calendar" class="w-3 h-3"></i>
                  <span>Jun 2025 &ndash; Dec 2025</span>
                </span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Architected a 3-stage automated video intelligence pipeline (audio transcription, semantic keyframe extraction, extractive summarization) that processes a 10-minute high-definition video in under 2 minutes.
            </p>
            <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Processing Speed</span>
                <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">&lt;2 Min / 10-Min Video</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Compression</span>
                <span class="font-mono text-sm font-bold text-appText">82% Volume</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">ASR Precision</span>
                <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">96% Accuracy</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Timeline Item 4: Rajavi Technologies Data Science Intern (Jun 2025 - Aug 2025) -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/30 transition-transform group-hover:scale-110" style="background: var(--bg-surface);">
            <i data-lucide="bar-chart-2" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <span class="font-mono text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wide">Rajavi Technologies</span>
                <h3 class="text-xl font-bold text-appText">Data Science Intern &mdash; Focus Pulse Elite</h3>
              </div>
              <div class="text-left sm:text-right">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-medium text-appMuted bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
                  <i data-lucide="calendar" class="w-3 h-3"></i>
                  <span>Jun 2025 &ndash; Aug 2025</span>
                </span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Engineered an employee productivity analytics platform tracking 8 quantitative indicators with 95% telemetry tracking reliability, providing real-time team workflow focus metrics.
            </p>
            <div class="grid grid-cols-3 gap-3 p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-center">
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Workflow Indicators</span>
                <span class="font-mono text-sm font-bold text-appText">8 Quantitative</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Tracking Reliability</span>
                <span class="font-mono text-sm font-bold text-emerald-600 dark:text-emerald-400">95% Reliability</span>
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted block">Telemetry Refresh</span>
                <span class="font-mono text-sm font-bold text-sky-600 dark:text-sky-400">&lt;500ms</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== COMPACT INSTAGRAM-STORY TROPHY & AWARDS RACK ==================== -->
  <section id="trophies" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-8">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">Academic & Technical Honors</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Honors & Trophy Story Rack</h2>
          <p class="text-sm text-appMuted mt-1">Tap any story ring to launch the interactive, full-screen story player.</p>
        </div>
        <button onclick="playAllStories()" class="self-start sm:self-auto px-4 py-2 rounded-full text-xs font-semibold flex items-center gap-2 border hover:border-amber-500 transition-all"
                style="background: var(--bg-surface); border-color: var(--border-line);">
          <i data-lucide="play-circle" class="w-4 h-4 text-amber-500"></i>
          <span>Play Full Story Reel</span>
        </button>
      </div>

      <div class="glass-card p-4 sm:p-5 rounded-3xl overflow-x-auto">
        <div class="flex items-center gap-4 sm:gap-6 min-w-max px-2" id="story-avatars-row"></div>
      </div>

      <div class="glass-card rounded-3xl p-6 sm:p-8 grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        <div class="md:col-span-5 relative rounded-2xl overflow-hidden aspect-[4/3] bg-black/5 dark:bg-black/40 border border-black/5 dark:border-white/5">
          <img id="spotlight-img" src="Trophys n awards/1776913249349.jpeg" alt="Trophy Highlight" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
          <span class="absolute bottom-3 left-3 px-2.5 py-1 rounded-full text-[10px] font-mono font-bold bg-amber-500 text-black shadow-md uppercase">
            Featured Honor
          </span>
        </div>
        <div class="md:col-span-7 space-y-3">
          <div class="flex items-center gap-2 text-xs font-mono text-amber-600 dark:text-amber-400">
            <i data-lucide="award" class="w-4 h-4"></i>
            <span id="spotlight-inst">Trinity Polytechnic Pune &bull; A.Y. 2025–26</span>
          </div>
          <h3 class="text-2xl font-extrabold text-appText" id="spotlight-title">Best Out Going Student Award</h3>
          <p class="text-sm text-appMuted leading-relaxed" id="spotlight-desc">
            Conferred to Hajrah Saleha Imran Kazi (Computer Engineering Department). College Rank 1 overall across six consecutive semesters with a final semester score of 96.12%.
          </p>
          <div class="flex items-center gap-3 pt-3">
            <button onclick="openStoryModal(currentSpotlightIndex)" class="px-5 py-2.5 rounded-full text-xs font-semibold flex items-center gap-2 shadow-sm"
                    style="background: var(--cta-btn-bg); color: var(--cta-btn-text);">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>View Full Story</span>
            </button>
            <div class="flex items-center gap-1">
              <button onclick="prevSpotlight()" class="p-2 rounded-full border text-appMuted hover:text-appText transition-colors" style="border-color: var(--border-line);">
                <i data-lucide="chevron-left" class="w-4 h-4"></i>
              </button>
              <button onclick="nextSpotlight()" class="p-2 rounded-full border text-appMuted hover:text-appText transition-colors" style="border-color: var(--border-line);">
                <i data-lucide="chevron-right" class="w-4 h-4"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== THE BOOKSHELF & VISIONARY DESIGNERS STUDIO ==================== -->
  <section id="bookshelf" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-10">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">Literary & Creative Venture</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">The Bookshelf & Creative Studio</h2>
        <p class="text-sm text-appMuted">First student-author from the college to publish a book &bull; Founder of Visionary Designers Co.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        
        <div class="md:col-span-5 flex justify-center">
          <div class="relative group cursor-pointer" onclick="openBookModal()">
            <div class="w-64 sm:w-72 rounded-2xl overflow-hidden shadow-2xl border transition-transform duration-500 group-hover:scale-105 group-hover:-rotate-1"
                 style="border-color: var(--border-line);">
              <img src="./prices of me still whole book-pic.jpeg" alt="Pieces of Me, Still Whole Book Cover" class="w-full h-auto object-cover">
            </div>
            <span class="absolute -bottom-3 -right-3 px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-500 text-black shadow-lg">
              1-Year Anniversary
            </span>
          </div>
        </div>

        <div class="md:col-span-7 space-y-6">
          <div class="space-y-2">
            <span class="text-xs font-mono text-amber-600 dark:text-amber-400">Published Author &bull; Released June 2025</span>
            <h3 class="text-2xl sm:text-3xl font-serif font-bold text-appText">Pieces of Me, Still Whole</h3>
            <p class="text-sm text-appMuted leading-relaxed">
              Celebrated its one-year self-publishing anniversary in June 2026. A deeply reflective collection of poetry and prose exploring human resilience, intellectual growth, and quiet strength through academic and personal tribulations.
            </p>
            <blockquote class="border-l-2 border-amber-500 pl-4 py-1 italic font-serif text-sm text-appText">
              "We fracture under pressure only to assemble ourselves into something far more deliberate, far more unbreakable."
            </blockquote>
          </div>

          <!-- Visionary Designers Co. with Direct Official Link -->
          <div class="p-5 rounded-2xl border space-y-3" style="background: var(--bg-surface); border-color: var(--border-line);">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2 text-xs font-mono text-purple-600 dark:text-purple-400 font-bold">
                <i data-lucide="palette" class="w-4 h-4"></i>
                <span>Visionary Designers Co. &bull; Founder & Creative Director</span>
              </div>
              <a href="https://visionarydesignersco.com/" target="_blank" rel="noopener noreferrer" 
                 class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-semibold bg-purple-600 text-white hover:bg-purple-700 transition-colors shadow-sm">
                <span>visionarydesignersco.com</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
            <p class="text-xs text-appMuted leading-relaxed">
              Independent digital branding and design studio delivering typography systems, UI/UX interaction design, and creative tech direction for modern software applications and academic ventures.
            </p>
          </div>

          <div class="flex items-center gap-3">
            <button onclick="openBookModal()" class="px-5 py-2.5 rounded-full text-xs font-semibold flex items-center gap-2 shadow-sm"
                    style="background: var(--cta-btn-bg); color: var(--cta-btn-text);">
              <i data-lucide="book-open" class="w-3.5 h-3.5"></i>
              <span>Read Synopsis</span>
            </button>
            <a href="https://visionarydesignersco.com/" target="_blank" rel="noopener noreferrer" 
               class="px-4 py-2.5 rounded-full text-xs font-semibold border flex items-center gap-2 text-purple-600 dark:text-purple-400 border-purple-500/30 hover:bg-purple-500/10 transition-colors">
              <i data-lucide="globe" class="w-3.5 h-3.5"></i>
              <span>Studio Portfolio</span>
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== PROMINENT EDUCATION SHOWCASE & TIMELINE ==================== -->
  <section id="education" class="py-16 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-5xl mx-auto space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-amber-600 dark:text-amber-400">Academic Foundation & Milestone Track</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Education & Academic Timeline</h2>
        <p class="text-sm text-appMuted">From international schooling to collegiate rank-1 topper and advanced B.Tech in AI & Machine Learning.</p>
      </div>

      <!-- Vertical Timeline Container -->
      <div class="relative pl-6 sm:pl-10 space-y-10">
        
        <!-- Continuous Vertical Timeline Spine -->
        <div class="absolute left-3 sm:left-5 top-4 bottom-4 w-0.5 bg-gradient-to-b from-sky-500 via-amber-500 to-slate-400/40"></div>

        <!-- 1. VIT Pune (2026 - 2029) - ON TOP AS REQUESTED -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-sky-500 text-white ring-4 ring-sky-500/20 transition-transform group-hover:scale-110">
            <i data-lucide="graduation-cap" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl border-2 border-sky-500/40 space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <div class="flex items-center gap-2">
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-sky-500/10 text-sky-600 dark:text-sky-400 border border-sky-500/20 uppercase">
                    Direct Second-Year (DSE) &bull; Ongoing
                  </span>
                  <span class="text-xs font-mono font-bold text-sky-600 dark:text-sky-400">2026 &ndash; 2029</span>
                </div>
                <h3 class="text-2xl font-extrabold text-appText mt-1">Vishwakarma Institute of Technology (VIT), Pune</h3>
                <p class="text-sm font-semibold text-sky-600 dark:text-sky-400">
                  B.Tech in Computer Science & Engineering (Artificial Intelligence & Machine Learning)
                </p>
              </div>
              <span class="text-xs font-mono font-bold px-3 py-1 rounded-full bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText self-start sm:self-auto">
                Undergraduate Degree
              </span>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Secured admission into VIT Pune's premier AI & ML division. Coursework and specialized research cover Advanced Deep Learning, High-Performance Computer Vision, Discrete Mathematics & Graph Theory, Relational Database Management Systems, and Embedded Edge Intelligence.
            </p>
            <div class="flex flex-wrap gap-2 pt-1 text-xs font-mono text-appMuted">
              <span class="px-2.5 py-1 rounded-lg bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">AI & Machine Learning Specialization</span>
              <span class="px-2.5 py-1 rounded-lg bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">Direct Second Year Entry</span>
              <span class="px-2.5 py-1 rounded-lg bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">Computer Vision & Edge AI</span>
            </div>
          </div>
        </div>

        <!-- 2. Trinity Polytechnic Pune (2023 - 2026) - SECOND AS REQUESTED -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-amber-500 text-black ring-4 ring-amber-500/20 transition-transform group-hover:scale-110">
            <i data-lucide="award" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-8 rounded-3xl border-2 border-amber-500/40 relative overflow-hidden space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-3 border-b pb-4" style="border-color: var(--border-line);">
              <div>
                <div class="flex items-center gap-2">
                  <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-amber-500 text-black uppercase">
                    College Rank 1 Topper (All 6 Semesters)
                  </span>
                  <span class="text-xs font-mono font-bold text-amber-600 dark:text-amber-400">2023 &ndash; 2026</span>
                </div>
                <h3 class="text-2xl font-extrabold text-appText mt-1">Trinity Polytechnic Pune</h3>
                <p class="text-sm font-semibold text-amber-600 dark:text-amber-400">
                  Diploma in Computer Engineering &bull; First Class with Distinction
                </p>
              </div>
              <div class="text-left sm:text-right">
                <span class="text-2xl font-mono font-extrabold text-amber-600 dark:text-amber-400 block">96.12%</span>
                <span class="text-[10px] font-mono text-appMuted">Final Semester Aggregate</span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Maintained the <strong class="text-appText">College Rank 1 position across all engineering branches for all six consecutive semesters</strong>. Conferred the prestigious <strong class="text-appText">Best Out Going Student Award (2025–26)</strong> and <strong class="text-appText">Best Student Award (2024–25)</strong> for exemplary scholarship and leadership.
            </p>
            <div class="pt-2 flex flex-wrap items-center gap-3">
              <button onclick="openCertificateModal('certificates/1728649891977.jpeg', 'Diploma Certificate &mdash; Trinity Polytechnic', 'First Class with Distinction &bull; College Rank 1 Topper across all six semesters')" class="px-4 py-2 rounded-full text-xs font-semibold flex items-center gap-1.5 border border-amber-500/40 hover:bg-amber-500 hover:text-black transition-all">
                <i data-lucide="file-check" class="w-3.5 h-3.5"></i>
                <span>View Diploma Certificate</span>
              </button>
              <button onclick="openStoryModal(0)" class="px-4 py-2 rounded-full text-xs font-semibold flex items-center gap-1.5 text-appMuted hover:text-appText transition-colors">
                <i data-lucide="award" class="w-3.5 h-3.5 text-amber-500"></i>
                <span>View Best Student Award</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3. Oysters International School (2023 Batch for IGCSEs) - THIRD AS REQUESTED -->
        <div class="relative group">
          <!-- Timeline Node / Icon -->
          <div class="absolute -left-6 sm:-left-10 top-1.5 w-6 h-6 sm:w-10 sm:h-10 rounded-xl sm:rounded-2xl flex items-center justify-center border shadow-md bg-slate-500/10 text-slate-600 dark:text-slate-300 border-slate-500/30 transition-transform group-hover:scale-110" style="background: var(--bg-surface);">
            <i data-lucide="book-open" class="w-3.5 h-3.5 sm:w-5 sm:h-5"></i>
          </div>

          <!-- Card Content -->
          <div class="glass-card p-6 sm:p-7 rounded-3xl space-y-3">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b pb-3" style="border-color: var(--border-line);">
              <div>
                <span class="text-[10px] font-mono font-bold uppercase text-slate-500 dark:text-slate-400">Secondary Education &bull; Cambridge Board</span>
                <h3 class="text-xl font-bold text-appText">Oysters International School</h3>
              </div>
              <div class="text-left sm:text-right">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-mono font-bold bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-appText">
                  <i data-lucide="calendar" class="w-3 h-3"></i>
                  <span>2023 Batch (IGCSE)</span>
                </span>
              </div>
            </div>
            <p class="text-sm text-appMuted leading-relaxed">
              Completed the International General Certificate of Secondary Education (IGCSE) with comprehensive STEM foundation covering Mathematics, Physics, Chemistry, Biology, English, and Information & Communication Technology (ICT).
            </p>
            <div class="flex flex-wrap gap-2 pt-1 text-xs font-mono text-appMuted">
              <span class="px-2.5 py-0.5 rounded-md bg-black/5 dark:bg-white/5 text-appText">Mathematics</span>
              <span class="px-2.5 py-0.5 rounded-md bg-black/5 dark:bg-white/5 text-appText">Physics</span>
              <span class="px-2.5 py-0.5 rounded-md bg-black/5 dark:bg-white/5 text-appText">Chemistry</span>
              <span class="px-2.5 py-0.5 rounded-md bg-black/5 dark:bg-white/5 text-appText">Biology</span>
              <span class="px-2.5 py-0.5 rounded-md bg-black/5 dark:bg-white/5 text-appText">ICT & Computing</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== VERIFIED CERTIFICATIONS SCROLLER (DUAL-TRACK) ==================== -->
  <section id="certificates" class="py-16 px-4 md:px-8 relative z-10 border-t overflow-hidden" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-10">
      
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Verified Credentials</span>
          <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Certifications & Accreditations Vault</h2>
          <p class="text-sm text-appMuted mt-1">Infinite dual-track marquee showcasing 24 verified certifications from Tata Group, AWS, IBM, Cisco, ISRO, and IIT Bombay. Hover to pause &bull; Click any credential to expand.</p>
        </div>
        <div class="flex items-center gap-2 self-start sm:self-auto">
          <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">
            24 Verified Seals
          </span>
        </div>
      </div>

      <div class="relative w-full overflow-hidden py-2">
        <div class="flex gap-4 marquee-track animate-marquee w-max">
          {track1_html}
        </div>
      </div>

      <div class="relative w-full overflow-hidden py-2">
        <div class="flex gap-4 marquee-track animate-marquee-reverse w-max">
          {track2_html}
        </div>
      </div>

    </div>
  </section>

  <!-- ==================== CONNECT & BUILD TOGETHER (WITH REAL BRAND LOGOS) ==================== -->
  <section id="contact" class="py-20 px-4 md:px-8 relative z-10 border-t" style="border-color: var(--border-line);">
    <div class="max-w-6xl mx-auto space-y-12">
      
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <span class="text-xs font-mono font-bold uppercase tracking-wider text-sky-600 dark:text-sky-400">Direct Collaboration</span>
        <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-appText">Let's Connect & Build Together</h2>
        <p class="text-sm text-appMuted">Open for paid internships, freelance contracts, part-time engineering roles, and AI research collaborations.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Left: Verified Contact Cards with Real Official Brand Logos -->
        <div class="lg:col-span-5 space-y-3.5">
          
          <!-- LinkedIn -->
          <a href="https://www.linkedin.com/in/hajrah-saleha-kazi" target="_blank" rel="noopener noreferrer"
             class="glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between group transition-all hover:scale-[1.02] hover:border-[#0A66C2] block">
            <div class="flex items-center gap-3.5">
              <div class="p-2.5 rounded-xl bg-[#0A66C2]/10 border border-[#0A66C2]/20 flex items-center justify-center">
                {social_svgs['linkedin']}
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">LinkedIn Profile</span>
                <span class="text-sm font-bold text-appText group-hover:text-[#0A66C2] transition-colors">in/hajrah-saleha-kazi</span>
              </div>
            </div>
            <i data-lucide="external-link" class="w-4 h-4 text-appMuted group-hover:text-[#0A66C2] transition-colors"></i>
          </a>

          <!-- GitHub -->
          <a href="https://github.com/hajrah-kazi" target="_blank" rel="noopener noreferrer"
             class="glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between group transition-all hover:scale-[1.02] hover:border-appText block">
            <div class="flex items-center gap-3.5">
              <div class="p-2.5 rounded-xl bg-black/10 dark:bg-white/10 border border-black/10 dark:border-white/10 flex items-center justify-center text-appText">
                {social_svgs['github']}
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">GitHub Repositories</span>
                <span class="text-sm font-bold text-appText group-hover:underline transition-colors">github.com/hajrah-kazi</span>
              </div>
            </div>
            <i data-lucide="external-link" class="w-4 h-4 text-appMuted group-hover:text-appText transition-colors"></i>
          </a>

          <!-- Gmail -->
          <a href="mailto:hajrahsalehak@gmail.com"
             class="glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between group transition-all hover:scale-[1.02] hover:border-[#EA4335] block">
            <div class="flex items-center gap-3.5">
              <div class="p-2.5 rounded-xl bg-[#EA4335]/10 border border-[#EA4335]/20 flex items-center justify-center">
                {social_svgs['gmail']}
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">Official Email</span>
                <span class="text-sm font-bold text-appText group-hover:text-[#EA4335] transition-colors">hajrahsalehak@gmail.com</span>
              </div>
            </div>
            <span class="text-xs font-mono text-emerald-600 dark:text-emerald-400 font-bold">Mail &rarr;</span>
          </a>

          <!-- WhatsApp Direct -->
          <a href="https://wa.me/919860336250" target="_blank" rel="noopener noreferrer"
             class="glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between group transition-all hover:scale-[1.02] hover:border-[#25D366] block">
            <div class="flex items-center gap-3.5">
              <div class="p-2.5 rounded-xl bg-[#25D366]/10 border border-[#25D366]/20 flex items-center justify-center">
                {social_svgs['whatsapp']}
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">WhatsApp &bull; Phone</span>
                <span class="text-sm font-bold text-appText group-hover:text-[#25D366] transition-colors">+91 9860336250</span>
              </div>
            </div>
            <span class="text-xs font-mono text-[#25D366] font-bold">Chat &rarr;</span>
          </a>

          <!-- Location -->
          <div class="glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between">
            <div class="flex items-center gap-3.5">
              <div class="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center">
                {social_svgs['location']}
              </div>
              <div>
                <span class="text-[10px] font-mono text-appMuted uppercase tracking-wider block">Location / Coordinates</span>
                <span class="text-sm font-bold text-appText">Pune, Maharashtra, India</span>
              </div>
            </div>
            
          </div>

        </div>

        <!-- Right: Direct Message Dispatch Prompt -->
        <div class="lg:col-span-7">
          <form id="contact-form" onsubmit="handleContactSubmit(event)" class="glass-card p-6 sm:p-8 rounded-3xl space-y-4">
            <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
              <h3 class="text-lg font-bold text-appText">Send a Direct Inquiry</h3>
              <span class="text-xs font-mono text-emerald-600 dark:text-emerald-400 font-bold">Fast Response Guarantee</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="space-y-1">
                <label class="text-xs font-mono text-appMuted">Your Name *</label>
                <input type="text" id="contact-name" required placeholder="Dr. Jane Doe / Alex Smith"
                       class="w-full px-4 py-2.5 rounded-xl border text-xs sm:text-sm text-appText bg-transparent outline-none focus:border-sky-500"
                       style="border-color: var(--border-line);">
              </div>
              <div class="space-y-1">
                <label class="text-xs font-mono text-appMuted">Email Address *</label>
                <input type="email" id="contact-email" required placeholder="jane@company.com"
                       class="w-full px-4 py-2.5 rounded-xl border text-xs sm:text-sm text-appText bg-transparent outline-none focus:border-sky-500"
                       style="border-color: var(--border-line);">
              </div>
            </div>

            <div class="space-y-1">
              <label class="text-xs font-mono text-appMuted">Opportunity / Inquiry Type</label>
              <select id="contact-type" class="w-full px-4 py-2.5 rounded-xl border text-xs sm:text-sm text-appText bg-transparent outline-none focus:border-sky-500"
                      style="border-color: var(--border-line);">
                <option value="Paid Internship" class="bg-slate-900 text-white">Paid Internship Opportunity</option>
                <option value="Part-Time Role" class="bg-slate-900 text-white">Part-Time Engineering Role</option>
                <option value="Freelance Project" class="bg-slate-900 text-white">Freelance / Contract AI Project</option>
                <option value="Research Collaboration" class="bg-slate-900 text-white">Research Collaboration & Paper</option>
                <option value="Speaking / Advisory" class="bg-slate-900 text-white">Speaking / Creative Mentorship</option>
              </select>
            </div>

            <div class="space-y-1">
              <label class="text-xs font-mono text-appMuted">Your Message *</label>
              <textarea id="contact-msg" required rows="4" placeholder="Describe the role, project scope, or opportunity..."
                        class="w-full px-4 py-2.5 rounded-xl border text-xs sm:text-sm text-appText bg-transparent outline-none focus:border-sky-500"
                        style="border-color: var(--border-line);"></textarea>
            </div>

            <button type="submit" class="w-full py-3 rounded-xl text-xs sm:text-sm font-semibold flex items-center justify-center gap-2 shadow-md hover:scale-[1.01] active:scale-95 transition-all"
                    style="background: var(--cta-btn-bg); color: var(--cta-btn-text);">
              <i data-lucide="send" class="w-4 h-4"></i>
              <span>Dispatch Message to Hajrah</span>
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>

  <!-- ==================== FOOTER ==================== -->
  <footer class="py-12 px-4 md:px-8 border-t relative z-10" style="border-color: var(--border-line); background: var(--bg-surface);">
    <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-appMuted font-mono">
      <div class="flex items-center gap-2">
        <img src="./HSK.png" alt="HSK Monogram" class="w-5 h-5 rounded-full">
        <span>&copy; 2026 Hajrah Saleha Kazi. All rights reserved.</span>
      </div>
      <div id="pune-clock" class="text-sky-600 dark:text-sky-400 font-bold">Pune IST: --:--:--</div>
      <div class="flex items-center gap-3">
        <a href="#hero" class="hover:text-appText transition-colors">Back to Top &uarr;</a>
      </div>
    </div>
  </footer>

  <!-- ==================== MODALS ==================== -->

  <!-- 1. Instagram Story Modal -->
  <div id="story-modal" class="fixed inset-0 z-[100] bg-black/95 backdrop-blur-2xl hidden flex-col items-center justify-center p-4">
    <div class="relative w-full max-w-md h-[88vh] max-h-[750px] bg-slate-950 rounded-3xl overflow-hidden border border-white/10 shadow-2xl flex flex-col justify-between">
      <div class="absolute top-3 left-3 right-3 flex gap-1 z-30" id="story-progress-container"></div>

      <div class="absolute top-7 left-4 right-4 flex items-center justify-between z-30">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-full border border-amber-400 overflow-hidden">
            <img src="./HSK.png" alt="HSK" class="w-full h-full object-cover">
          </div>
          <div>
            <h4 class="text-xs font-bold text-white leading-tight">Hajrah Saleha Kazi</h4>
            <span class="text-[9px] font-mono text-amber-400" id="story-header-date">A.Y. 2025–26</span>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="toggleStoryPlay()" class="p-1 rounded text-white/80 hover:text-white" id="story-pause-btn">
            <i data-lucide="pause" class="w-4 h-4" id="story-play-icon"></i>
          </button>
          <button onclick="closeStoryModal()" class="p-1 rounded text-white/80 hover:text-white">
            <i data-lucide="x" class="w-5 h-5"></i>
          </button>
        </div>
      </div>

      <div class="relative flex-1 flex items-center justify-center overflow-hidden bg-black cursor-pointer" onclick="handleStoryTap(event)">
        <img id="story-image" src="" alt="Story Award" class="w-full h-full object-contain">
      </div>

      <div class="relative z-30 p-5 bg-gradient-to-t from-black via-black/90 to-transparent space-y-1 text-white">
        <span class="font-mono text-[10px] text-sky-400 uppercase tracking-wide" id="story-institution">Trinity Polytechnic Pune</span>
        <h3 class="text-base font-bold text-white" id="story-title">Award Title</h3>
        <p class="text-[11px] text-slate-300 font-light line-clamp-3 leading-relaxed" id="story-desc">Award description...</p>
        <div class="pt-2 flex items-center justify-between text-[10px] font-mono text-slate-400 border-t border-white/10 mt-2">
          <span class="flex items-center gap-1">
            <i data-lucide="sparkles" class="w-3 h-3 text-amber-400"></i> Tap left/right to navigate
          </span>
          <span id="story-counter">1 / 9</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 2. Certificate Lightbox Modal -->
  <div id="cert-modal" class="fixed inset-0 z-[100] bg-black/95 backdrop-blur-2xl hidden flex-col items-center justify-center p-4">
    <div class="relative max-w-3xl w-full glass-card rounded-3xl overflow-hidden border shadow-2xl p-4 sm:p-6 space-y-4" style="background: var(--bg-surface-solid);">
      <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
        <div class="flex items-center gap-2">
          <i data-lucide="shield-check" class="w-5 h-5 text-amber-500"></i>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-appText">Verified Credential Inspection</span>
        </div>
        <button onclick="closeCertModal()" class="p-1 rounded-full text-appMuted hover:text-appText">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="max-h-[65vh] overflow-hidden rounded-2xl border flex items-center justify-center bg-black/5 dark:bg-black/60" style="border-color: var(--border-line);">
        <img id="cert-modal-img" src="" alt="Verified Certificate" class="max-w-full max-h-[62vh] object-contain">
      </div>

      <div class="space-y-1">
        <h3 class="text-lg font-bold text-appText" id="cert-modal-title">Certificate Title</h3>
        <p class="text-xs text-appMuted font-light" id="cert-modal-desc">Issuing details</p>
      </div>
    </div>
  </div>

  <!-- 3. Verified Resume Modal (With Confetti Action) -->
  <div id="resume-modal" class="fixed inset-0 z-[100] bg-black/95 backdrop-blur-2xl hidden flex-col items-center justify-center p-4">
    <div class="relative max-w-4xl w-full h-[90vh] glass-card rounded-3xl overflow-hidden border shadow-2xl flex flex-col" style="background: var(--bg-surface-solid);">
      <div class="flex items-center justify-between p-4 border-b" style="border-color: var(--border-line);">
        <div class="flex items-center gap-2.5">
          <div class="w-3 h-3 rounded-full bg-emerald-500"></div>
          <div>
            <h3 class="text-base font-bold text-appText">Hajrah Saleha Kazi &mdash; Verified Resume</h3>
            <span class="text-[10px] font-mono text-appMuted">Official PDF Document &bull; Validated Portfolio CV</span>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <a href="./Hajrah_Saleha_Kazi_Resume_v3.pdf" download="Hajrah_Saleha_Kazi_Resume.pdf" onclick="triggerConfetti()"
             class="px-3.5 py-1.5 rounded-full text-xs font-semibold flex items-center gap-1.5 bg-emerald-600 text-white hover:bg-emerald-700 transition-colors shadow-sm">
            <i data-lucide="download" class="w-3.5 h-3.5"></i>
            <span>Download PDF</span>
          </a>
          <button onclick="closeResumeModal()" class="p-1 rounded-full text-appMuted hover:text-appText">
            <i data-lucide="x" class="w-5 h-5"></i>
          </button>
        </div>
      </div>
      <div class="flex-1 bg-slate-900 overflow-hidden">
        <iframe src="./Hajrah_Saleha_Kazi_Resume_v3.pdf#toolbar=1" class="w-full h-full border-none"></iframe>
      </div>
    </div>
  </div>

  <!-- 4. Book Modal -->
  <div id="book-modal" class="fixed inset-0 z-[100] bg-black/95 backdrop-blur-2xl hidden flex-col items-center justify-center p-4">
    <div class="relative max-w-2xl w-full glass-card rounded-3xl overflow-hidden border shadow-2xl p-6 space-y-4" style="background: var(--bg-surface-solid);">
      <div class="flex items-center justify-between border-b pb-3" style="border-color: var(--border-line);">
        <div class="flex items-center gap-2">
          <i data-lucide="book" class="w-5 h-5 text-amber-500"></i>
          <span class="text-xs font-mono font-bold uppercase tracking-wider text-appText">Pieces of Me, Still Whole</span>
        </div>
        <button onclick="closeBookModal()" class="p-1 rounded-full text-appMuted hover:text-appText">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      <div class="flex flex-col sm:flex-row gap-5 items-center">
        <img src="./prices of me still whole book-pic.jpeg" alt="Book Cover" class="w-40 rounded-xl shadow-lg border" style="border-color: var(--border-line);">
        <div class="space-y-3">
          <h3 class="text-xl font-serif font-bold text-appText">Pieces of Me, Still Whole</h3>
          <span class="font-mono text-xs text-amber-600 dark:text-amber-400 block">By Hajrah Saleha Kazi &bull; Celebrated 1-Year Anniversary</span>
          <p class="text-xs text-appMuted leading-relaxed">
            A published literary work exploring self-reconstruction, resilience, and personal evolution. Written by Hajrah Saleha Kazi as the first student-author from her college, it stands as testament to balancing deep technical rigor with creative humanities.
          </p>
          <div class="pt-2">
            <a href="https://visionarydesignersco.com/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 text-xs font-mono text-purple-600 dark:text-purple-400 hover:underline">
              <span>Visit visionarydesignersco.com &rarr;</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ==================== JAVASCRIPT LOGIC ==================== -->
  <script>
    const certData = {cert_json_str};
    const trophyStories = {trophy_json_str};

    let isSoundEnabled = true;
    let audioCtx = null;
    let currentStoryIndex = 0;
    let storyTimer = null;
    let storyDuration = 4500;
    let isStoryPaused = false;
    let currentSpotlightIndex = 0;

    // --- THEME ENGINE ---
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const htmlElement = document.documentElement;

    function initTheme() {{
      const saved = localStorage.getItem('hsk_theme');
      if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
        htmlElement.classList.add('dark');
        htmlElement.classList.remove('light');
      }} else {{
        htmlElement.classList.add('light');
        htmlElement.classList.remove('dark');
      }}
    }}
    initTheme();

    themeToggleBtn.addEventListener('click', () => {{
      playTone(520, 'sine', 0.1);
      if (htmlElement.classList.contains('dark')) {{
        htmlElement.classList.remove('dark');
        htmlElement.classList.add('light');
        localStorage.setItem('hsk_theme', 'light');
      }} else {{
        htmlElement.classList.remove('light');
        htmlElement.classList.add('dark');
        localStorage.setItem('hsk_theme', 'dark');
      }}
      lucide.createIcons();
    }});

    // --- MOBILE MENU ---
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenuBtn.addEventListener('click', () => {{
      mobileMenu.classList.toggle('hidden');
    }});
    function closeMobileMenu() {{
      mobileMenu.classList.add('hidden');
    }}

    // --- DYNAMIC TYPEWRITER (HERO) ---
    const typeStrings = [
      "engineer sub-100ms edge AI systems.",
      "build real-time computer vision pipelines.",
      "fine-tune multimodal deep neural architectures.",
      "write books and publish peer-reviewed AI research.",
      "solve low-latency systems problems in C & Python."
    ];
    let typeIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    const typeEl = document.getElementById('dynamic-typewriter');

    function typeDynamicText() {{
      const current = typeStrings[typeIdx];
      if (isDeleting) {{
        typeEl.textContent = current.substring(0, charIdx - 1);
        charIdx--;
      }} else {{
        typeEl.textContent = current.substring(0, charIdx + 1);
        charIdx++;
      }}

      let delay = isDeleting ? 30 : 65;

      if (!isDeleting && charIdx === current.length) {{
        delay = 2000;
        isDeleting = true;
      }} else if (isDeleting && charIdx === 0) {{
        isDeleting = false;
        typeIdx = (typeIdx + 1) % typeStrings.length;
        delay = 400;
      }}

      setTimeout(typeDynamicText, delay);
    }}
    typeDynamicText();

    // --- PUNE CLOCK ---
    function updatePuneClock() {{
      const options = {{ timeZone: 'Asia/Kolkata', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' }};
      const now = new Date().toLocaleTimeString('en-US', options);
      const clockEl = document.getElementById('pune-clock');
      if (clockEl) clockEl.textContent = 'Pune IST: ' + now;
    }}
    setInterval(updatePuneClock, 1000);
    updatePuneClock();

    // --- WEB AUDIO SYNTHESIZER ---
    function initAudio() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}
    }}
    function playTone(freq, type = 'sine', duration = 0.12, gainVal = 0.04) {{
      if (!isSoundEnabled) return;
      try {{
        initAudio();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch(e) {{}}
    }}
    const soundToggleBtn = document.getElementById('sound-toggle-btn');
    soundToggleBtn.addEventListener('click', () => {{
      isSoundEnabled = !isSoundEnabled;
      const icon = document.getElementById('sound-icon');
      if (isSoundEnabled) {{
        icon.setAttribute('data-lucide', 'volume-2');
        playTone(660, 'sine', 0.15);
      }} else {{
        icon.setAttribute('data-lucide', 'volume-x');
      }}
      lucide.createIcons();
    }});

    // --- CONFETTI ENGINE ---
    function triggerConfetti() {{
      if (typeof confetti === 'function') {{
        confetti({{
          particleCount: 90,
          spread: 75,
          origin: {{ y: 0.6 }},
          colors: ['#0284c7', '#d97706', '#7c3aed', '#10b981', '#f59e0b']
        }});
      }}
    }}
    function triggerResumeWithConfetti() {{
      triggerConfetti();
      openResumeModal();
    }}

    // --- THREE.JS MESMERIZING 3D NEURAL CRYSTAL SPHERE ---
    function initCleanOrb() {{
      const container = document.getElementById('hero-orb-canvas');
      if (!container) return;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      camera.position.z = 4.2;

      const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true }});
      renderer.setSize(container.clientWidth, container.clientHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      container.appendChild(renderer.domElement);

      // Group to rotate together
      const masterGroup = new THREE.Group();
      scene.add(masterGroup);

      // 1. Inner Geodesic Wireframe
      const innerGeo = new THREE.IcosahedronGeometry(1.2, 2);
      const innerMat = new THREE.MeshBasicMaterial({{
        color: 0x0284c7,
        wireframe: true,
        transparent: true,
        opacity: 0.35
      }});
      const innerMesh = new THREE.Mesh(innerGeo, innerMat);
      masterGroup.add(innerMesh);

      // 2. Outer Neural Particle Swarm
      const particleCount = 1400;
      const positions = new Float32Array(particleCount * 3);
      const colors = new Float32Array(particleCount * 3);

      const colorCyan = new THREE.Color('#00f0ff');
      const colorGold = new THREE.Color('#d4af37');
      const colorPurple = new THREE.Color('#a855f7');

      for (let i = 0; i < particleCount; i++) {{
        const phi = Math.acos(-1 + (2 * i) / particleCount);
        const theta = Math.sqrt(particleCount * Math.PI) * phi;
        const radius = 1.35 + (Math.random() - 0.5) * 0.35;

        positions[i * 3] = radius * Math.cos(theta) * Math.sin(phi);
        positions[i * 3 + 1] = radius * Math.sin(theta) * Math.sin(phi);
        positions[i * 3 + 2] = radius * Math.cos(phi);

        const r = Math.random();
        const col = r < 0.4 ? colorCyan : (r < 0.75 ? colorGold : colorPurple);
        colors[i * 3] = col.r;
        colors[i * 3 + 1] = col.g;
        colors[i * 3 + 2] = col.b;
      }}

      const particleGeo = new THREE.BufferGeometry();
      particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

      const particleMat = new THREE.PointsMaterial({{
        size: 0.042,
        vertexColors: true,
        transparent: true,
        opacity: 0.88
      }});

      const particleSystem = new THREE.Points(particleGeo, particleMat);
      masterGroup.add(particleSystem);

      // 3. Floating Orbital Equatorial Rings
      const ringGeo = new THREE.RingGeometry(1.5, 1.52, 64);
      const ringMat = new THREE.MeshBasicMaterial({{
        color: 0x0284c7,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.4
      }});
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);
      ringMesh.rotation.x = Math.PI / 3;
      masterGroup.add(ringMesh);

      // Mouse Drag Interaction
      let isDragging = false;
      let prevMousePos = {{ x: 0, y: 0 }};
      container.addEventListener('mousedown', (e) => {{
        isDragging = true;
        prevMousePos = {{ x: e.clientX, y: e.clientY }};
      }});
      window.addEventListener('mouseup', () => isDragging = false);
      window.addEventListener('mousemove', (e) => {{
        if (!isDragging) return;
        const deltaX = e.clientX - prevMousePos.x;
        const deltaY = e.clientY - prevMousePos.y;
        masterGroup.rotation.y += deltaX * 0.007;
        masterGroup.rotation.x += deltaY * 0.007;
        prevMousePos = {{ x: e.clientX, y: e.clientY }};
      }});

      // Touch Drag Support for Mobile & Tablets
      container.addEventListener('touchstart', (e) => {{
        if (e.touches.length === 1) {{
          isDragging = true;
          prevMousePos = {{ x: e.touches[0].clientX, y: e.touches[0].clientY }};
        }}
      }}, {{ passive: true }});
      window.addEventListener('touchend', () => isDragging = false, {{ passive: true }});
      window.addEventListener('touchmove', (e) => {{
        if (!isDragging || e.touches.length !== 1) return;
        const deltaX = e.touches[0].clientX - prevMousePos.x;
        const deltaY = e.touches[0].clientY - prevMousePos.y;
        masterGroup.rotation.y += deltaX * 0.007;
        masterGroup.rotation.x += deltaY * 0.007;
        prevMousePos = {{ x: e.touches[0].clientX, y: e.touches[0].clientY }};
      }}, {{ passive: true }});

      function animate() {{
        requestAnimationFrame(animate);
        if (!isDragging) {{
          masterGroup.rotation.y += 0.0028;
          masterGroup.rotation.x += 0.0014;
        }}
        ringMesh.rotation.z += 0.003;
        renderer.render(scene, camera);
      }}
      animate();

      window.addEventListener('resize', () => {{
        if (!container.clientWidth) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      }});
    }}
    window.addEventListener('DOMContentLoaded', initCleanOrb);

    // --- BENCHMARK SIMULATOR ---
    const benchmarkSlider = document.getElementById('benchmark-slider');
    const benchmarkData = [
      {{ hw: 'ESP32 / MCU', latency: '210ms', fps: '4.8 FPS', map: '84.5%' }},
      {{ hw: 'Edge CPU (Lenovo i5)', latency: '42ms', fps: '24 FPS', map: '90.2%' }},
      {{ hw: 'GPU Workstation (RTX)', latency: '12ms', fps: '83 FPS', map: '92.4%' }},
      {{ hw: 'TensorRT Cluster', latency: '4.5ms', fps: '220 FPS', map: '94.8%' }}
    ];

    function updateBenchmarkUI(val) {{
      const d = benchmarkData[val - 1];
      document.getElementById('benchmark-hw-name').textContent = d.hw;
      document.getElementById('metric-latency').textContent = d.latency;
      document.getElementById('metric-fps').textContent = d.fps;
      document.getElementById('metric-map').textContent = d.map;
    }}
    if (benchmarkSlider) {{
      benchmarkSlider.addEventListener('input', (e) => {{
        updateBenchmarkUI(parseInt(e.target.value));
        playTone(400 + parseInt(e.target.value) * 60, 'triangle', 0.05);
      }});
    }}
    function setBenchmarkPreset(val) {{
      if (benchmarkSlider) {{
        benchmarkSlider.value = val;
        updateBenchmarkUI(val);
        playTone(520, 'sine', 0.1);
      }}
    }}

    // --- PROJECTS FILTER ---
    function filterProjects(cat, elem) {{
      playTone(540, 'sine', 0.08);
      const btns = document.querySelectorAll('.project-filter-btn');
      btns.forEach(b => {{
        b.classList.remove('bg-appText', 'text-appBg');
        b.classList.add('text-appMuted');
      }});
      const targetBtn = elem || (window.event ? window.event.target : null);
      if (targetBtn) {{
        targetBtn.classList.add('bg-appText', 'text-appBg');
        targetBtn.classList.remove('text-appMuted');
      }}

      const cards = document.querySelectorAll('.project-card');
      cards.forEach(card => {{
        const categories = card.getAttribute('data-category');
        if (cat === 'all' || categories.includes(cat)) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // --- INSTAGRAM-STORY REEL LOGIC ---
    function renderStoryAvatars() {{
      const row = document.getElementById('story-avatars-row');
      if (!row) return;
      row.innerHTML = '';

      trophyStories.forEach((st, i) => {{
        const div = document.createElement('div');
        div.className = 'flex flex-col items-center gap-1.5 cursor-pointer group';
        div.onclick = () => {{
          playTone(600, 'sine', 0.1);
          setSpotlight(i);
          openStoryModal(i);
        }};

        div.innerHTML = `
          <div class="relative w-16 h-16 sm:w-18 sm:h-18 p-[2.5px] rounded-full story-gradient-ring transition-transform duration-300 group-hover:scale-110">
            <div class="w-full h-full rounded-full overflow-hidden bg-black border-2 border-white dark:border-slate-900">
              <img src="${{st.file}}" alt="${{st.title}}" class="w-full h-full object-cover">
            </div>
          </div>
          <span class="text-[10px] font-mono text-appMuted max-w-[70px] truncate text-center group-hover:text-appText transition-colors">
            ${{st.title}}
          </span>
        `;
        row.appendChild(div);
      }});
    }}
    renderStoryAvatars();

    function setSpotlight(idx) {{
      currentSpotlightIndex = idx;
      const s = trophyStories[idx];
      document.getElementById('spotlight-img').src = s.file;
      document.getElementById('spotlight-title').textContent = s.title;
      document.getElementById('spotlight-inst').textContent = `${{s.institution}} &bull; ${{s.date}}`;
      document.getElementById('spotlight-desc').textContent = s.desc;
    }}
    function nextSpotlight() {{
      setSpotlight((currentSpotlightIndex + 1) % trophyStories.length);
      playTone(550, 'sine', 0.08);
    }}
    function prevSpotlight() {{
      setSpotlight((currentSpotlightIndex - 1 + trophyStories.length) % trophyStories.length);
      playTone(550, 'sine', 0.08);
    }}

    // Fullscreen Story Player
    function openStoryModal(idx = 0) {{
      playTone(640, 'sine', 0.1);
      currentStoryIndex = idx;
      document.getElementById('story-modal').classList.remove('hidden');
      document.getElementById('story-modal').classList.add('flex');
      setupStoryBars();
      renderStory();
      startStory();
    }}
    function closeStoryModal() {{
      clearInterval(storyTimer);
      document.getElementById('story-modal').classList.add('hidden');
      document.getElementById('story-modal').classList.remove('flex');
    }}
    function playAllStories() {{
      openStoryModal(0);
    }}
    function setupStoryBars() {{
      const container = document.getElementById('story-progress-container');
      container.innerHTML = '';
      trophyStories.forEach((_, i) => {{
        const barBg = document.createElement('div');
        barBg.className = 'flex-1 h-1 bg-white/30 rounded-full overflow-hidden';
        barBg.innerHTML = `<div id="story-bar-${{i}}" class="h-full bg-amber-400 w-0 transition-all duration-100"></div>`;
        container.appendChild(barBg);
      }});
    }}
    function renderStory() {{
      const s = trophyStories[currentStoryIndex];
      document.getElementById('story-image').src = s.file;
      document.getElementById('story-title').textContent = s.title;
      document.getElementById('story-institution').textContent = s.institution;
      document.getElementById('story-desc').textContent = s.desc;
      document.getElementById('story-header-date').textContent = s.date;
      document.getElementById('story-counter').textContent = `${{currentStoryIndex + 1}} / ${{trophyStories.length}}`;

      for (let i = 0; i < trophyStories.length; i++) {{
        const b = document.getElementById(`story-bar-${{i}}`);
        if (!b) continue;
        if (i < currentStoryIndex) b.style.width = '100%';
        else if (i === currentStoryIndex) b.style.width = '0%';
        else b.style.width = '0%';
      }}
    }}
    function startStory() {{
      clearInterval(storyTimer);
      isStoryPaused = false;
      let elapsed = 0;
      const interval = 50;
      const currentBar = document.getElementById(`story-bar-${{currentStoryIndex}}`);

      storyTimer = setInterval(() => {{
        if (isStoryPaused) return;
        elapsed += interval;
        const pct = Math.min((elapsed / storyDuration) * 100, 100);
        if (currentBar) currentBar.style.width = pct + '%';

        if (elapsed >= storyDuration) {{
          clearInterval(storyTimer);
          if (currentStoryIndex < trophyStories.length - 1) {{
            currentStoryIndex++;
            renderStory();
            startStory();
          }} else {{
            closeStoryModal();
          }}
        }}
      }}, interval);
    }}
    function toggleStoryPlay() {{
      isStoryPaused = !isStoryPaused;
      const icon = document.getElementById('story-play-icon');
      icon.setAttribute('data-lucide', isStoryPaused ? 'play' : 'pause');
      lucide.createIcons();
    }}
    function handleStoryTap(e) {{
      const rect = e.currentTarget.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      if (clickX < rect.width / 2) {{
        if (currentStoryIndex > 0) {{
          currentStoryIndex--;
          renderStory();
          startStory();
        }}
      }} else {{
        if (currentStoryIndex < trophyStories.length - 1) {{
          currentStoryIndex++;
          renderStory();
          startStory();
        }} else {{
          closeStoryModal();
        }}
      }}
    }}

    // --- CERTIFICATE LIGHTBOX MODAL ---
    function openCertificateModal(imgSrc, title, desc) {{
      playTone(600, 'sine', 0.1);
      document.getElementById('cert-modal-img').src = imgSrc;
      document.getElementById('cert-modal-title').textContent = title;
      document.getElementById('cert-modal-desc').textContent = desc;
      document.getElementById('cert-modal').classList.remove('hidden');
      document.getElementById('cert-modal').classList.add('flex');
    }}
    function closeCertModal() {{
      document.getElementById('cert-modal').classList.add('hidden');
      document.getElementById('cert-modal').classList.remove('flex');
    }}

    // --- RESUME & BOOK MODALS ---
    function openResumeModal() {{
      playTone(620, 'sine', 0.1);
      document.getElementById('resume-modal').classList.remove('hidden');
      document.getElementById('resume-modal').classList.add('flex');
    }}
    function closeResumeModal() {{
      document.getElementById('resume-modal').classList.add('hidden');
      document.getElementById('resume-modal').classList.remove('flex');
    }}
    function openBookModal() {{
      playTone(580, 'sine', 0.1);
      document.getElementById('book-modal').classList.remove('hidden');
      document.getElementById('book-modal').classList.add('flex');
    }}
    function closeBookModal() {{
      document.getElementById('book-modal').classList.add('hidden');
      document.getElementById('book-modal').classList.remove('flex');
    }}

    // --- ANIMATED INTERACTIVE TERMINAL (HAJRAH-SALEHA-KAZI) ---
    const termHistory = document.getElementById('terminal-history');
    const termInput = document.getElementById('terminal-input');

    const terminalCommands = {{
      help: `AVAILABLE COMMANDS:
  &bull; roles      : View open paid roles, internships & freelance availability
  &bull; projects   : Summary of key AI & systems projects with metrics
  &bull; stack      : Core languages, CV frameworks, and LLM proficiencies
  &bull; education  : Academic credentials (VIT Pune & Trinity Rank 1)
  &bull; awards     : Summary of collegiate awards & SIH hackathon victory
  &bull; certs      : 24 verified certifications status
  &bull; resume     : Launch verified resume viewer
  &bull; contact    : Email, phone, LinkedIn & WhatsApp coordinates
  &bull; clear      : Clear terminal history`,

      roles: `HAJRAH SALEHA KAZI &mdash; AVAILABILITY STATUS: [IMMEDIATE]
  &bull; Paid AI/ML Internships (In-Person / Remote)
  &bull; Part-Time Computer Vision / Deep Learning Engineering
  &bull; Freelance Architecture & Edge Deployment Contracts
  &bull; Applied Research Projects & Multimodal Framework Prototyping
  Compensation: Competitive paid compensation commensurate with value.`,

      projects: `KEY ENGINEERING PROJECTS:
  1. NeuroCalm 2.0 (Published Research IJIRT) &bull; 94.2% Accuracy, &lt;120ms
  2. Right-Fit AI-CV (MESAKI Lead) &bull; 90% mAP@50, &lt;100ms
  3. GoatAI (MESAKI) &bull; 20+ hrs CCTV, 15 FPS, 4 behavioral classes
  4. RecapBot (Cognizeal) &bull; 10 min video in &lt;2 min (Whisper + CV)
  5. Focus Pulse Elite (Rajavi) &bull; 8 metrics, 95% telemetry reliability
  6. Adaptive Bloom Filter (C Language) &bull; ~38% RAM reduction, &lt;1.2% FP
  7. CivicAI (DBMS) &bull; 11 tables, 17 foreign keys, ML priority scoring
  8. ClinCase (Java OOP) &bull; 5 domain models, explainable decision alerts
  9. TeamMatch (Discrete Math) &bull; Weighted graph compatibility solver
  10. NEXUS-X (Robotics) &bull; ESP32 dual-core, 180&deg; ultrasonic spatial sweep`,

      stack: `BIG TECH STACK MATRIX:
  &bull; Languages: Python, C++, C, Java, JavaScript, TypeScript, SQL, Bash
  &bull; AI / CV: PyTorch, YOLOv11/v26, OpenCV, TensorFlow, Scikit-Learn, HF
  &bull; LLMs / GenAI: Gemini 2.x, Claude 3.5 Sonnet, GPT-4o, DeepSeek-V3/R1, LangChain
  &bull; Systems & Full-Stack: FastAPI, React, Next.js 15, Node.js, WebSockets, MySQL
  &bull; Hardware / Embedded: ESP32, Arduino, Ultrasonic Arrays, Lenovo i5 (24GB RAM)`,

      education: `ACADEMIC HONORS & DEGREES:
  &bull; B.Tech CSE (AI & ML) &bull; Vishwakarma Institute of Technology (VIT), Pune (2026&ndash;2029)
  &bull; Diploma in Computer Engineering &bull; Trinity Polytechnic (First Class with Distinction)
    Score: 96.12% Final Semester | COLLEGE RANK 1 TOPPER (All 6 Consecutive Semesters)
  &bull; Secondary IGCSE &bull; Oysters International School (2023 Batch)`,

      awards: `AWARDS & HONORS:
  &bull; Best Out Going Student Award &bull; Trinity Polytechnic (A.Y. 2025–26)
  &bull; Best Student Award Overall &bull; KJEI Trinity Polytechnic (A.Y. 2024–25)
  &bull; 1st Prize Winner &bull; Smart India Hackathon 2025 Internal Hackathon
  &bull; Published Author &bull; 'Pieces of Me, Still Whole' (First student-author)`,

      certs: `CERTIFICATION VAULT:
  &bull; 24 Verified Certificates indexed on disk.
  &bull; Issuers: Tata Group iQ, AWS, IBM, TCS iON, Cisco, ISRO, IIT Bombay, Stanford.`,

      resume: `[SYSTEM] Launching Verified Resume Viewer...`,
      contact: `CONTACT DETAILS:
  &bull; Email: hajrahsalehak@gmail.com
  &bull; WhatsApp: https://wa.me/919860336250
  &bull; LinkedIn: https://www.linkedin.com/in/hajrah-saleha-kazi
  &bull; GitHub: https://github.com/hajrah-kazi
  &bull; Location: Pune, Maharashtra, India`
    }};

    function printTerminal(cmd, output) {{
      const div = document.createElement('div');
      div.className = 'space-y-1 mb-2';
      div.innerHTML = `
        <div class="text-sky-600 dark:text-sky-400 font-bold flex items-center gap-1">
          <span>hajrah-saleha-kazi:~$</span>
          <span class="text-appText">${{cmd}}</span>
        </div>
        <div class="text-appMuted whitespace-pre-line pl-2 leading-relaxed text-xs">${{output}}</div>
      `;
      termHistory.appendChild(div);
      const scr = document.getElementById('terminal-screen');
      scr.scrollTop = scr.scrollHeight;
    }}

    function executeTerminalCommand(cmd) {{
      playTone(500, 'sine', 0.08);
      cmd = cmd.trim().toLowerCase();
      if (!cmd) return;

      if (cmd === 'clear') {{
        termHistory.innerHTML = '';
        return;
      }}
      if (cmd === 'resume') {{
        printTerminal(cmd, terminalCommands.resume);
        triggerResumeWithConfetti();
        return;
      }}

      if (terminalCommands[cmd]) {{
        printTerminal(cmd, terminalCommands[cmd]);
      }} else {{
        printTerminal(cmd, `Command '${{cmd}}' not recognized. Type 'help' for available commands.`);
      }}
    }}

    if (termInput) {{
      termInput.addEventListener('keydown', (e) => {{
        if (e.key === 'Enter') {{
          const val = termInput.value;
          termInput.value = '';
          executeTerminalCommand(val);
        }}
      }});
    }}

    function bootTerminalAnimation() {{
      const bootLines = [
        "[BOOT] Initializing Hajrah Saleha Kazi Shell v2.6.4...",
        "[OK] Identity: AI/ML Engineer & Computer Vision Specialist",
        "[OK] Status: AVAILABLE &mdash; Open for Paid Internships, Part-Time & Freelance",
        "[READY] Type 'help' or click any command chip below to explore:"
      ];
      let delay = 300;
      bootLines.forEach((line) => {{
        setTimeout(() => {{
          const p = document.createElement('div');
          p.className = 'text-[11px] font-mono text-appMuted leading-tight';
          p.innerHTML = line;
          termHistory.appendChild(p);
          const scr = document.getElementById('terminal-screen');
          scr.scrollTop = scr.scrollHeight;
          playTone(600, 'sine', 0.03, 0.01);
        }}, delay);
        delay += 250;
      }});
    }}
    window.addEventListener('DOMContentLoaded', bootTerminalAnimation);

    // --- CONTACT FORM SUBMISSION ---
    function handleContactSubmit(e) {{
      e.preventDefault();
      playTone(700, 'sine', 0.2);
      triggerConfetti();
      alert('Thank you! Your message has been prepared for Hajrah. She will respond promptly to discuss this opportunity.');
      e.target.reset();
    }}

    // Global Escape Key Listener for Modals
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeStoryModal();
        closeCertModal();
        closeResumeModal();
        closeBookModal();
        closeMobileMenu();
      }}
    }});

    // Initialize Lucide icons on load
    window.addEventListener('DOMContentLoaded', () => {{
      lucide.createIcons();
    }});
  </script>
</body>
</html>
'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully! Total bytes:", len(html))

if __name__ == '__main__':
    build_elite_html()

